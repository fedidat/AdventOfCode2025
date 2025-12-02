from day_2.main import Main

def test_part1_example():
    main = Main("day_2/example.txt")
    result = main.part1()
    assert result == 1227775554

def test_part1_actual():
    main = Main("day_2/input.txt")
    result = main.part1()
    assert result == 19574776074

def test_part2_example():
    main = Main("day_2/example.txt")
    result = main.part2()
    assert result == 4174379265

def test_part2_actual():
    main = Main("day_2/input.txt")
    result = main.part2()
    assert result == 25912654282
