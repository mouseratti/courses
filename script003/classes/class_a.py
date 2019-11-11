

class A:
    property_a = 1

    def method_a(self):
        print("this is the method from A")

    def __init__(self, property_a):
        print("this is the init of class A")
        self.property_a = property_a




class B():
    property_b = ""
    def __repr__(self):
        return f"!! my representation: {self.property_b}"

    def method_b(self):
        print("this is the method from B")



    def __init__(self, b):
        print("this is the init of class B")
        self.property_b = b




class C(B,A):
    property_c = []

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.property_c = []

    def method_c(self):
        print("method of C")

    # def __add__(self, other):
    #     self.property_c += other.property_c
    #     return self

if __name__ == '__main__':
    c1 = C("string")
    c1.property_c.append(1)
    c2 = C("222")
    c2.property_c.append(4)
    print(C.property_c, c1.property_c, c2.property_c)
    print(C.__dict__, c1.__dict__, c2.__dict__)
    print(C.__bases__)

    def runtime_method(self, arg1="non-empty string"):
        print(self)
        print(arg1)
        return

    C.runtime_method = runtime_method
    c1.runtime_method()
    c2.instance_method = runtime_method
    c2.instance_method(c2)
    # c1_runtime_method = c1.runtime_method
    # c1_runtime_method()