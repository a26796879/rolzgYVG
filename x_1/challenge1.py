class Phone:
    def __init__(self,price,camera_count,screen_size):
        self.price = 0
        self.camera_count = 0
        self.screen_size = 0

class Google_phone(Phone):

    def __init__(self,price,camera_count,screen_size):
        self.price = 10
        self.camera_count = 3
        self.screen_size = 5

    def special_freature(self):
        userinput = eval(input('Google_phone.special_freature input a list: '))
        num = 1
        for i in list(userinput):
            num *= i
        print(num)

class Taiwan_phone(Phone):

    def __init__(self, price, camera_count, screen_size):
        self.price = 20
        self.camera_count = 1
        self.screen_size = 3

    def special_freature(self):
        userinput = int(input('Taiwan_phone.special_freature input a number: '))

        def fib(n):
            if n <= 2:
                return 1
            else:
                return fib(n-1)+fib(n-2)
        print(fib(userinput))


class Apple_phone(Phone):

    def __init__(self, price, camera_count, screen_size):
        self.price = 30
        self.camera_count = 2
        self.screen_size = 10

    def special_freature(self):
        import ast
        userinput = ast.literal_eval(
            input('Apple_phone.special_freature input 2 numbers: '))
        inputs = []
        for a in range(userinput[0]-userinput[1]+1, userinput[0]+1):
            inputs.append(a)
        num = 1
        for i in inputs:
            num *= i
        print(num)


Google_phone(10,3,5).special_freature()
Taiwan_phone(20,1,3).special_freature()
Apple_phone(30,2,10).special_freature()
