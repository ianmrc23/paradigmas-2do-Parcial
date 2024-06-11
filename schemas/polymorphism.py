from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> float:
        pass


class CashPayment(PaymentMethod):
    def process_payment(self, amount: float) -> float:
        return amount


class CardPayment(PaymentMethod):
    def process_payment(self, amount: float) -> float:
        return amount * 0.7


class QRPayment(PaymentMethod):
    def process_payment(self, amount: float) -> float:
        return amount * 0.9


def process_payment(
    payment_method: PaymentMethod,
    total_amount: float
) -> float:
    return payment_method.process_payment(total_amount)


class ShippingMethod(ABC):
    @abstractmethod
    def calculate_shipping_cost(self, weight: float, distance_from_store: float, total_products: int) -> float:
        pass


class StandardShipping(ShippingMethod):
    def calculate_shipping_cost(self, weight: float, distance_from_store: float, total_products: int) -> float:
        return 5 + weight * 0.5 + distance_from_store * 0.1


class ExpressShipping(ShippingMethod):
    def calculate_shipping_cost(self, weight: float, distance_from_store: float, total_products: int) -> float:
        return 10 + weight + distance_from_store * 0.2 + total_products * 0.2


class InStorePickup(ShippingMethod):
    def calculate_shipping_cost(self, weight: float, distance_from_store: float, total_products: int) -> float:
        return 0


def calculate_shipping(
        shipping_method: ShippingMethod,
        weight: float,
        distance_from_store: float,
        total_products: int
) -> float:
    return shipping_method.calculate_shipping_cost(weight, distance_from_store, total_products)
