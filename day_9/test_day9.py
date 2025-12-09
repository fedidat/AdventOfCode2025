from day_9.main import Main

def test_part1_example():
    main = Main("day_9/example.txt")
    result = main.part1()
    assert result == 50

def test_part1_actual():
    main = Main("day_9/input.txt")
    result = main.part1()
    assert result == 4743645488

def test_part2_example():
    main = Main("day_9/example.txt")
    result = main.part2()
    assert result == 24

def test_part2_actual():
    main = Main("day_9/input.txt")
    result = main.part2()
    assert result == 1529011204
