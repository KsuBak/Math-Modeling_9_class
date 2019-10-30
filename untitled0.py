def massive_func(Ma):
    """ функцию, которая перемножает все элементы входного массива, подающегося на входвкачествеаргумента"""
    a=1
    for i in range (1,len(Ma),1):
        a=a*Ma[i]
        print(a)
    print('---------------')
    return a


x = [1, 2, 3, 4]
print(massive_func(x))