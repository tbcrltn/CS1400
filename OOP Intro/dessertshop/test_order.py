import pytest
from dessert import Order, Cookie
from payment import PayType

def test_set_and_get():
    order = Order()
    order.set_pay_type("CASH")
    assert order.get_pay_type() == "CASH"
    order.set_pay_type("CARD")
    assert order.get_pay_type() == "CARD"
    order.set_pay_type("PHONE")
    assert order.get_pay_type() == "PHONE"


def test_value_error():
    order = Order()
    with pytest.raises(ValueError):
        order.set_pay_type("CREDITCARD")

    order._pay_type = "CREDITCARD"

    with pytest.raises(ValueError):
        order.get_pay_type()

def test_sort_method():
    order = Order()
    order.add(Cookie("cookie", 12, 1))
    order.add(Cookie("cookie", 12, 2))
    order.add(Cookie("cookie", 12, 2))
    list1 = sorted(order.order)
    order.sort()
    assert list1 == order.order

def test_iter_next():
    order = Order()
    order.add(Cookie("cookie", 12, 1))
    order.add(Cookie("cookie", 12, 2))
    order.add(Cookie("cookie", 12, 3))
    iterator = iter(order)
    assert next(iterator) == Cookie("cookie", 12, 1)
    assert next(iterator) == Cookie("cookie", 12, 2)
    assert next(iterator) == Cookie("cookie", 12, 3)
    

