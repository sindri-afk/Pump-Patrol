from logo import Logo
# from Membership_Page.application import Membership
import sys

class MainPage:
    def __init__(self):
        self.logo = Logo().draw()
        self.title = "Main Page"

    def show(self):
        self.logo
        print(self.title)
    def choice(self):
        print("1. Membership")
        print("2. Membership Plans")
        print("3. Exit")
        choice = input("Enter choice(1, 2, 3): ")
        if choice == "3":
            print("\nThank you for using the system\n")
            sys.exit()
        else: 
            return choice


if __name__ =="__main__":
    main_page = MainPage()
    main_page.show()
    main_page.choice()
    # if main_page.choice() == "1":
    #     membership = Membership()
    #     membership.show()   

