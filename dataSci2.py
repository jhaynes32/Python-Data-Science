from collections import defaultdict
from collections import Counter
import random
import re


# Function - rule for taking zero or more inputes and returning a corresponding output.

def double(x):

    return x * 2

def apply_to_one(f):

    return f(1)

my_double = double 

x = apply_to_one(my_double)

y = apply_to_one(lambda x: x + 4)

def another_double(x):

    return 2 * x

# default parameters
def my_print(message = "my default message"):

    print(message)

my_print("hello")
my_print()


# specify arguments by name
def full_name(first = "What's-his-name", last = "Something"):
    return first + " " + last

print(full_name("Joel", "Grus"))
print(full_name("Jeremiah"))




                        # Strings
tab_string = "\t"
print(len(tab_string)) # = 1

not_tab_string = r"\t"
print(len(not_tab_string))


# f-strings allow for substitute values in strings
first_name = "Joel"
last_name = "Grus"

full_name1 = first_name + " " + last_name
full_name2 = "{0}{1}".format(first_name, last_name)
full_name3 = f"{first_name} {last_name}"



                        # Lists
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x[0] = -1

every_third = x[::3] # -1, 3, 6, 9
five_to_three = x[5:2:-1] # [5, 4, 3]

1 in [1, 2, 3] # True

x = [1, 2, 3]
x.extend([4, 5, 6]) # x is now [1, 2, 3, 4, 5, 6]
y = x + [4, 5, 6]

x, y = [1, 2]


                        # Tuples

# return multiple values from functions with tuples
def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2, 3)

x, y = 1, 2
x, y = y, x  # Pythonic swap



                        # Dictionaries (Objects) dict

empty_dict = {}

grades = {"Joel": 80, "Tim": 95} 
joels_grade = grades.get("Joel", 0) # 80

tweet = { 
    "user" : "jeremiah",
    "text" : "Data Science is cool",
    "retweet_count" : 100,
    "hashtags" : ["#data", "science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()


"user" in tweet_keys
"Jeremiah" in tweet_values



                        # defaultdict

dd_dict = defaultdict(dict)      # empty dict
dd_dict["Joel"]["City"] = "Seattle"    
# {"Joel" : {"City" : "Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1



                        # Counters

# Turns a sequence of values into defaultdict(int)-like object mapping keys to counts

c = Counter([0, 1, 2, 0])
# {0: 2, 1: 1, 2: 1}

document = ["this", "is", "a", "list", "of", "words", "also", "a"]
word_counts = Counter(document)
for word, count in word_counts.most_common(10):
    print(word, count)




words_and_counts = Counter(word

for user, interest in interests 

for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1: 
        print(word, count)


print(words_and_counts)


                    # Sets

# A collection of distinct elements
primes_below_10 = {2, 3, 5, 7}
s = set()
s.add(1)
s.add(2)
s.add(2)
x = len(s)
y = 2 in s # True
z = 3 in s # Falsee

item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)
item_set = set(item_list) # {1, 2, 3}
num_distinct_items = len(item_set) # 3
disting_item_list = list(item_set) # [1, 2, 3]




                    # Sorting

# Sort and Sorted sort a list from smallest to largest based on naively comparing the elements to one another. 

x = [4, 1, 2, 3]
y = sorted(x)   # y = [1, 2, 3, 4]
x.sort() # now x = [1, 2, 3, 4]

x = sorted([-4, 1, -2, 3], key=abs, reverse=True) 
# is [-4, 3, -2, 1] uses library function "abs" to sort based on absolute value





                    # List Comprehensions 
# Transform a list into another list


                    # Automated Testing

# Use Assertion errors to check if a condition is true or raise a flag




                    # OOP

# Classes enncapsulate data and functions that operate on them.

class CountingClicker:

    def _init_(self, count = 0):
        
        self.count = count

    def _repr_(self):
        return f"CountingClicker(count={self.count})"
    
    def click(self, num_times = 1):
        """Click the clicker some number of times."""
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0



clicker = CountingClicker()
assert clicker.read() == 0, "Clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clikcer should have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"


# random.random produces numbers between 0 and 1
# random.randrange(10)
# random.randrange(3, 6)
# random.choice(["Alice", "Bob", "Charlie"]) chooses randomly
