from users import User


# New Instance of User
user = User(name="Duke", age=17, weight=200.5, eye_color="Brown")
print user.name, user.age, user.weight, user.eye_color
print 'User\'s current age: %s' % (user.age)
user.birthday()
print 'Current name: %s' % user.name
user.name_change(name="Danny")
print 'New name: %s' % user.name
user.message(content="Hello World!")