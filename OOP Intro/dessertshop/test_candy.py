import pytest
from dessert import Candy


class TestObj:
    pass

def test_candy():
    candy = Candy("name", 0, 0)
    assert candy.name == "name"
    assert candy.candy_weight == 0
    assert candy.price_per_pound == 0
    assert candy.packaging == "Bag"
    assert round(candy.calculate_cost(), 2) == 0.0

    candy.name = "diffname"
    candy.candy_weight = 5
    candy.price_per_pound = 5
    assert candy.name == "diffname"
    assert candy.candy_weight == 5
    assert candy.price_per_pound == 5
    assert round(candy.calculate_cost(), 2) == 25.0

def test_combine():
    candy = Candy("name", 0, 0)
    candy2 = Candy("name", 1, 0)
    candy3 = Candy("name", 0, 1)
    candy4 = Candy("other", 0, 0)
    candy5 = TestObj()
    assert candy.can_combine(candy2)
    assert not candy.can_combine(candy3)
    assert not candy.can_combine(candy4)
    assert not candy.can_combine(candy5)

    candy.combine(candy2)
    assert candy.name == "name"
    assert candy.candy_weight == 1
    
    with pytest.raises(TypeError):
        candy.combine(candy5)






