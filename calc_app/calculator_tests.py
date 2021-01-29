from calc_app.calculator import *


def run_tests():
    """ tests all the functions"""
    assert add(2, 3) == 5, "2 + 3 is 5"
    assert subt(2, 3) == -1, "2 -3 is -1"
    assert multiply(2, 3) == 6, " 2 * 3 is 6"
    assert divide(4, 2) == 2, " 4 / 2 is 2"
    assert sqr(2) == 4, "2 ** 2 is 4"
    assert sq_rt(4) == 2, "4 ** 0.5 is 2"


if __name__ == '__main__':
    print('starting test')
    run_tests()
    print('test end')