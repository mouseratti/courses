import time
from string import ascii_letters
import random


class Order:
    _created_At = None
    _ID = None

    def __init__(self):
        self._created_At = time.time()
        STRING_LENGTH = 20
        self._ID = "".join(random.choice(ascii_letters) for x in range(STRING_LENGTH))
        print(f"time from init {self._created_At}")
        print(f"ID from init {self._ID}")
        print("this is the init of class Order")

    @property
    def created_at(self):
        print("this is acceptor")
        return self._created_At

    @property
    def ID(self):
        print("this is acceptor")
        return self._ID

    def __gt__(self, other):
        return self.created_at > other.created_at

    def __lt__(self, other):
        return self.created_at < other.created_at

    def __eq__(self, other):
        return self.created_at == other.created_at

if __name__ == '__main__':
    o1 = Order()
    o2 = Order()
    assert o1 > o2
    assert not o1 < o2
    assert not o1 == o2
