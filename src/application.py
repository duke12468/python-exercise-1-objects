from users import User


# New Instance of User
user = User(name="Duke", age=17, weight=200.5, eye_color="Brown")
print user.name, user.age, user.weight, user.eye_color
print 'User\'s current age: %s' % (user.age)
user.birthday(age=18)
print 'User\'s age after birthday: %s' % str(user.age)
user.message(content="Hello World!")