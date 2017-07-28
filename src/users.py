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

    def message(self, content):
        """
        :Description: Will print the message quoted by the user.
        :param content: Message to spit out.
        :type content: basestring
        """
        print self.name + " says \"%s\"" % content

    def birthday(self):
        """
        :Description: Increment the users age by 1.
        """
        print 'Happy Birthday!'
        self.age = self.age + 1
        print birthday(self)