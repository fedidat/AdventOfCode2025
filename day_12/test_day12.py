from day_12.main import Main

def test_part1_example():
    main = Main("day_12/example.txt")
    result = main.part1()
    assert result == 1

def test_part1_actual():
    main = Main("day_12/input.txt")
    result = main.part1()
    assert result == 457
