from day_5.main import Main

def test_part1_example():
    main = Main("day_5/example.txt")
    result = main.part1()
    assert result == 3

def test_part1_actual():
    main = Main("day_5/input.txt")
    result = main.part1()
    assert result == 513

def test_part2_example():
    main = Main("day_5/example.txt")
    result = main.part2()
    assert result == 14

def test_part2_actual():
    main = Main("day_5/input.txt")
    result = main.part2()
    assert result == 339668510830757
