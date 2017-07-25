from users import User


# New Instance of User
user = User(name="Duke", age=17, weight=200.5, eye_color="Brown")
print user.name, user.age, user.weight, user.eye_color
user.message(content="Hello World!")