from __future__ import division
from collections import Counter
from collections import defaultdict
import random
import re




users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Laquandria"},
    {"id": 4, "name": "Devante"},
    {"id": 5, "name": "Chi"},
    {"id": 6, "name": "Laqruishia"},
    {"id": 7, "name": "Hicks"},
    {"id": 8, "name": "Calvin"},
    {"id": 9, "name": "Klein"},
]


# Create list (array) of tuples (editable array)
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


# Create a dict where key = user ids and value = list of friend ids. 

# Initialize the dict (object) with key = user id, and value = [] empty list (array) for each user:
friendships = {user["id"]: [] for user in users}



# loop through the dict and add user id of i & j friends for user. 

for i, j in friendship_pairs:
    # user[i] is the user whose id is i
    friendships[i].append(j) #add i as friend of j
    friendships[j].append(i) #add j as friend i 



            # Total number of connections
def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id] # "friends: x"
    return len(friend_ids)      

total_connections = sum(number_of_friends(user)
                        for user in users)  # 24


num_users = len(users)      # len of the users list
avg_connections = total_connections / num_users     # 2.4



            # Who has the most friends?

# create a 2D list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
                    for user in users]


# sort num_friends_by_id list in reverse order of largest j to smallest.
num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1], reverse=True
)



# each pair is (user_id, num_friends)
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), # (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]


def foaf_ids_bad(user):
    # "foaf" = friend of a friend
    return [foaf_id
    for friend_id in friendships[user["id"]]
    for foaf_id in friendships[friend_id]]


print(friendships[0])
print(friendships[1])
print(friendships[2])



def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        #For each of my friends,
        for foaf_id in friendships[friend_id]
        #find their friends
            
            if foaf_id != user_id
        #who aren't me

    and foaf_id not in friendships[user_id]
        #and aren't my friends.
    )

print(friends_of_friends(users[3]))




                # Connect Users by Interest
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
    ]


# Less effective 
def data_scientists_who_like(target_interest):
    """Find the ids of all the users who like target interest."""
    return [user_id
for user_id, user_interest in interests
if user_interest == target_interest]


# More effective
# Create indices using "defaultdict" (dict = object)
# _____________________________________________________
# Key = interest, Value = list of user_ids w/interests
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# Key = user_ids, values = lists of interests
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)




# Most interests in common
def most_common_interests_with(user):
    return Counter(
        interested_user_id

    for interest in interests_by_user_id[user["id"]]
    

    for interested_user_id in user_ids_by_interest[interest]

        if interested_user_id != user["id"]
    )

print(most_common_interests_with(users[4]))





                # Salaries and Experience

salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)]



# Less Effective for grouping salary
# Object: Key = years, Value = salary
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:

    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)

for tenure, salaries in salary_by_tenure.
items()
}


# More Effective (bucket tenures)
def tenure_bucket(tenure):
    if tenure < 2: 
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# Key = tenure bucket, Value = list of salaries
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    
    bucket = tenure_bucket(tenure)

salary_by_tenure_bucket[bucket].append(salary)

# Key = tenure bucket, Value = average salary for bucket
average_salary_by_bucket = {

    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

print(average_salary_by_bucket)


def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else: 
        return "paid"


