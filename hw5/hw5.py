import sys
import inspect
from math import sqrt, cos, sin
def your_name():
    return 'Chase Carroll'
def a_plus_bx(a,b,x):
    a = int(a)
    b = int(b)
    x = int(x)
    return a+b*x
def hypotenuse(a,b):
    a = int(a)
    b = int(b)
    res = sqrt((a*a)+(b*b))
    return res
def polar_to_rect(radius,theta):
    radius = int(radius)
    theta = int(theta)
    list = [radius*cos(theta),radius*sin(theta)]
    return list
def dot_product(a,b):
    a = a.replace("(","")
    a = a.replace(")","")
    b = b.replace("(","")
    b = b.replace(")","")
    alst = a.split(",")
    blst = b.split(",")
    lsta = [int(x) for x in alst]
    lstb = [int(x) for x in blst]
    sum = 0
    for i in range(0,len(lsta)):
        sum += lsta[i]*lstb[i]
    return sum
def threshold(min,lst):
    min = int(min)
    lst = lst.replace("(","")
    lst = lst.replace(")","")
    lst = lst.split(",")
    lst2 = [int(i) for i in lst]
    res = [value for value in lst2 if value >= min]
    return res
def diff(z,lst):
    z = int(z)
    lst = lst.replace("(","")
    lst = lst.replace(")","")
    lst = lst.split(",")
    lsta = [int(x) for x in lst]
    res = [abs(value-z) for value in lsta]
    return res
blis = []
def build_list(start,end):
    start = int(start)
    end = int(end)
    if end <= start:
        return
    else:
        blis.append(start)
        build_list(start+1,end)
    return blis
def convert(command,arg):
    if command == "upper":
        return arg.upper()
    elif command == "lower":
        return arg.lower()
    elif command == "reverse":
        if "(" and ")" in arg:
            arg = arg.replace("(","")
            arg = arg.replace(")","")
            arg = arg.split(",")
            arg.reverse()
            return arg
        elif type(arg) == str:
            return arg[::-1]
        else:
            return 'Unsupported argument type.'
    elif command == "square":
        arg = int(arg)
        return arg*arg
    else:
        return 'not-implemented'
def strip_spaces(string):
    return string.replace(" ","")
def get_cogs():
    all_funcs = inspect.getmembers(sys.modules[__name__],inspect.isfunction)
    func_names = [name for name,value in all_funcs]
    func_names.remove('main')
    func_names.remove('get_cogs')
    return func_names
def main():
    # print("Total arguments passed: {}\n".format(len(sys.argv)-1))
    # for i in range(1,len(sys.argv)):
    #     print(sys.argv[i])
    cogs = get_cogs()
    if sys.argv[1] == 'info':
        print("\nAvailable functions. Refer to doc.txt for argument entry information.\n--------------------------")
        for name in cogs:
            print(name)
        print("--------------------------\n")
    elif sys.argv[1] in cogs:
        if len(sys.argv) == 2:
            print(getattr(sys.modules[__name__],sys.argv[1])())
        elif len(sys.argv) > 2:
            args = []
            for i in range(2,len(sys.argv)):
                args.append(sys.argv[i])
            print(getattr(sys.modules[__name__],sys.argv[1])(*args))
    else:
        print('Unrecognized function.')
main()
