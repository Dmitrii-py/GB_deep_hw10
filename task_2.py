# 2. Превратите функции в методы класса.
# Задачи должны решаться через вызов методов экземпляра.
# Например: Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.

from random import randint
class Quest:
    def __init__(self, lower_limit: int, upper_limit: int, counter) -> str:
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.counter = counter
    def get_random_num(self):
        num = randint(self.lower_limit, self.upper_limit)
        return num

    def get_answer(self):
        r_num = self.get_random_num()
        i = 0
        while i < self.counter:
            i += 1
            input_num = int(input(f'Введите число больше {self.lower_limit} и меньше {self.upper_limit} : '))
            if input_num > r_num:
                print(f'Число больше\n Осталось попыток {self.counter - i}')
            elif input_num < r_num:
                print(f'Число меньше\n Осталось попыток {self.counter - i}')
            elif input_num == r_num:
                print('Вы угадали число!')
                break
            else:
                print(f'Вы не угадали число {r_num}')
        return f'Загаданное число {r_num}'


q = Quest(1, 10, 3)
print(q.get_answer())
