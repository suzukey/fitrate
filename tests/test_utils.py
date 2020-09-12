from fitrate.utils import gcd, nthrt, prod


def test_gcd() -> None:
    assert gcd(*(300, 400)) == 100
    assert gcd(*[200, 400, 1000]) == 200
    assert gcd(27, 123, 57, 255) == 3


def test_nthrt() -> None:
    assert nthrt(25, 2) == 5
    assert nthrt(27, 3) == 3
    assert nthrt(16, 4) == 2


def test_prod() -> None:
    assert prod(*[5, 10]) == 50
    assert prod(*(3.5, 4.5, 5)) == 78.75
    assert prod(3, 5, 2, 2) == 60
