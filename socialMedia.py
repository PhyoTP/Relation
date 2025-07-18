from relation import Relator 

class Person(Relator):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def __add__(self, other):
        super().__add__(other)
        if self in other.children:
            self*=other
        
class Group(Relator):
    def __init__(self, name, desc):
        super().__init__(name)
        self.desc = desc

user = Person("Tim", 17)
friend = Person("Min", 23)
groupmate = Person("Maddie", 16)
coding_club = Group("High School Coding Club", "a club for coding")

# Adding relationships
user + friend

# Printing children's names
print("User's followers:", user.children_names())

# Adding user as a child to friend
friend + user

# Printing relations' names
print("User's friends:", user.relations_names())
print("Friend's friends:", friend.relations_names())

# Printing counts
print("User's follower count:", len(user.children))
print("User's friends count:", len(user.relations))

# Adding user and groupmate to the coding club
coding_club + user
coding_club + groupmate

# Printing children names of the coding club
print("Coding Club's members:", coding_club.children_names())
print("Coding Club's member count:", len(coding_club.children))


