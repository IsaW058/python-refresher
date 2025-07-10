import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertNotEqual(hello.hello(), "bye, world!")
        self.assertNotEqual(hello.hello(), "oompa loompa")

    def test_add(self):
        self.assertEqual(hello.add(1, 2), 3)
        self.assertEqual(hello.add(-1, 5), 4)
        self.assertNotEqual(hello.add(-10, 5), 90)

    def test_sub(self):
        self.assertEqual(hello.sub(900, 2), 898)
        self.assertEqual(hello.sub(0, 0), 0)
        self.assertNotEqual(hello.sub(2000, 5), 200)

    def test_mul(self):
        self.assertEqual(hello.mul(-3, -4), 12)
        self.assertNotEqual(hello.mul(-1, 9), -5)
        self.assertNotEqual(hello.mul(2, 3), 7)

    def test_div(self):
        self.assertEqual(hello.div(6, 2), 3)
        self.assertEqual(hello.div(-10, 2), -5)
        self.assertNotEqual(hello.div(10, 2), 6)
        







    


    # def test_sin(self):
    #     self.assertEqual(hello.sin(0), 0)
    #     self.assertEqual(hello.sin(1), 0.8414709848078965)

    # def test_cos(self):
    #     self.assertEqual(hello.cos(0), 1)
    #     self.assertEqual(hello.cos(1), 0.5403023058681398)

    # def test_tan(self):
    #     self.assertEqual(hello.tan(0), 0)
    #     self.assertEqual(hello.tan(1), 1.5574077246549023)

    # def test_cot(self):
    #     self.assertEqual(hello.cot(0), float("inf"))
    #     self.assertEqual(hello.cot(1), 0.6420926159343306)


if __name__ == "__main__":
    unittest.main()
