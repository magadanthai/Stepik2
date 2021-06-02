class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    def __str__(self):
        return f'Ваше состояние составляет {self.total_cents // 100} долларов {self.total_cents % 100} центов'

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_cents = self.total_cents % 100 + value * 100
        else:
            print('Error dollars')

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 0 < value < 100:
            self.total_cents = self.total_cents // 100 * 100 + value
        else:
            print('Error cents')


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов

