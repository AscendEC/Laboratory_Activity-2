class BudgetCategory:

    # Represents a single budget category with a name, spending limit, and current expenses.

    def __init__(self, name: str, limit: float):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Category name must be a non-empty string.")
        if not isinstance(limit, (int, float)) or limit <= 0:
            raise ValueError("Budget limit must be a positive number.")
        
        self.name = name.strip()
        self.limit = float(limit)
        self.expenses = 0.0
        self.transactions = []  # list of (description, amount)

    def add_expense(self, amount: float, description: str = "Unnamed expense") -> None:
        # Add an expense to this category.

        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Expense amount must be a positive number.")
        
        self.expenses += amount
        self.transactions.append((description.strip(), amount))
        print(f"Added ₱{amount:.2f} for '{description}' to '{self.name}'")

    def remaining(self) -> float:
        # Returns how much budget is left (can be negative).
        return self.limit - self.expenses

    def status(self) -> str:
        # Returns a human-readable status message.
        remaining = self.remaining()
        percent_used = (self.expenses / self.limit) * 100 if self.limit > 0 else 0
        
        if remaining > 0:
            if percent_used >= 80:
                return f"{self.name}: ₱{remaining:.2f} left ({percent_used:.1f}% used) — getting close!"
            return f"✓  {self.name}: ₱{remaining:.2f} left ({percent_used:.1f}% used)"
        elif remaining == 0:
            return f"✗  {self.name}: Exactly at limit (100%)"
        else:
            return f"!!! {self.name}: OVER BUDGET by ₱{abs(remaining):.2f} ({percent_used:.1f}%)"

    def __str__(self) -> str:
        return f"{self.name} (Limit: ₱{self.limit:.2f}) — Spent: ₱{self.expenses:.2f}"


def main():
    print(" Simple Budget Tracker \n")
    categories = {}

    while True:
        print("\nOptions:")
        print("  1. Create new category")
        print("  2. Add expense")
        print("  3. Show status of all categories")
        print("  4. Exit")

        try:
            choice = input("Enter choice (1–4): ").strip()

            if choice == "1":
                name = input("Category name: ").strip()
                limit_input = input("Monthly limit (₱): ").strip()
                
                try:
                    limit = float(limit_input)
                except ValueError:
                    print("Error: Please enter a valid number for the limit.")
                    continue

                try:
                    cat = BudgetCategory(name, limit)
                    categories[name.lower()] = cat  # case-insensitive key
                    print(f"Created category: {cat}")
                except ValueError as e:
                    print(f"Error: {e}")
                    continue

            elif choice == "2":
                if not categories:
                    print("No categories yet. Create one first.")
                    continue

                name = input("Which category? ").strip()
                key = name.lower()
                if key not in categories:
                    print("Category not found.")
                    continue

                amount_input = input("Expense amount (₱): ").strip()
                desc = input("Description (optional): ").strip() or "Unnamed expense"

                try:
                    amount = float(amount_input)
                except ValueError:
                    print("Error: Invalid amount. Must be a number.")
                    continue

                try:
                    categories[key].add_expense(amount, desc)
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == "3":
                if not categories:
                    print("No categories created yet.")
                else:
                    print("\nCurrent budget status:")
                    for cat in categories.values():
                        print(cat.status())

            elif choice == "4":
                print("\nGoodbye! Stay within budget!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()