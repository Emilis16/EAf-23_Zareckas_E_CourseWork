import unittest
import os
import Expenses


class TestFinancialTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = Expenses.FinancialTracker()
        self.data_file = "test_finances_data.json"

    def test_add_user(self):
        self.tracker.add_user("Alice", 2000)
        self.assertIn("Alice", self.tracker.finances)
        self.assertEqual(self.tracker.finances["Alice"]["initial_income"], 2000)

    def test_expense(self):
        self.tracker.add_user("Bob", 2500)
        self.tracker.expense("Bob", "Groceries", 100, "Food")
        self.assertEqual(len(self.tracker.finances["Bob"]["transactions"]), 1)

    def test_get_expense_by_category(self):
        self.tracker.add_user("Charlie", 3000)
        self.tracker.expense("Charlie", "Rent", 1000, "Housing")
        self.tracker.expense("Charlie", "Groceries", 200, "Food")
        expenses = self.tracker.get_expense_by_category("Charlie", "Food")
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]["description"], "Groceries")

    def test_get_total_income(self):
        self.tracker.add_user("Dave", 4000)
        income = self.tracker.get_total_income("Dave")
        self.assertEqual(income, 4000)

    def tearDown(self):
        if os.path.exists(self.data_file):
            os.remove(self.data_file)


class TestBudgetTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = Expenses.BudgetTracker()
        self.data_file = "test_finances_data.json"

    def test_get_budget_summary(self):
        self.tracker.add_user("Eve", 5000)
        self.tracker.expense("Eve", "Rent", 1500, "Housing")
        self.tracker.expense("Eve", "Groceries", 300, "Food")
        self.tracker.expense("Eve", "Entertainment", 200, "Fun")
        expected_income = 5000
        expected_expenses = 1500 + 300 + 200
        expected_remaining_budget = expected_income - expected_expenses
        self.tracker.get_budget_summary("Eve")
        self.assertEqual(self.tracker.get_total_income("Eve"), expected_income)
        self.assertEqual(expected_expenses, sum(expense["amount"]
                                                for expense in self.tracker.finances["Eve"]["transactions"]))
        self.assertEqual(expected_remaining_budget, expected_income - expected_expenses)

    def tearDown(self):
        if os.path.exists(self.data_file):
            os.remove(self.data_file)


if __name__ == '__main__':
    unittest.main()
