from day_4.main import Main

def test_part1_example():
    main = Main("day_4/example.txt")
    result = main.part1()
    assert result == 13

def test_part1_actual():
    main = Main("day_4/input.txt")
    result = main.part1()
    assert result == 1523

def test_part2_example():
    main = Main("day_4/example.txt")
    result = main.part2()
    assert result == 43

def test_part2_actual():
    main = Main("day_4/input.txt")
    result = main.part2()
    assert result == 9290
