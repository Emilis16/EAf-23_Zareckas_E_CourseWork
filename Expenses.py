import json


class FinancialTracker:
    def __init__(self):
        self.finances = {}

    def load_data(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.finances = json.load(file)
                self._post_load_hook()
        except FileNotFoundError:
            print("No data file found. Starting with empty data.")

    def save_data(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.finances, file, indent=4)
            self._post_save_hook()

    def add_user(self, name, initial_income):
        if name not in self.finances:
            self.finances[name] = {'initial_income': initial_income, 'transactions': []}
            print('User {} added.'.format(name))
        else:
            print('User {} already exists.'.format(name))

    def expense(self, name, description, amount, category):
        if name in self.finances:
            self.finances[name]['transactions'].append(
                {'description': description, 'amount': amount, 'category': category})
            print('€{} has been spent on {}'.format(amount, category))
        else:
            print("User not found. Please add the user first.")

    def get_expenses(self, name):
        if name in self.finances:
            for expense in self.finances[name]['transactions']:
                print(f"Description: {expense['description']}"
                      f" Amount: {expense['amount']} Category: {expense['category']}")
        else:
            print("User not found.")

    def get_expense_by_category(self, name, category):
        if name in self.finances:
            expenses_in_category = \
                [expense for expense in self.finances[name]['transactions'] if expense['category'] == category]
            return expenses_in_category
        else:
            print("User not found.")
            return []

    def get_total_income(self, name):
        if name in self.finances:
            return self.finances[name]['initial_income']
        else:
            print("User not found.")
            return 0

    def _post_load_hook(self):
        pass

    def _post_save_hook(self):
        pass


class BudgetTracker(FinancialTracker):
    def __init__(self):
        super().__init__()

    def get_budget_summary(self, name):
        if name in self.finances:
            total_income = self.get_total_income(name)
            total_expenses = sum(expense['amount'] for expense in self.finances[name]['transactions'])
            remaining_budget = total_income - total_expenses
            print(f"Total Income: {total_income}")
            print(f"Total Expenses: {total_expenses}")
            print(f"Remaining Budget: {remaining_budget}")
        else:
            print("User not found.")


class LoggingDecorator(FinancialTracker):
    def __init__(self, tracker):
        super().__init__()
        self._tracker = tracker

    def load_data(self, file_path):
        print("Logging: Loading data...")
        self._tracker.load_data(file_path)

    def save_data(self, file_path):
        print("Logging: Saving data...")
        self._tracker.save_data(file_path)

    def add_user(self, name, initial_income):
        return self._tracker.add_user(name, initial_income)

    def expense(self, name, description, amount_spent, category):
        return self._tracker.expense(name, description, amount, category)

    def get_expenses(self, name):
        return self._tracker.get_expenses(name)

    def get_expense_by_category(self, name, category):
        return self._tracker.get_expense_by_category(name, category)

    def get_total_income(self, name):
        return self._tracker.get_total_income(name)

    def get_budget_summary(self, name):
        return self._tracker.get_budget_summary(name)


if __name__ == "__main__":
    tracking = BudgetTracker()
    tracking = LoggingDecorator(tracking)
    data_file = "finances_data.json"
    tracking.load_data(data_file)

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add User")
        print("2. Add Expense")
        print("3. Show All Expenses")
        print("4. Show Expenses by Category")
        print("5. Summary")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter user name: ")
            initial_income = float(input("Enter initial income: "))
            tracking.add_user(name, initial_income)
        elif choice == '2':
            name = input("Enter user name: ")
            description = input("Description: ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            tracking.expense(name, description, amount, category)
        elif choice == '3':
            name = input("Enter user name: ")
            tracking.get_expenses(name)
        elif choice == '4':
            name = input("Enter user name: ")
            category = input("Enter category: ")
            expenses = tracking.get_expense_by_category(name, category)
            if expenses:
                for expense in expenses:
                    print(f"Description: {expense['description']}"
                          f" Amount: {expense['amount']} Category: {expense['category']}")
            else:
                print("No expenses found in this category.")
        elif choice == '5':
            name = input("Enter user name: ")
            tracking.get_budget_summary(name)
        elif choice == '6':
            tracking.save_data(data_file)
            break
        else:
            print("Invalid option. Please choose again.")
