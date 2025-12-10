from day_10.main import Main

def test_part1_example():
    main = Main("day_10/example.txt")
    result = main.part1()
    assert result == 7

def test_part1_actual():
    main = Main("day_10/input.txt")
    result = main.part1()
    assert result == 434

def test_part2_example():
    main = Main("day_10/example.txt")
    result = main.part2()
    assert result == 33

def test_part2_actual():
    main = Main("day_10/input.txt")
    result = main.part2()
    assert result == 6932
