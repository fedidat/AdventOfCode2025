from day_11.main import Main

def test_part1_example():
    main = Main("day_11/example.txt")
    result = main.part1()
    assert result == 5

def test_part1_actual():
    main = Main("day_11/input.txt")
    result = main.part1()
    assert result == 470

def test_part2_example():
    main = Main("day_11/example2.txt")
    result = main.part2()
    assert result == 2

def test_part2_actual():
    main = Main("day_11/input.txt")
    result = main.part2()
    assert result == 384151614084875
