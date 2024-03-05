import math
import statistics


def distance(x1loc, y1loc, x2loc, y2loc):
    return (x2loc - x1loc) ** 2 + (y2loc - y1loc) ** 2


def midpoint(x1loc, y1loc, x2loc, y2loc):
    return (x1loc + x2loc) / 2, (y1loc + y2loc) / 2


def slope(x1loc, y1loc, x2loc, y2loc):
    return (y2loc - y1loc), (x2loc - x1loc)


def slope_intercept(yloc, xloc, bloc):
    return -xloc, yloc, bloc / yloc


def square_root(xloc):
    return math.sqrt(xloc)


def divide(xloc, yloc):
    return xloc / yloc


def multiply(xloc, yloc):
    return xloc * yloc


def add(xloc, yloc):
    return xloc + yloc


def subtract(xloc, yloc):
    return xloc - yloc


def sine(opploc, hyploc):
    return opploc / hyploc


def cosine(adjloc, hyploc):
    return adjloc / hyploc


def tangent(opploc, adjloc):
    return opploc / adjloc


print('Enter choice')
print('1. distance, midpoint, and slope         11. cosin(x) degree')
print('2. x ^ y                                 12. tangent(x) degree')
print('3. root x                                13. sin-1(x) opp/hyp')
print('4. slope intercept                       14. cos-1(x) adj/hyp')
print('5. divide, multiply, add, subtract       15. tangent-1(x) opp/adj')
print('6. mean, median, mode')
print('7. sin opp/hyp')
print('8. cosin adj/hyp')
print('9. tangent opp/adj')
print('10. sin(x) degree')

while True:
    choice = input('Enter choice: ')
    if choice in '1, distance, midpoint, slope':
        try:
            x1 = float(input('Enter x1 number: '))
            y1 = float(input('Enter y1 number: '))
            x2 = float(input('Enter x2 number: '))
            y2 = float(input('Enter y2 number: '))
        except ValueError:
            print('invalid choice')
            continue
        if choice == '1':
            print('Distance= ', distance(x1, y1, x2, y2))
        if choice == '1':
            print('Midpoint= ', midpoint(x1, y1, x2, y2))
        if choice == '1':
            print('Slope= ', slope(x1, y1, x2, y2))
    elif choice in '3, root x':
        try:
            x = float(input('Enter number: '))
        except ValueError:
            print('invalid choice')
            continue
        if choice in '3, root x':
            print(square_root(x))

    elif choice in '4, slope intecept':
        try:
            x = float(input('Enter x: '))
            y = float(input('Enter y: '))
            b = float(input('Enter b: '))
        except ValueError:
            print('invalid choice')
            continue
        if choice == '4':
            print(slope_intercept(y, x, b))
    elif choice in '2, x ^ y, divide, multiply, add, subtract, /, *, +, -':
        try:
            x = float(input('Enter first number: '))
            y = float(input('Enter second number: '))
        except ValueError:
            print('invalid choice')
            continue
        if choice == '2':
            print(math.pow(x, y))
        if choice in 'divide, /':
            print(x, '/', y, '= ', divide(x, y))
        if choice in 'multiply, *':
            print(x, '*', y, '= ', multiply(x, y))
        if choice in 'add, +':
            print(x, '+', y, '= ', add(x, y))
        if choice in 'subtract, -':
            print(x, '-', y, '= ', subtract(x, y))
    elif choice == '5':
        choice2 = input('Enter operator: ')
        try:
            x = float(input('Enter number: '))
            y = float(input('Enter number: '))
        except ValueError:
            print('invalid choice')
            continue
        if choice2 == '/':
            print(x, '/', y, '= ', divide(x, y))
        if choice2 == '*':
            print(x, '*', y, '= ', multiply(x, y))
        if choice2 == '+':
            print(x, '+', y, '= ', add(x, y))
        if choice2 == '-':
            print(x, '-', y, '= ', subtract(x, y))

    elif choice in '6, mean, median, mode':
        try:
            list1 = input('Enter numbers: ')
            list2 = list1.split(',')
            list3 = [float(b) for b in list2]
        except ValueError:
            print('invalid choice')
            continue
        if choice == '6':
            print('Mean= ', statistics.mean(list3))
            print('Median= ', statistics.median(list3))
            print('Mode= ', statistics.mode(list3))
        if choice == 'mean':
            print('Mean= ', statistics.mean(list3))
        if choice == 'median':
            print('Median= ', statistics.median(list3))
        if choice == 'mode':
            print('Mode= ', statistics.mode(list3))
    elif choice in '7, sine, sin, 8, cosine, cosin, 9, tangent':
        if choice in '7, sine, sin':
            try:
                opp = float(input('Enter Opposite: '))
                hyp = float(input('Enter Hypotenuse: '))
            except ValueError:
                print('invalid choice')
                continue
            print(sine(opp, hyp))
        if choice in '8, cosine, cosin':
            try:
                adj = float(input('Enter Adjacent: '))
                hyp = float(input('Enter Hypotenuse: '))
            except ValueError:
                print('invalid choice')
                continue
            print(cosine(adj, hyp))
        if choice in '9, tangent, tan':
            try:
                opp = float(input('Enter Opposite: '))
                adj = float(input('Enter Adjacent: '))
            except ValueError:
                print('invalid choice')
                continue
            print(tangent(opp, adj))
    elif choice in '10, sine(x), sin(x)':
        try:
            y = float(input('Enter degree: '))
        except ValueError:
            print('invalid choice')
            continue
        x = (y * math.pi) / 180
        print(math.sin(x))
    elif choice in '11, cosin(x), cosine(x)':
        try:
            y = float(input('Enter degree: '))
        except ValueError:
            print('invalid choice')
            continue
        x = (y * math.pi) / 180
        print(math.cos(x))
    elif choice in '12, tangent(x), tan(x)':
        try:
            y = float(input('Enter degree: '))
        except ValueError:
            print('invalid choice')
            continue
        x = (y * math.pi) / 180
        print(math.tan(x))
    elif choice in '13, sin-1':
        try:
            x = float(input('Enter opp: '))
            y = float(input('Enter hyp: '))
        except ValueError:
            print('invalid choice')
            continue
        z = x / y
        a = math.asin(z)
        print(a * 180 / math.pi)
    elif choice in '14, cos-1':
        try:
            x = float(input('Enter adj: '))
            y = float(input('Enter hyp: '))
        except ValueError:
            print('invalid choice')
            continue
        z = x / y
        a = math.acos(z)
        print(a * 180 / math.pi)
    elif choice in '15, tan-1, tangent-1':
        try:
            x = float(input('Enter opp: '))
            y = float(input('Enter adj: '))
        except ValueError:
            print('invalid choice')
            continue
        z = x / y
        a = math.atan(z)
        print(a * 180 / math.pi)
    else:
        print('invalid choice')
        continue

