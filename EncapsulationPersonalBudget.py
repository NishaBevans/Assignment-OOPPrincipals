#Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget. 
# - Initialize these attributes in the constructor.

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name  # Private attribute for category name
        self.__allocated_budget = allocated_budget  # Private attribute for allocated budget
        self.__remaining_budget = allocated_budget  # Private attribute for remaining budget
#Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. - 
# Ensure that the setter methods include validation (e.g., budget should be a positive number).
    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    def set_allocated_budget(self, new_budget):
        if new_budget < 0:
            print("Budget cannot be negative.")
        else:
            self.__allocated_budget = new_budget
            self.__remaining_budget = new_budget  # Reset remaining budget when allocated budget changes

    # Getter for remaining budget
    def get_remaining_budget(self):
        return self.__remaining_budget
#Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust the budget accordingly. - 
# Validate the expense amount before making deductions from the budget.
    # Method to add an expense to the category
    def add_expense(self, amount):
        if amount < 0:
            print("Expense cannot be negative.")
        elif amount > self.__remaining_budget:
            print("Expense exceeds remaining budget.")
        else:
            self.__remaining_budget -= amount
            print(f"Added expense of ${amount:.2f}. Remaining budget: ${self.__remaining_budget:.2f}")
#Task 4: Display Budget Details Create a method to display the details of a budget category, including the name, 
# allocated budget, and remaining budget after expenses.
    # Method to display the budget category details
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}")

# Example usage
if __name__ == "__main__":
    food_category = BudgetCategory("Food", 500)
    food_category.display_category_summary()

    food_category.add_expense(100)
    food_category.display_category_summary()

    food_category.add_expense(450)  # This should fail
    food_category.add_expense(-50)   # This should fail
    food_category.display_category_summary()
