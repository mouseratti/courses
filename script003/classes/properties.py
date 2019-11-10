


class A:
    _my_property = None

    def __init__(self, initial):
        self._my_property = initial

    @property
    def my_property(self):
        print("this is acceptor")
        return self._my_property

    # @my_property.setter
    # def my_property(self, value):
    #     print("this is mutator")
    #     self._my_property = value
    #


if __name__ == '__main__':
    a = A(15)
    print(a.my_property)
    a.my_property = 16
    print(a._my_property)