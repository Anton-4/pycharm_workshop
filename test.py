from bloedgroepen import calcGroup


def test_calc_group_1():
    assert "O+ O- {O+,O-}" == calcGroup("O+", "O-", "?")


def test_calc_group_2():
    assert "O- O- O-" == calcGroup("O-", "O-", "?")


def test_calc_group_3():
    assert "O+ {A+,A-,B+,B-,O+,O-} O-" == calcGroup("O+", "?", "O-")


def test_calc_group_4():
    assert "AB- AB+ {A+,A-,AB+,AB-,B+,B-}" == calcGroup("AB-", "AB+", "?")


def test_calc_group_5():
    assert "AB+ ONMOGELIJK O+" == calcGroup("AB+", "?", "O+")
