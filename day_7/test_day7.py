from day_7.main import Main

def test_part1_example():
    main = Main("day_7/example.txt")
    result = main.part1()
    assert result == 21

def test_part1_actual():
    main = Main("day_7/input.txt")
    result = main.part1()
    assert result == 1579

def test_part2_example():
    main = Main("day_7/example.txt")
    result = main.part2()
    assert result == 40

def test_part2_actual():
    main = Main("day_7/input.txt")
    result = main.part2()
    assert result == 13418215871354
