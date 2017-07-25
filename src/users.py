class User(object):
    """
    :Description: Definition for users.
    :param name: Name of the user.
    :type name: basestring
    :param age: Age of the user.
    :type age: int
    :param weight: Weight of the user.
    :type weight: float
    :param eye_color: User's eye color.
    :type eye_color: basestring
    """
    def __init__(self, name, age, weight, eye_color):
        self.name = name
        self.age = age
        self.weight = weight
        self.eye_color = eye_color

user = User(name="Duke", age=17, weight=200.5, eye_color="Brown")
print user.name, user.age, user.weight, user.eye_color

def message(self, content):
        """
        :Description: Will print the message quoted by the user.
        :param content: Message to spit out.
        :type content: basestring
        """
        print self.name + " says \"%s\"" % content

def birthday(self, age, birthday):
 """
 :Description: Increment the users age by 1.
 """
 self.age = age
 self.birthday = birthday(age + 1)
user = User(age=17 + 1, name="Duke", weight=200.5, eye_color="Brown")
print'Happy Birthday!'