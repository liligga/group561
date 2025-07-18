from lessons.lesson_1 import Car

class Money:
    USD_TO_KGS = 87
    # Dunder methods - double underscore
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"Money(mount={self.amount}, currency={self.currency})"

    def __eq__(self, other):
        if self.currency == other.currency \
            and self.amount == other.amount:
            return True
        return False

    # gt - greater than >
    # ge - greater or equal >=
    # lt - less than
    # le - less than or equal
    def __gt__(self, other):
        if self.currency == other.currency and self.amount > other.amount:
            return True
        if self.currency != other.currency:
            if self.currency == 'USD':
                self_amount = self.amount * Money.USD_TO_KGS
            elif self.currency == 'KGS':
                self_amount = self.amount
            if other.currency == 'USD':
                other_amount = other.amount * Money.USD_TO_KGS
            elif self.currency == 'KGS':
                other_amount = other.amount
            if self_amount > other_amount:
                return True
        return False

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            raise ValueError("Нельзя складывать деньги с разными валютами")

    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)

m1 = Money(100, "KGS")
m3 = Money(100, "KGS")
m2 = Money(100, "USD")
m4 = Money(101, "KGS")
print(m1)
print(m2 == m1)
print(m3 == m1)
print(m4 > m3)
print(m1+m3)
print(m4-m3)

car1 = Car("Ford", 2000)
print(car1)