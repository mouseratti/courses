from unittest import TestCase
from .myfile import odd_generator

class TestOdd_generator(TestCase):
    generator = None

    def setUp(self):
        self.generator = odd_generator()
        print("setup")

    def tearDown(self):
        print("cleanup")

    def test_odd_generator(self):
        self.fail()

    def test_always_pass(self):
        self.assertTrue(True)

    def test_check_exception(self):
        with self.assertRaises(StopIteration):
            raise StopIteration
