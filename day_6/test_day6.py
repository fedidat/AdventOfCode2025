from day_6.main import Main

def test_part1_example():
    main = Main("day_6/example.txt")
    result = main.part1()
    assert result == 4277556

def test_part1_actual():
    main = Main("day_6/input.txt")
    result = main.part1()
    assert result == 5346286649122

def test_part2_example():
    main = Main("day_6/example.txt")
    result = main.part2()
    assert result == 3263827

def test_part2_actual():
    main = Main("day_6/input.txt")
    result = main.part2()
    assert result == 10389131401929
