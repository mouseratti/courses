

class A():
    _field1 = 1
    def my_method(self):
        print(self)
        print(self.field1)
        pass

    def my_method2(self, *args, **kwargs):
        print(self, args, kwargs)
        self.my_method()
        pass

    def __add__(self, other):
        return self.field1 + other.field1

    def _private(self):
        print("this is private")


# a = A()
# a.my_method()