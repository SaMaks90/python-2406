

class Calculator:
    def __init__(self, save_history=True):
        self.save_history = save_history
        self.history = []
        self.id_transaction = 0

    def add(self, a, b):
        sum_ = a + b
        if self.save_history:
            self.id_transaction += 1
            self.history.append({
                'operation': 'add',
                'transaction': self.id_transaction,
                'Arguments': (a, b),
                'Result': sum_
            })

        return sum_

    def sub(self, a, b):
        sub_ = a - b
        if self.save_history:
            self.id_transaction += 1
            self.history.append({
                'operation': 'add',
                'transaction': self.id_transaction,
                'Arguments': (a, b),
                'Result': sub_
            })

        return sub_
