# This is a sample Python script.
from PIL import Image

# граница от которой отходим чтобы не было слишком близко
EPS = 3


def digit_in_square(x1, y1, x2, y2, x3, y3, x4, y4):
    begin = 200
    length = 454
    if min(x1, x2, x3, x4) > (begin + EPS):
        return False
    if max(x1, x2, x3, x4) < (begin + length - EPS):
        return False
    if min(y1, y2, y3, y4) > (begin + EPS):
        return False
    if max(y1, y2, y3, y4) < (begin + length - EPS):
        return False

    return True


def rectangle_intersection(x1, y1, x2, y2, x3, y3, x4, y4, a1, b1, a2, b2, a3, b3, a4, b4):
    if (min(x1, x2, x3, x4) > max(a1, a2, a3, a4)):
        return False
    if (max(x1, x2, x3, x4) < min(a1, a2, a3, a4)):
        return False
    if (max(y1, y2, y3, y4) < min(b1, b2, b3, b4)):
        return False
    if (min(y1, y2, y3, y4) > max(b1, b2, b3, b4)):
        return False

    return True

def test

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
