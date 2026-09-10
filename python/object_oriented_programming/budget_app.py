from __future__ import annotations


class Category:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ledger: list[dict[str, float | int | str]] = []

    def deposit(self, amount: float | int, description: str = '') -> None:
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount: float | int, description: str = '') -> bool:
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self) -> float | int:
        return sum(transaction['amount'] for transaction in self.ledger)

    def transfer(self, amount: float | int, category: Category) -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount: float | int) -> bool:
        return self.get_balance() >= amount

    def __str__(self) -> str:
        name = self.name[:30] if len(self.name) > 30 else self.name
        title = f'{name:*^30}\n'

        ledger_entries = ''
        for item in self.ledger:
            amount = item['amount']
            formatted_amount = f'{amount:.2f}'

            description = item['description']
            trimmed_description = (
                description[:23] if len(description) > 23 else description
            )
            formatted_description = f'{trimmed_description:<{len(trimmed_description)}}'

            ledger_entries += f'{formatted_description}{formatted_amount:>{30 - len(formatted_description)}}\n'

        total = f'Total: {self.get_balance():.2f}'
        return title + ledger_entries + total


def create_spend_chart(categories: list[Category]) -> str:
    total_withdrawals = abs(
        sum(
            sum(item['amount'] for item in category.ledger if item['amount'] < 0)
            for category in categories
        )
    )

    percentages: list[int] = []
    for category in categories:
        category_withdrawals = abs(
            sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        )

        if total_withdrawals == 0:
            percentages.append(0)
        else:
            percentages.append(int(category_withdrawals / total_withdrawals * 100))

    bar_chart = 'Percentage spent by category\n\n'

    for i in range(100, -1, -10):
        bar_chart += f'{i:>3}| '

        for percentage in percentages:
            if percentage >= i:
                bar_chart += 'o' + (' ' * 2)
            else:
                bar_chart += ' ' * 3

        bar_chart += '\n'

    bar_chart += ' ' * 4 + '-' * (len(categories) * 3 + 1) + '\n'

    longest_name_length = max(len(category.name) for category in categories)

    for i in range(longest_name_length):
        bar_chart += ' ' * 5
        for category in categories:
            if i < len(category.name):
                bar_chart += category.name[i] + (' ' * 2)
            else:
                bar_chart += ' ' * 3
        bar_chart += '\n'

    return bar_chart[:-1]


food = Category('Food')
clothing = Category('Clothing')

food.deposit(1000, 'initial deposit')

assert food.get_balance() == 1000
assert food.check_funds(500)
assert not food.get_balance() == 1001

food.withdraw(10.15, 'groceries')

assert food.get_balance() == 989.85
assert food.ledger[-1] == {'amount': -10.15, 'description': 'groceries'}

assert food.withdraw(2000, 'too expensive') is False
assert food.get_balance() == 989.85

assert food.transfer(50, clothing) is True
assert food.get_balance() == 939.85
assert clothing.get_balance() == 50

assert food.ledger[-1]['description'] == 'Transfer to Clothing'
assert clothing.ledger[-1]['description'] == 'Transfer from Food'

output = str(food)

assert 'Food' in output
assert 'initial deposit' in output
assert 'groceries' in output
assert 'Transfer to Clothing' in output
assert 'Total: 939.85' in output

auto = Category('Auto')
auto.deposit(900, 'initial deposit')
auto.withdraw(120, 'gas')

clothing.withdraw(25)

expected_chart = """Percentage spent by category

100|          
 90|          
 80|          
 70|          
 60|          
 50|       o  
 40|       o  
 30|       o  
 20| o     o  
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     """

assert create_spend_chart([food, clothing, auto]) == expected_chart
