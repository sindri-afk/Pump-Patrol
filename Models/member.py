from abc import ABC, abstractmethod
class Member(ABC):
    def __init__(self, name, age, email, membership_type):
        self.name = name
        self.age = age
        self.email = email
        self.membership_type = membership_type

