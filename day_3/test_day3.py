from day_3.main import Main

def test_part1_example():
    main = Main("day_3/example.txt")
    result = main.part1()
    assert result == 357

def test_part1_actual():
    main = Main("day_3/input.txt")
    result = main.part1()
    assert result == 17263

def test_part2_example():
    main = Main("day_3/example.txt")
    result = main.part2()
    assert result == 3121910778619

def test_part2_actual():
    main = Main("day_3/input.txt")
    result = main.part2()
    assert result == 170731717900423
