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
- Abstraction: The "FinancialTracker" class provides an abstraction for managing finances through methods like add_user, hiding the implementation details of how user data is stored and managed.
- Inheritance: "BudgetTracker" inherits from "FinancialTracker", acquiring its attributes and methods. This allows BudgetTracker to reuse functionality defined in FinancialTracker.
- Encapsulation: Data like "finances" is encapsulated within the "FinancialTracker" class, and access to it is controlled through methods like add_user, ensuring that the data remains consistent and protected from external manipulation.

Design patterns:
Decorator:
            \class LoggingDecorator(FinancialTracker):
            \def __init__(self, tracker):
              \super().__init__()
              \self._tracker = tracker


