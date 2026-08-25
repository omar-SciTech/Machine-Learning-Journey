# %matplotlib inline ,this line only works in jupyter notebook to display plots inline.
import matplotlib
import seaborn as sns
sns.set() #this function modifies the default visuals for matplotlib (makes it look better )
matplotlib.rcParams['savefig.dpi'] = 144 # Set the DPI (dots per inch) for saved figures.
                                         #rcParams is a dictionary-like variable that contains the default settings for matplotlib. 
print(3)
print('Hello World')
print("4") 
''''unlike cpp it doesn't matter if you use single or double quotes for strings in python, 
    there is no char data type in python.'''
# 'join' function is often used in python
# It joins items in iterable (list,etc..) with a specified separator
a = ["I", "am", "a string"] #list

print(" ".join(a))
z=6
print(z)
a=None #here a is assigned to None.
print(a) #prints "None".


x = 42
print('%d is an object of %s' % (x, type(x)))   #'%' is used for string formatting in python.
                                                #'%d' is used to format integers, and '%s' is used to format strings.
                                                #and then we use the '%' operator to substitute the values of x and type(x) into the string.
                                                #if we used '%s' it would print the integer as a string.
x = 'Hello world!'
print('%s is an object of %s' % (x, type(x)))

x = {'name': 'Ahmed', 'age': 28}      #this is a dictionary in python, it is a collection of key-value pairs.
print('%s is an object of %s' % (x, type(x)))

#the reason it says "object of <class 'dict'>" is because in python everything is an object,
#in python everything is an instance of a class, thats means that int, str, dict, list, etc.. are all classes in python,
#and when we create an instance of a class we get an object.
#so when i say a = 42, a is an object of the class int.

#An object's methods are its internal functions that implement different capabilities.
x = 'Ahmed'
print(x.lower()) #ahmed
print(x.upper()) #AHMED


# a complex number has real and imaginary parts
x = complex(5, 3)
print(x.real)
print(x.imag)
#here x is a complex number with real part 5 and imaginary part 3, both are floats.
#an example of a complex number is 5 + 3j, where j is the imaginary unit.

#We'll interact with an object's methods more often than its attributes. The attributes represent the _state_ of an object.
#We usually prefer to mutate'نعدل' the state of an object via its methods, 
#since the methods represent the actions one can take safely without breaking the object. 
#Often the attributes of an object will be immutable.
'''
 x = complex(5, 3)
 x.real = 6 
'''
#here we are trying to change the real part of the complex number x,
#but it will raise an error because the real and imaginary parts of a complex number are immutable.


#An example of a method that mutates an object is the `append` method of a `list`:
x = [35, 'example', 348.1]
x.append(True) # Adds True to the end of the list
print(x)

#How do we know what the attributes and methods of an object are? We can use Python's `dir` function. We can use `dir` on an object or on a class.

#to make a float variable we can use the float() function or we can use a decimal point in the number.
x=42.0
print(x/4) #10.5
x = float(42)
print(x) #42.0

class Rational(object): #(object) means we inherit from the class 'object' which the whole python inherits from,
                        #however we dont need to type it in new pythin versions
#the word instance in python is the same as an object in cpp,
#which means a real variable that is made with the class data type for ex: x=rational(3,4)
#in python everything is an object,int,float,str,dic,etc...

    def __init__(self, numerator, denominator): #this is the first method
                                                #'dunder' double underscore b4 and after is usually a built-in, and its prefered not be inhereted but you can
                                                
                                                #to make a constructor and use the function's name in declaring we use'__init__',
                                                #which is a built-in function.
                                                #self is a reference to the current instance of the class,
                                                #and is used by the compiler to access variables that belong to the class, must type it.
                                                #numerator and denominator are the parameters of the constructor,
                                                #they are used to initialize the attributes of the class.
        self.numerator = numerator #this is an attribute (خاصية)that stores the parameter in the instance itself when made
                                   #we use it to access the parameters ,ex:print(x.numerator) x is the name of the instance which is called self here 
        self.denominator = denominator
        

    def __repr__(self): #'__repr__' function determine the display method of the object(instance)
        return '%d/%d' % (self.numerator, self.denominator) #as i said b4 %d formats an integer

    def __mul__(self, number): #the function '__mul__' is a built-in function that is called if i used the '*' operator
        if isinstance(number, int):
            return Rational(self.numerator * number, self.denominator)
        elif isinstance(number, Rational):
            return Rational(self.numerator * number.numerator, self.denominator * number.denominator)
        else:
            raise TypeError('Expected number to be int or Rational. Got %s' % type(number))
    
    def _gcd(self): #one underscore isn't really a rule but it meas don't touch this function from outside of the class
                    #also gcd means greatest common divisor
        smaller = min(self.numerator, self.denominator) #smallest value
        small_divisors = {i for i in range(1, smaller + 1) if smaller % i == 0} #these brackets means this is a set(unique values)
                                                                                #range(1, smaller + 1) returns values from 1(number not index) to smaller includin smaller
                                                                                #for i in range(...)means walk on each i in this range
                                                                                #if smaller % i == 0 is the condition for each i to be stored 
                                                                #so it means make me a set of all divisors of smaller including itself
        larger = max(self.numerator, self.denominator) #largest value
        common_divisors = {i for i in small_divisors if larger % i == 0}#biggest divisor for larger 
        return max(common_divisors)#العامل المشترك

    def reduce(self):
        gcd = self._gcd()#any method in the class is called with'slef', gcd carries the common factor of the current instance
        self.numerator = self.numerator // gcd #بنبسط البسط والمقام
        self.denominator = self.denominator // gcd #'/' returns a float and we want an integer for '%d' so we use '//' which returns an integer
        return self #returns 'self' itself after editing this allows method chaining ex: x =rational(4,8).reduce()


x = Rational(4, 8)
x.reduce()
print(x)  
print(Rational(4, 6) * 3)# i can't do this before declaring what the operator '*' does to the attributes
print(Rational(5, 9) * Rational(2, 3))



# remember, no support for float, can't say:
#print(Rational(4, 6) * 2.3)

# also, no addition, subtraction, etc added.
#print(Rational(4, 6) + Rational(2, 3))

#there is no actual 'private' method that can't be inherited like in cpp, all methods can be inherited

#inheritence
class Rectangle(object):
    def __init__(self, height, length):
        self.height = height
        self.length = length
    
    def area(self):
        return self.height * self.length
    
    def perimeter(self):
        return 2 * (self.height + self.length)

class Square(Rectangle):#inherits from the father 
    def __init__(self, length):
        super(Square, self).__init__(length, length)
        #super= look for the father 
        #square = ill use the methods of the father under the name of square
        #self=this instance of the square
        #i call the function init from the father and give it the values length and length

s = Square(5)
print(s.area(), s.perimeter())
print(type(s))
if type(s) == Square:
    print("yes")
if isinstance(s, Rectangle):#asking if s inherits from crectangle
    print("yes")


grocery_a = 'chicken'
grocery_b = 'onions'
grocery_c = 'rice'
grocery_d = 'peppers'
grocery_e = 'bananas'

grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas']

def buy_groceries_individual(item_a, item_b, item_c, item_d, item_e):
    print('Buying %s...' % item_a)
    print('Buying %s...' % item_b)
    print('Buying %s...' % item_c)
    print('Buying %s...' % item_d)
    print('Buying %s...' % item_e)

def buy_grocery_list(items):
    for item in items:
        print('Buying %s...' % item)


buy_groceries_individual(grocery_a, grocery_b, grocery_c, grocery_d, grocery_e)
buy_grocery_list(grocery_list)#more flexible

# let's try to buy just three items:
#buy_groceries_individual(grocery_a, grocery_b, grocery_c) error cuz i must assign all 5 parameters

# let's try to buy a sixth item:
#grocery_f = 'squash'
#buy_groceries_individual(grocery_a, grocery_b, grocery_c, grocery_d, grocery_e, grocery_f) still an error

short_grocery_list = ['chicken', 'onions', 'rice']
buy_grocery_list(short_grocery_list)

long_grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas', 'squash']

buy_grocery_list(long_grocery_list)

#we wan make a variable list:grocery_a = 'chicken'
grocery_b = 'onions'
grocery_c = 'rice'
grocery_d = 'peppers'
grocery_e = 'bananas'

grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas']
print(grocery_list)

grocery_list = [grocery_a, grocery_b, grocery_c, grocery_d, grocery_e]
print(grocery_list)


int_list = [2, 6, 3049, 18, 37]
float_list = [3.7, 8.2, 178.245, 63.1]
mixed_list = [26, False, 'some words', 1.264]

print(int_list)
print(float_list)
print(mixed_list)

list_of_lists = [['a', 'list', 'of', 'words'], [1, 5, 209], [True, True, False]]
print(list_of_lists)
print (list_of_lists[0])


confusing_list = [[23, 73, 50], 'some words', 12.308, [[False, True], 'more words']]
print(confusing_list)
print(confusing_list[0][0])# first element of the first list

print(grocery_list[1:4])#from i=1 to i=3
print(grocery_list[3:])#from i=3 to end
print(grocery_list[:3])#from i=0 to i=2

print(grocery_list[-1])#acces the list from the end, this will print the last elment.
print(grocery_list[-3:])#from the third element from the end to the end

print(grocery_list[::2]) #start:end:step
print(grocery_list[4:1:-1]) #['bananas', 'peppers', 'rice'] , counts from 1(end) to 3 from the end.
#so when counting from front its 0 based index and from the end its 1 based index with negative values.

for item in grocery_list:
    print(item)

for i in range(0, len(grocery_list), 2):
    print(i, grocery_list[i])

'''
print(range(0, 10, 3))
print(range(104, 100, -1))
print(range(5)) # starts at 0 and counts by 1 by default
'''

grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas']
print(grocery_list)
grocery_list[-1] = 'oranges' # replace bananas with oranges
print(grocery_list)
grocery_list[1:3] = ['carrots', 'couscous'] #replace onions and rice with carrots and couscous
print(grocery_list)


grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas']
print(grocery_list)
grocery_list.append('squash')#if i add [] here it'll print it
print(grocery_list)
grocery_list.append(['bread', 'salt'])# imust use [] when adding more than 1 item
print(grocery_list) # ['chicken', 'onions', 'rice', 'peppers', 'bananas', 'squash', ['bread', 'salt']]

#Since lists can contain lists, we have to be careful about adding multiple items to our list. Instead of `append`, we might want to use `extend`.
grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas', 'squash']
print(grocery_list)
grocery_list.extend(['bread', 'salt'])
print(grocery_list)#['chicken', 'onions', 'rice', 'peppers', 'bananas', 'squash', 'bread', 'salt']
#i must always use brackets with extend even if it's only 1 item
grocery_list.extend('salt')# this prints : ['chicken', 'onions', 'rice', 'peppers', 'bananas', 'squash', 's', 'a', 'l', 't']

print(grocery_list)
del grocery_list[-1] # delete the last item
print(grocery_list)

print(grocery_list)
print(grocery_list.pop(-1)) # remove the last item from the list and return it
print(grocery_list)#after remove

grocery_list.sort()
print(grocery_list)#sorts by the smallest binary value of a character, or the smallest integer

a = 4
b = a
print(a, b)
a = 5
print(a, b)

'''output:4 4
          5 4'''
a = [3, 2, 1]
b = a #they both carry the reference of the list
print(a, b)
a[1] = 5
print(a, b)


'''output:[3, 2, 1] [3, 2, 1]
          [3, 5, 1] [3, 5, 1]'''


#A Python `tuple` is very similar to a `list` with one major difference -- it is immutable. We create a `tuple` using parentheses `()`.
example_tuple = ('Ahmed', 26, 167.6, True)
print(example_tuple)
print(example_tuple[2])
#While we can retrieve data through indexing (because a `tuple` is ordered), we cannot modify it (because a `tuple` is immutable).

'''error:
example_tuple[2] = 169.3
del example_tuple[-1]'''

#While for clarity we should enclose tuples with `()`, 
#Python will assume we want a `tuple` if we don't use any symbols to enclose comma separated values.
another_example_tuple = 'Jana', 36, 162.3, True
print(another_example_tuple)
print(type(another_example_tuple))