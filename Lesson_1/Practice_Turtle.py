def hypot(a, b):
    # Вычисление гипотенузы
    c = (a ** 2 + b ** 2) ** 0.5
    return c


# print(hypot(3,4))

def coord_quarter():
    """
    Determines by the entered x, y coordinates in which coordinate quarter the point is located
    :return: Print the number of the coordinate quarter
    """
    x = int(input('Введите координату x: '))
    y = int(input('Введите координату y: '))
    if x > 0:
        if y > 0:
            print('Первая четверть')
        else:
            print('Четвёртая четверть')
    else:
        if y > 0:
            print('Вторая четверть')
        else:
            print('Третья четверть')


def coord_quarter2():
    """
    Determines by the entered x, y coordinates in which coordinate quarter the point is located
    Using a cascading sequence of conditions.
    :return: Print the number of the coordinate quarter

    """

    x = int(input('Введите координату x: '))
    y = int(input('Введите координату y: '))
    if x > 0 and y > 0:
        print('Первая четверть')
    elif x > 0 > y:
        print('Четвёртая четверть')
    elif y > 0:
        print('Вторая четверть')
    else:
        print('Третья четверть')


# coord_quarter2()


def draw_turtle_S():
    """
    Exercise 2 Рисуем исполнителем Черепаха букву S
    :return:
    """

    import turtle
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)


# draw_turtle_S()

def draw_turtle_square():
    """
     Exercise 3 Рисуем исполнителем Черепаха букву квадрат
    :return:
    """

    import turtle
    turtle.shape('turtle')
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)


#draw_turtle_square()


def draw_turtle_circle():
    """
    Exercise 4 Рисуем исполнителем Черепаха окружность
    :return:
    """

    import turtle
    turtle.shape('turtle')
    n=int(input('Введите количество углов в мноноугольнике: ')) # Задаём количество углов в многоугольнике
    a = 180-((n-2)/n)*180 # Рассчитываем угол поворота исполнитея при рисовании многоугольника
    for i in range(1,n+1):
        turtle.forward(10)
        turtle.left(a)
    turtle.exitonclick()


#draw_turtle_circle()

def draw_turtle_ten_square():
    """
    Exercise 5 Рисуем исполнителем Черепаха n вложенных квадратов
    :return:
    """

    import turtle
    turtle.shape('turtle')
    turtle.speed(10)
    n = int(input('Введите количество квадратов: '))  # Задаём количество квадратов
    a = int(input('Введите длину стороны квадрата: '))
    h = a / 2 # Рассчёт расстояния между сторонами квадрата
    for j in range(1,n+1):
        for i in range(1, 5):
            turtle.forward(a)
            turtle.left(90)
        turtle.penup()
        turtle.goto(0-j*h,0-j*h)
        turtle.pendown()
        a=a+2*h

    turtle.exitonclick()


#draw_turtle_ten_square()

def draw_turtle_spider():
    """
    Exercise 6 Рисуем исполнителем Черепаха паука с n лапками
    :return:
    """

    import turtle
    turtle.shape('turtle')
    turtle.speed(5)
    n = int(input('Введите лапок: '))  # Задаём количество лапок
    a = int(input("Введите длину лапки: ")) # Задаём  длину лапки
    w=360/n # Задаём угол поворота лапки
    for j in range(1,n+1):
        turtle.forward(a)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(a)
        turtle.left(w)

    turtle.exitonclick()


#draw_turtle_spider()