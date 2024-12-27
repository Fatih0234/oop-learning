# In this app, we will create a class called ShareBill that will help us calculate how much each person owes for a bill.

class ShareBill:
    def __init__(self, total_amount):
        self.total_amount = total_amount
        self.people = []  # To store people and their days stayed

    def add_person(self, name, days_stayed):
        """Add a person and their days stayed."""
        self.people.append({"name": name, "days_stayed": days_stayed})

    def calculate_shares(self):
        """Calculate how much each person owes."""
        total_days = sum(person["days_stayed"] for person in self.people)
        shares = []
        for person in self.people:
            share = (person["days_stayed"] / total_days) * self.total_amount
            shares.append({"name": person["name"], "share": share})
        return shares

    def display_shares(self):
        """Display each person's share."""
        shares = self.calculate_shares()
        for share in shares:
            print(f"{share['name']} owes {share['share']:.2f}")

# Input Section
total_amount = float(input("Enter the total amount of the bill: "))
total_people = int(input("Enter the number of people: "))

# Create a ShareBill instance
bill = ShareBill(total_amount)

# Add people to the bill
for _ in range(total_people):
    name = input("Enter the name of the person: ")
    days_stayed = int(input(f"Enter the number of days {name} stayed: "))
    bill.add_person(name, days_stayed)

# Display the results
print("\nBill Breakdown:")
bill.display_shares()






























