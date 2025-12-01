from typing import Protocol, Literal

PayType = Literal["CASH", "CARD", "PHONE"]

class Payable(Protocol):
    def get_pay_type(self) -> PayType:
        pass

    def set_pay_type(self, payment_method: PayType) -> None:
        pass


