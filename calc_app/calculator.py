def add(num1: float, num2: float) -> float:
    num3 = num1 + num2
    return num3


def subt(num1: float, num2: float) -> float:
    num3 = num1 - num2
    return num3


def multiply(num1: float, num2: float) -> float:
    num3 = num1 * num2
    return num3


def divide(num1: float, num2: float) -> float:
    num3 = num1 / num2
    return num3


def sqr(num1: float) -> float:
    num2 = num1 ** 2
    return num2


def sq_rt(num1: float) -> float:
    num2 = num1 ** 0.5
    return num2


def main():
    x = 2
    y = 10
    z = add(x, y)
    print(f' x + y: {x} + {y} = {z}')


if __name__ == '__main__':
    main()
