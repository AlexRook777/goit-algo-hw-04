import turtle

def koch_curve(t, order, size):
    """
    Draws a Koch curve of the given order and size.

    The Koch curve is a fractal curve and one of the classic examples of
    self-similarity. It is drawn by recursively drawing a sequence of
    lines at a 60 degree angle, with each line being one-third the size
    of the previous one.

    :param t: the turtle to draw with
    :param order: the order of the Koch curve (higher values produce more
        detailed curves)
    :param size: the size of the curve (default is 300)
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    """
    Draws a Koch curve of the given order and size.

    This function draws a Koch curve in a window using the turtle graphics
    library. The curve is drawn by recursively drawing a sequence of lines
    at a 60 degree angle, with each line being one-third the size of the
    previous one.

    :param order: the order of the Koch curve (higher values produce more
        detailed curves)
    :param size: the size of the curve (default is 300)
    """
    window = turtle.Screen()
    window.bgcolor("black")

    t = turtle.Turtle()
    t.color("white")
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    t.hideturtle()
    window.mainloop()


def main():
    """
    Draws a Koch curve with the given level of recursion.

    This function prompts the user to enter a level of recursion and then
    draws a Koch curve with that level. If the user enters an invalid
    input (e.g. a negative number or a non-integer), it prints an
    error message and continues to the next iteration.

    :param None: no parameters
    :return None: no return value
    """
    while True:
        try:
            # Запитуємо користувача ввести рівень рекурсії
            level = input("Будь ласка, введіть рівень рекурсії (ціле число, наприклад, 3 або 4): ")
            level = int(level)
            if level < 0:
                print("Рівень не може бути від'ємним. Спробуйте ще раз.")
                continue
            break  # Виходимо з циклу, якщо ввід коректний
        except ValueError:
            print("Некоректний ввід. Будь ласка, введіть ціле число.")
            
    # Викликаємо функцію малювання з рівнем, який ввів користувач
    draw_koch_curve(level)

if __name__ == '__main__':
    main()