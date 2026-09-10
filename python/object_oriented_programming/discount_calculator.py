from abc import ABC, abstractmethod
import uuid


class User:
    def __init__(self, tier: str) -> None:
        if not isinstance(tier, str):
            raise TypeError('User tier must be a string.')
        if not tier.strip():
            raise ValueError('User tier cannot be empty.')
        if tier not in ('free', 'premium'):
            raise ValueError('User tier must be "free" or "premium".')

        self.user_id = uuid.uuid4()
        self.tier = tier.lower()


class Product:
    def __init__(self, name: str, price: float | int) -> None:
        if not isinstance(name, str):
            raise TypeError('Product name must be a string.')
        if not name.strip():
            raise ValueError('Product name cannot be empty.')
        if not isinstance(price, (float, int)):
            raise TypeError('Price must be a number.')
        if price <= 0:
            raise ValueError('Price must be greater than 0.')

        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} — ${self.price}'


class DiscountStrategy(ABC):
    @abstractmethod
    def is_applicable(self, product: Product, user: User) -> bool:
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float | int) -> None:
        if not isinstance(percentage, (float, int)):
            raise TypeError('Percentage must be a number.')
        if percentage <= 0:
            raise ValueError('Percentage must be greater than 0.')

        self.percentage = percentage

    def is_applicable(self, product: Product, user: User) -> bool:
        return self.percentage <= 70

    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percentage / 100)


class FixedDiscount(DiscountStrategy):
    def __init__(self, amount: float | int) -> None:
        if not isinstance(amount, (float, int)):
            raise TypeError('Discount amount must be a number.')
        if amount <= 0:
            raise ValueError('Discount amount must be greater than 0.')

        self.amount = amount

    def is_applicable(self, product: Product, user: User) -> bool:
        return product.price * 0.9 > self.amount

    def apply_discount(self, product: Product) -> float:
        return product.price - self.amount


class PremiumUserDiscount(DiscountStrategy):
    def is_applicable(self, product: Product, user: User) -> bool:
        return user.tier == 'premium'

    def apply_discount(self, product: Product) -> float:
        return product.price * 0.8


class DiscountEngine:
    def __init__(self, strategies: list[DiscountStrategy]) -> None:
        if not isinstance(strategies, list):
            raise TypeError('Discount strategies must be a list.')
        if not len(strategies):
            raise ValueError('Discount strategies list cannot be empty.')
        if any(not isinstance(strategy, DiscountStrategy) for strategy in strategies):
            raise TypeError('Every strategy must be a DiscountStrategy instance.')

        self.strategies = strategies

    def calculate_best_price(self, product: Product, user: User) -> float:
        prices = [product.price]

        for strategy in self.strategies:
            if strategy.is_applicable(product, user):
                discounted = strategy.apply_discount(product)
                prices.append(discounted)

        return min(prices)


product = Product('Wireless Mouse', 52.99)

assert str(product) == 'Wireless Mouse — $52.99'

free_user = User('free')
premium_user = User('premium')

assert free_user.tier == 'free'
assert premium_user.tier == 'premium'

discount_engine = DiscountEngine([
    PercentageDiscount(10),
    FixedDiscount(5),
    PremiumUserDiscount(),
])

assert discount_engine.calculate_best_price(product, free_user) == 47.691
assert discount_engine.calculate_best_price(product, premium_user) == 42.392
