from fitrate._fit import contain, scale_down


def test_contain() -> None:
    assert contain((200, 200), 60000) == (244, 244)
    assert contain((400, 300), 60000) == (282, 212)
    assert contain((100, 300, 200), 100000) == (25, 76, 51)


def test_scale_down() -> None:
    assert scale_down((200, 200), 60000) == (200, 200)
    assert scale_down((400, 300), 60000) == (282, 212)
