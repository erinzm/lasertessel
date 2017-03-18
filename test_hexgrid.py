from hexgrid import Hex

def test_coord_construction():
    hex = Hex(1, 3)
    assert hex.q == 1
    assert hex.r == 3
    assert hex.s == -1-3

def test_eq():
    hex1 = Hex(1, 3)
    hex2 = Hex(1, 3)
    hex3 = Hex(4, 2)
    assert hex1 == hex2
    assert hex1 != hex3
