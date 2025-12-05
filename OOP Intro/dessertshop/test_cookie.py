import pytest
from dessert import Cookie



class TestObj:
    pass

def test_cookie():
    cookie = Cookie("name", 0, 0)
    assert cookie.name == "name"
    assert cookie.cookie_ammount == 0
    assert cookie.price_per_dozen == 0
    assert cookie.packaging == "Box"
    assert round(cookie.calculate_cost(), 2) == 0.0

    cookie.name = "diffname"
    cookie.cookie_ammount = 5
    cookie.price_per_dozen = 12
    assert cookie.name == "diffname"
    assert cookie.cookie_ammount == 5
    assert cookie.price_per_dozen == 12
    assert round(cookie.calculate_cost(), 2) == 5.0

def test_combine():
    cookie = Cookie("name", 0, 0)
    cookie2 = Cookie("name", 1, 0)
    cookie3 = Cookie("name", 0, 1)
    cookie4 = Cookie("other", 0, 0)
    cookie5 = TestObj()
    assert cookie.can_combine(cookie2)
    assert not cookie.can_combine(cookie3)
    assert not cookie.can_combine(cookie4)
    assert not cookie.can_combine(cookie5)

    cookie.combine(cookie2)
    assert cookie.name == "name"
    assert cookie.cookie_ammount == 1
    
    with pytest.raises(TypeError):
        cookie.combine(cookie5)