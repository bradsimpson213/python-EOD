# The help() function

num1 = 245
word = "Pizza"
letters= ['a', 'b', 'c']

# help()
# help(num1)
# help(num2)
# help(str)
# help(letters)

# Doc strings

# def double(num):
#     """
#     function that takes in a number as an arguement and return 2 times its value
#     """
#     return num * 2


# help(double)

class Book:
    """
    Class definition to create Book objects
    """
    
    def __init__(self, title, series, author):
        """Book Class initializor"""
        self.title = title
        self.series = series
        self.author = authorq


    def get_information(self):
        '''Returns the author and title of the Book instance '''
        return f'{self.title} by {self.author}'


help(Book)


