from fitrate import calc


def test_calc() -> None:
    assert calc((400, 300), 60000) == (282, 212)
    assert calc((100, 300, 200), 100000) == (25, 76, 51)
