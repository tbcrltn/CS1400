import pytest
from dessert import DessertItem


class Test(DessertItem):
    def __init__(self, name):
        DessertItem.__init__(self, name)

    def calculate_cost(self):
        return 0.00
    def calculate_tax(self):
        return 0.00


def test_dessert():
    dessert = Test("name")
    assert dessert.name == "name"

    dessert.name = "diffname"
    assert dessert.name == "diffname"

def test_operators():
    test = Test("name")
    test2 = Test("name")
    assert test == test2
    assert not test > test2
    assert not test < test2
    assert test >= test2
    assert test <= test2
    
    

    




    





