from add_class.addition import *


def celsius_to_fahrenheit(celsius: float) -> float:
    fahrenheit = add(multiply(celsius, 1.8), 32)
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    celsius = div(sub(fahrenheit, 32), 1.8)
    return celsius


def collect_multiple_temperature():
    temp = input('Enter 10 temperature, each temp should be separated with a comma(,): ')

    temp = temp.split()

    for element in temp:
        int_result = celsius_to_fahrenheit(int(element))
        print(int_result)


def main():
    collect_multiple_temperature()


if __name__ == '__main__':
    main()
