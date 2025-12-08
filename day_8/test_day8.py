from day_8.main import Main

def test_part1_example():
    main = Main("day_8/example.txt")
    result = main.part1(10)
    assert result == 40

def test_part1_actual():
    main = Main("day_8/input.txt")
    result = main.part1(1000)
    assert result == 24360

def test_part2_example():
    main = Main("day_8/example.txt")
    result = main.part2(100)
    assert result == 25272

def test_part2_actual():
    main = Main("day_8/input.txt")
    result = main.part2(10000)
    assert result == 2185817796
