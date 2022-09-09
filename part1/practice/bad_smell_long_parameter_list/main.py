# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, state):
        self.state = state
        self.speed = 1
        self.y = 0
        self.x = 0

    def move(self, direction, field):
        speed = self._get_speed()

        if direction == 'UP':
            field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            field.set_unit(y=self.y, x=self.x + speed, unit=self)

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Эк тебя раскорячило')
#     ...
