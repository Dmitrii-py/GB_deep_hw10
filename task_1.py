# 1. Превратите функции в методы класса.
# Задачи должны решаться через вызов методов экземпляра.
# Например: Треугольник существует только тогда,
# когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник
# разносторонним, равнобедренным или равносторонним.

class Triangle:
    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def check_on_exist_triangle(self) -> bool:
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            res = False
        else:
            res = True
        return res

    def get_type_triangle(self) -> str:
        triangle = self.check_on_exist_triangle()
        if triangle:
            if self.a != self.b and self.a != self.c and self.b != self.c:
                type_tr = 'Разносторонний'
            elif self.a == self.b == self.c:
                type_tr = 'Равносторонний'
            else:
                type_tr = 'Равнобедренный'
        else:
            type_tr = "Треугольник не существует"
        return type_tr


t = Triangle(2, 2, 2)
print(t.get_type_triangle())
