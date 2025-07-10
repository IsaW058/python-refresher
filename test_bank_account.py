import unittest
import bank_account


class Test_Bankaccount(unittest.TestCase):
    def setUp(self):
        self.account = bank_account.Bankaccount("oompa loompa", 20, "123356")

    def test_withdraw(self):
        amount = 908.2
        self.assertTrue(isinstance(amount, (float, int)))
        amount = "hi"
        self.assertFalse(isinstance(amount, (float, int)))
        amount = 10
        self.assertFalse(isinstance(amount, (str)))

        self.assertTrue(self.account.withdraw(amount))
        self.assertEqual(self.account.balance, 10)

        self.assertTrue(self.account.withdraw(7))
        self.assertNotEqual(self.account.balance, 5)
        self.assertEqual(self.account.balance, (3))

    def test_withdraw_insufficient_funds(self):
        self.assertFalse(self.account.withdraw(340))
        self.assertTrue(self.account.withdraw(3))
        self.assertEqual(self.account.balance, 17)

    def test_withdraw_neg_amount(self):
        self.assertFalse(self.account.withdraw(-10))
        self.assertEqual(self.account.balance, 20)

    def test_deposit(self):
        self.assertTrue(self.account.deposit(10))
        self.assertEqual(self.account.balance, 30)
        self.assertTrue(self.account.deposit(20000))
        self.assertNotEqual(self.account.balance, 31.5)

    def test_deposit_neg_amount(self):
        self.assertFalse(self.account.deposit(-987.678))
        self.assertEqual(self.account.balance, 20)
