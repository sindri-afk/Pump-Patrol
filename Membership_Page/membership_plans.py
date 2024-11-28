from logo import Logo

class MembershipPlans:
    def __init__(self):
        self.Logo = Logo()

    def membership_type(self):
        print("Options: Go to Go, Short Term, Long Term\n")
        choice = input("Enter the type of membership you want to purchase(1, 2, 3): \n")
        if choice == "1":
            self.go_to_go()
        elif choice == "2":
            self.short_term()
        elif choice == "3":
            self.long_term()
        else:
            print("Invalid choice. Please try again.\n\n")
            self.membership_type()
    
    def go_to_go(self):
        print("Go to Go Membership Plans")
        print("Options: 1 time, 5 times, 10 times")
        print("Price:   $1.50,   $6.50     $13")   

        choice = input("Enter your choice(1, 2, 3): \n")
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        else:
            print("Invalid choice. Please try again.\n\n")
            self.go_to_go()

    def long_term(self):
        print("Long Term Membership Plans")
        print("Options: 1 year, 2 years, 5 years")
        print("Price:   $100,   $180     $300")
        choice = input("Enter your choice(1, 2, 3): ")
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        else:
            print("Invalid choice. Please try again.\n\n")
            self.long_term()

    def short_term(self):
        print("Short Term Membership Plans")
        print("Options: 1 month, 3 months, 6 months")
        print("Price:   $10,   $25     $45")
        choice = input("Enter your choice(1, 2, 3): \n")
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        else:
            print("Invalid choice. Please try again.\n\n")
            self.short_term()

if __name__ == "__main__":
    member = MembershipPlans()
    member.membership_type()

