from membership_plans import MembershipPlans
from logo import Logo


class Membership:
    def __init__(self):
        self.title = "Membership Page"
        self.logo = Logo().draw()
    
    def show(self):
        self.logo
        print(self.title)


if __name__ == "__main__":
    membership = Membership()
    membership_plans = MembershipPlans()
    membership.show()
    membership_plans.membership_type()



    
