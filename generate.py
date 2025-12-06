import os
import shutil
from datetime import datetime
import json

# Get current day of the month
n = datetime.now().day
SRC = "day_1"
DST = f"day_{n}"

# Copy folder if it doesn't exist
if not os.path.exists(DST):
    shutil.copytree(SRC, DST)
    # Replace all occurrences of 'day_1' with 'day_n' in files
    for root, _, files in os.walk(DST):
        for file in files:
            if file.endswith('.py') or file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = content.replace('day_1', f'day_{n}')
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
    # Rename test_day1.py to test_dayn.py
    old_test_file = os.path.join(DST, "test_day1.py")
    new_test_file = os.path.join(DST, f"test_day{n}.py")
    if os.path.exists(old_test_file):
        os.rename(old_test_file, new_test_file)
else:
    print(f"{DST} already exists.")

# Update settings.json
settings_path = os.path.join('.vscode', 'settings.json')
if os.path.exists(settings_path):
    with open(settings_path, 'r', encoding='utf-8') as f:
        settings = json.load(f)
    pytest_args = settings.get('python.testing.pytestArgs', [])
    if DST not in pytest_args:
        pytest_args.append(DST)
        settings['python.testing.pytestArgs'] = pytest_args
        with open(settings_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=4)
else:
    print("settings.json not found.")
