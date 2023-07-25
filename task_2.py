# 2. Превратите функции в методы класса.
# Задачи должны решаться через вызов методов экземпляра.
# Например: Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.

from random import randint
class Quest:
    def __init__(self, LOWER_LIMIT, UPPER_LIMIT, COUNTER) -> str:
        self.LOWER_LIMIT = LOWER_LIMIT
        self.UPPER_LIMIT = UPPER_LIMIT
        self.COUNTER = COUNTER
    def get_random_num(self):
        num = randint(self.LOWER_LIMIT, self.UPPER_LIMIT)
        return num

    def get_answer(self):
        r_num = self.get_random_num()
        i = 0
        while i < self.COUNTER:
            i += 1
            input_num = int(input(f'Введите число больше {self.LOWER_LIMIT} и меньше {self.UPPER_LIMIT} : '))
            if input_num > r_num:
                print(f'Число больше\n Осталось попыток {self.COUNTER - i}')
            elif input_num < r_num:
                print(f'Число меньше\n Осталось попыток {self.COUNTER - i}')
            elif input_num == r_num:
                print('Вы угадали число!')
                break
            else:
                print(f'Вы не угадали число {r_num}')
        return f'Загаданное число {r_num}'


q = Quest(1, 10, 3)
print(q.get_answer())
