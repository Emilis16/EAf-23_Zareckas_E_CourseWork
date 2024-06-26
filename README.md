# Expense Tracker
# By Emilis Zareckas EAf-23
## Description
A program that tracks all your expenses, categorizes them, and displays the expenses.

## Program features
- Entering expenses for different users
- Displaying all expenses 
- Displaying Expenses by Category
- Setting an initial income
- Reading and saving data to JSON file

## Program requirements
- Python 3.x

## Program guide
- To begin, select option "1" and enter your name along with your initial income.
- Add an expense by selecting option "2". Enter the expense details: name, description, amount, and category.
- To see all expenses, select option "3" and enter your name.
- Additionally, the program allows you to view expenses by category by selecting option "4".
- Finally, the summary function enables you to see your total income, total expenses, and remaining budget.

## Code analysis
My program use 4 object-oriented programming pillars:
- Polymorphism: Class "BudgetTracker" is inheriting from Class "FinancialTracker', allowing instances of BudgetTracker to be treated as instances of FinancialTracker.

            class BudgetTracker(FinancialTracker):
                def __init__(self):
                    super().__init__()

            #########################################

            class LoggingDecorator(FinancialTracker):
                def __init__(self, tracker):
                    super().__init__()
                    self._tracker = tracker

                def load_data(self, file_path):
                    print("Logging: Loading data...")
                    self._tracker.load_data(file_path)

- Abstraction: The "FinancialTracker" class provides an abstraction for managing finances through methods like add_user, hiding the implementation details of how user data is stored and managed.

            class FinancialTracker:
                def __init__(self):
                    self.finances = {}

                def add_user(self, name, initial_income):
                    if name not in self.finances:
                        self.finances[name] = {'initial_income': initial_income, 'transactions': []}
                        print('User {} added.'.format(name))
                    else:
                        print('User {} already exists.'.format(name))
- Inheritance: "BudgetTracker" inherits from "FinancialTracker", acquiring its attributes and methods. This allows BudgetTracker to reuse functionality defined in FinancialTracker.

            class BudgetTracker(FinancialTracker):
                def __init__(self):
                    super().__init__()
- Encapsulation: Data like "finances" is encapsulated within the "FinancialTracker" class, and access to it is controlled through methods like add_user, ensuring that the data remains consistent and protected from external manipulation.

            class FinancialTracker:
                def __init__(self):
                    self.finances = {}

                def add_user(self, name, initial_income):
                    if name not in self.finances:
                        self.finances[name] = {'initial_income': initial_income, 'transactions': []}
                        print('User {} added.'.format(name))
                    else:
                        print('User {} already exists.'.format(name))

Design patterns:
- Decorator:

            class LoggingDecorator(FinancialTracker):
                def __init__(self, tracker):
                    super().__init__()
                    self._tracker = tracker
The "LoggingDecorator" class decorates instances of "FinancialTracker", enhancing their behavior by adding logging functionality to methods like "load_data", "save_data", etc. This is achieved by composing an instance of "FinancialTracker" within "LoggingDecorator" and delegating method calls to it.

Unittest:
- Test adding a user:

            self.tracker.add_user("Alice", 2000)
            self.assertIn("Alice", self.tracker.finances)
            self.assertEqual(self.tracker.finances["Alice"]["initial_income"], 2000)

- Test adding an expense:

            self.tracker.add_user("Bob", 2500)
            self.tracker.expense("Bob", "Groceries", 100, "Food")
            self.assertEqual(len(self.tracker.finances["Bob"]["transactions"]), 1)

- Test getting expenses by category:

            self.tracker.add_user("Charlie", 3000)
            self.tracker.expense("Charlie", "Rent", 1000, "Housing")
            self.tracker.expense("Charlie", "Groceries", 200, "Food")
            expenses = self.tracker.get_expense_by_category("Charlie", "Food")
            self.assertEqual(len(expenses), 1)
            self.assertEqual(expenses[0]["description"], "Groceries")

- Test getting total income:

            self.tracker.add_user("Dave", 4000)
            income = self.tracker.get_total_income("Dave")
            self.assertEqual(income, 4000)

- Clean up data file:

            if os.path.exists(self.data_file):
            os.remove(self.data_file)

- Test getting budget summary:

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

- Clean up data file:

            if os.path.exists(self.data_file):
                        os.remove(self.data_file)

## Results
What I successfully implemented:
- Writing and reading from JSON file.
- Used all 4 object-oriented programming pillars.
- Code unittest.

What I didn't implement:
- I used only one design pattern instead of two.

## Conclusion
- My program is a great simple tool to track expenses. It can do basic functions such as adding expenses, showing all or categorised expenses, and remaining budget, for multiple users. However, there are a few improvements that could be made, such as error handling for invalid input and better separation of concerns between the decorator and the tracked object. Additionally, logging could be enhanced to provide more detailed information about the operations being performed.
