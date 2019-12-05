
try:
    num1 = input('Enter Values:')
    num2 = input('Enter values')
    num3 = num1/num2
except:
    pass




class InvalidNumbers(BaseException):
    def __init__(self,msg):
        super().__init__(msg)

try:
    print('inside try block')
    num1 = int(input('Enter Number 1 :'))
    num2 = int(input('Enter Number 2 : '))
    print('try completed..')
except ValueError as e:
    print('inside except block')
    raise InvalidNumbers("Invalid numbers..")
    print('Excepted digits only..!')
else:
    print('inside else block')
    result = num1 * num2
    print("Result is  : ",result)
finally:
    print('inside finally block')


import sys
sys.exit(0)
def function1():
    print('inside function 1')
    #except TypeError:
    #    print('Invalid Input..excepted digits only')
    #else:
     #   print('Function 1 completed ', result)

    print('Function 1 completed ',result)


def funtion2():
    print('inside function 2')
    try:
        function1()
    except :
        print('Excepted values are digits only..!')

    print('Function 2 completed ')

def function3():
    print('inside function 3')
    funtion2()
    print('Function 3 completed ')

if __name__ == '__main__':
    pass