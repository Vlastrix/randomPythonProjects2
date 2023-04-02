# the class OR blueprint - should have pascal case (each letter capitalized)
# there is PascalCase, camelCase and snake_case
class User:
    # The init function is the constructor
    def __init__(self, user_id, username):
        # these are variables (attributes)
        self.id = user_id
        self.username = username
        # Default value (Doesn't need to be passed when called)
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# We do this to create an object from a blueprint
# object declaration - () to initialize an object from a class
user1 = User("001", "Vlad")
user2 = User("002", "Flavia")

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
