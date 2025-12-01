from day_1.main import Main

def test_part1_example():
    main = Main("day_1/example.txt")
    result = main.part1()
    assert result == 3

def test_part1_actual():
    main = Main("day_1/input.txt")
    result = main.part1()
    assert result == 1172

def test_part2_example():
    main = Main("day_1/example.txt")
    result = main.part2()
    assert result == 6

def test_part2_actual():
    main = Main("day_1/input.txt")
    result = main.part2()
    assert result == 6932
