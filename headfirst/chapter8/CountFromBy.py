class CountFromBy:

    # Переопределение метода из базового класса Object для инициализации параметров.
    # Метод вызывается при каждом создании экземпляров класса.
    # С аргуметами "по умолчанию" будет доступно несколько конструкторов (см. примеры)
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.incr = i

    # self (текущий объект) всегда должен быть первым аргументом в ЛЮБОМ методе класса.
    #
    # При вызове метода у объекта:
    #   c = CountFromBy()
    #   c.increase()
    # компилятор неявно передает ссылку экземпляра вызывающего класса при вызове метода:
    #   CountFromBy.increase(c)
    #
    # self.val - обращение к переменной этого экземпляра
    def increase(self) -> None:
        self.val += self.incr

    # Переопределение метода строкового отображения экземпляра.
    # По умолчанию '<__main__.CountFromBy object at <hex(id)>'
    def __repr__(self) -> str:
        return 'val = ' + str(self.val)


# Оба аргумента присваиваются по умолчанию
a = CountFromBy()
print('a: ', a.val)
print(a.incr)
a.increase()
print(a.val)

# Первый аргумент присваивается явно, второй по умолчанию
b = CountFromBy(50)
print('\nb: ', b.val)
print(b.incr)
b.increase()
print(b.val)

# Первый аргумент присваивается по умолчанию, второй явно
c = CountFromBy(i=50)
print('\nc: ', c.val)
print(c.incr)
c.increase()
print(c.val)

# Оба аргумента присваиваются явно
d = CountFromBy(100, 10)
print('\nc: ', d.val)
print(d.incr)
d.increase()
print(d.val)

print('\nобъект "d": ', d)
print('инфо о классе: ', type(d))
print('id (адрес) объекта в памяти: ', id(d))
print('16-ричное значение id объекта: ', hex(id(d)))
