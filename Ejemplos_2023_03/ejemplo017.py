def func1():
    return True

def func2():
    return True

def func3():
    return False

hay_peligro = all([func1(), func2(), func3()])
if not hay_peligro: 
    print("Hay peligro", hay_peligro)