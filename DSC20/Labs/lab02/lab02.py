"""
DSC 20 Winter 2024 Lab 02
Name: Derrick Dollesin
PID: A18133427
Source: TODO
"""

# Question 1
def directions(all_directions):
    """
    Returns a list where only the directions for DSC20 are kept. If the list is 
    empty, return an empty list

    Args:
        all_directions: a list of strings containing directions 

    Returns: A list containing only DSC20 directions

    >>> all_directions = ["DSC20-Loops", "DSC20-Slicing", "DSC10-numpy"]
    >>> directions(all_directions)
    ['Loops', 'Slicing']
    >>> all_directions = ["DSC10-numpy", "DSC80-pandas"]
    >>> directions(all_directions)
    []
    >>> all_directions = ["DsC20-Loops", "dsc20-Slicing", "DSC10-numpy"]
    >>> directions(all_directions)
    ['Loops', 'Slicing']
    """
    # YOUR CODE GOES HERE #

    temp = []
    
    for i in all_directions:
        if i[:5].upper() == 'DSC20':
            temp.append(i[6:])

    return temp


# Question 2.1
def easy_topics(topics, difficulty):
    """
    Create a new list of tuples such that: 
        - If the topic's difficulty is less than or equal to the general 
        difficulty keep as is
        - If the topic's difficulty is greater than the general difficulty, 
        replace it with 'too early'

    Args:
        topics: a list of tuples where the first element of each tuple is a 
        string (a topic) and the second element is a positive integer 
        (difficulty of specific topic)
        difficulty: a positive integer used to represent general difficulty

    Returns: A new list with new tuples satisfying the conditions above

    >>> topics = [('dsc20:loops.', 1), ('dsc20:recursion.', 3), \
('dsc20:slicing.', 2), ('dsc20:HOF.', 5)]
    >>> easy_topics(topics, 5)
    [('dsc20:loops.', 1), ('dsc20:recursion.', 3), \
('dsc20:slicing.', 2), ('dsc20:HOF.', 5)]
    >>> topics = [('dsc20:loops.', 1), ('dsc20:recursion.', 7), \
('dsc20:slicing.', 2), ('dsc20:HOF.', 5)]
    >>> easy_topics(topics, 5)
    [('dsc20:loops.', 1), ('dsc20:recursion.', 'too early'), \
('dsc20:slicing.', 2), ('dsc20:HOF.', 5)]
    >>> easy_topics([], 5)
    []
    """
    # YOUR CODE GOES HERE #
    
    temp = []

    for topic in topics:
        if topic[1] <= difficulty:
            temp.append(topic)
        elif topic[1] > difficulty:
            temp.append((topic[0], 'too early'))

    return temp


# Question 2.2
def easy_topics_lists(topics, difficulty):
    """
    Returns the original list of lists using the following rules:
        - Removes 'dsc20:' from the beginning of each topic
        - Remove a period at the end of each topic
        - If the topic's difficulty is greater than the general difficulty, 
        replace it with 'too early'

    Args:
        topics: a list of lists where the first element of each list is a 
        string (a topic) and the second element is a positive integer 
        (difficulty of specific topic)
        difficulty: a positive integer used to represent general difficulty

    Returns: The original list of lists modified to satisfy the conditions above
            
    >>> topics = [['dsc20:loops.', 1], ['dsc20:recursion.', 3], \
['dsc20:slicing.', 2], ['dsc20:HOF.', 5]]
    >>> easy_topics_lists(topics, 5)
    [['loops', 1], ['recursion', 3], ['slicing', 2], ['HOF', 5]]
    >>> topics = [['dsc20:loops.', 1], ['dsc20:recursion.', 7], \
['dsc20:slicing.', 2], ['dsc20:HOF.', 5]]
    >>> easy_topics_lists(topics, 5)
    [['loops', 1], ['recursion', 'too early'], ['slicing', 2], ['HOF', 5]]
    >>> easy_topics_lists([], 5)
    []
    """
    # YOUR CODE GOES HERE #

    if topics == []:
        return []
    
    for topic in topics:
        topic[0] = topic[0][6:-1]

        if topic[1] > difficulty:
            topic[1] = 'too early'


    return topics


# Question 3 
def up_down(directions):
    """
    Portray a list of directions using arrows - you can follow any direction 
    except 'up'

    Args:
        directions: a list of strings representing directions

    Returns:
        '<-' if direction is 'left'
        '->' if direction is 'right'
        'V' if direction is 'down'
        return the most recent version of the output if direction is 'up'

    >>> dircts = ["left", "right", "right", "up", "left"]
    >>> up_down(dircts)
    '<-->->'
    >>> dircts = ["left", "right", "left", "down", "left"]
    >>> up_down(dircts)
    '<--><-V<-'
    >>> up_down([])
    ''
    """
    # YOUR CODE GOES HERE #
    
    if directions == []:
        return ''

    left = "<-"
    right = "->"
    down = "V"

    direct = ""
    i = 0

    message = ""

    while i <= len(directions) - 1:
        direct = directions[i]

        if direct == "left":
            message = message + left
        elif direct == "right":
            message = message + right
        elif direct == "down":
            message = message + down
        else:
            break

        i += 1

    return message


# Question 4
def creatures(first_group, second_group):
    """
    Returns the number of female and male names as a tuple. Assume all names 
    have at least length of 1

    Args:
        first_group: string with names separated by one space
        second_group: string with names separated by a comma

    Returns: The number of female and male names as a tuple

    >>> first = "fifif fafaf fufuf"
    >>> second = "wiwiw,wawaw,wuwuw"
    >>> creatures(first, second)
    (3, 3)

    >>> first = "fefel fafaf f"
    >>> second = "wiwiw,wawaw,wuwuw,wow"
    >>> creatures(first, second)
    (2, 4)
    """
    # YOUR CODE GOES HERE #
    
    first_list = first_group.split(" ")
    second_list = second_group.split(",")

    first_count = 0
    second_count = 0

    for i in first_list:
        if i[0] == i[-1]:
            first_count += 1

    for i in second_list:
        if i[0] == i[-1]:
            second_count += 1

    return (first_count, second_count)


# Question 5.1
def days(office_hours):
    """
    Returns a list of all days in the given dictionary

    Args:
        office_hours: dictionary where each key is a day of the week and each 
        value is a list of tutor names for that day

    Returns: A list of all days in the given dictionary

    >>> office_hours = {"Monday": ["Bryce", "Ben"], "Tuesday": ["Teressa"]}
    >>> days(office_hours)
    ['Monday', 'Tuesday']
    >>> office_hours = {}
    >>> days(office_hours)
    []
    >>> office_hours = {"Saturday": [], "Sunday": [], "Friday": ["Ben"]}
    >>> days(office_hours)
    ['Saturday', 'Sunday', 'Friday']
    """
    # YOUR CODE GOES HERE #
    
    if office_hours == {}:
        return []

    return list(office_hours.keys())


# Question 5.2
def how_many_days(office_hours):
    """
    Returns the number of days in the dictionary

    Args:
        office_hours: dictionary where each key is a day of the week and each 
        value is a list of tutor names for that day

    Returns: The number of days in the dictionary

    >>> office_hours = {"Monday": ["Bryce", "Ben"], "Tuesday": ["Teressa"]}
    >>> how_many_days(office_hours)
    2
    >>> office_hours = {}
    >>> how_many_days(office_hours)
    0
    >>> office_hours = {"Saturday": [], "Sunday": [], "Friday": ["Ben"]}
    >>> how_many_days(office_hours)
    3
    """
    # YOUR CODE GOES HERE #
    
    return len(days(office_hours))


# Question 5.3
def little_help(office_hours):
    """
    Returns the number of tutors on the day with the least amount of tutors. If
    there are no tutors, return 0

    Args:
        office_hours: dictionary where each key is a day of the week and each 
        value is a list of tutor names for that day

    Returns: The number of tutors on the day with the least amount of tutors

    >>> office_hours = {"Monday": ["Bryce", "Ben"], "Tuesday": ["Teressa"]}
    >>> little_help(office_hours)
    1
    >>> office_hours = {}
    >>> little_help(office_hours)
    0
    >>> office_hours = {"Saturday": [], "Sunday": [], "Friday": ["Ben"]}
    >>> little_help(office_hours)
    0
    """
    # YOUR CODE GOES HERE #

    if office_hours == {}:
        return 0
    
    day_list = days(office_hours)
    people_count = []

    for day in day_list:
        people_count.append(len(office_hours[day]))

    lowest_index = people_count.index(min(people_count))

    return lowest_index


# Question 5.4
def best_day(office_hours):
    """
    Returns the day of the week with the most number of tutors. If there is a 
    tie, return the last day and if there are no tutors, return ''

    Args:
        office_hours: dictionary where each key is a day of the week and each 
        value is a list of tutor names for that day
    
    Returns: The day of the week with the most number of tutors

    >>> office_hours = {"Monday": ["Bryce", "Ben"], "Tuesday": ["Teressa"]}
    >>> best_day(office_hours)
    'Monday'
    >>> office_hours = {}
    >>> best_day(office_hours)
    ''
    >>> office_hours = {"Saturday": [], "Sunday": [], "Friday": ["Ben"]}
    >>> best_day(office_hours)
    'Friday'
    >>> office_hours = {"Sat": [], "Monday": ["Bryce"], "Friday": ["Ben"]}
    >>> best_day(office_hours)
    'Friday'
    """
    # YOUR CODE GOES HERE #
    
    if office_hours == {}:
        return ""

    day_list = days(office_hours)
    d = ""
    x = 0

    for day in day_list:
        if len(office_hours[day]) >= x:
            d = day
            x = len(office_hours[d])

    return d


# Question 5.5
def added_day(office_hours, day):
    """
    Return an updated dictionary with a new day added as a key. If the day 
    already exists, do nothing. If the day is new, then add an empty list as a 
    corresponding value

    Args:
        office_hours: dictionary where each key is a day of the week and each 
        value is a list of tutor names for that day
        day: string specifying which day to add

    Returns: An updated dictionary with a new day added as a key

    >>> office_hours = {"Monday": ["Bryce"], "Tuesday": ["Teressa"]}
    >>> added_day(office_hours, "Wed")
    {'Monday': ['Bryce'], 'Tuesday': ['Teressa'], 'Wed': []}
    >>> office_hours = {}
    >>> added_day(office_hours, "Monday")
    {'Monday': []}
    >>> office_hours = {"Sat": [], "Sun": [], "Friday": ["Ben"]}
    >>> added_day(office_hours, "sat")
    {'Sat': [], 'Sun': [], 'Friday': ['Ben'], 'sat': []}
    """
    # YOUR CODE GOES HERE #
    
    day_list = days(office_hours)

    if day in day_list:
        return office_hours
    else:
        office_hours[day] = []

    return office_hours 


# Question 5.6
def added_help(office_hours, day, tutor):
    """
    Returns an updated dictionary where day becomes a key and tutor becomes
    an item in a value list. If the day already exists in the dictionary, then 
    just update the value list corresponding to this day

    Args:
        office_hours: dictionary where each key is a day of the week and each 
        value is a list of tutor names for that day
        day: string specifying which day to add
        tutor: string specifying the tutor to add

    Returns: The updated dictionary with day and tutor added

    >>> office_hours = {"Monday": ["Bryce"], "Tuesday": ["Teressa"]}
    >>> added_help(office_hours, "Wed", "Jieqi")
    {'Monday': ['Bryce'], 'Tuesday': ['Teressa'], 'Wed': ['Jieqi']}
    >>> office_hours = {"Monday": ["Bryce"], "Tuesday": ["Teressa"]}
    >>> added_help(office_hours, "Monday", 'Jieqi')
    {'Monday': ['Bryce', 'Jieqi'], 'Tuesday': ['Teressa']}
    >>> office_hours = {"Monday": ["Bryce"], "Tuesday": ["Teressa"]}
    >>> added_help(office_hours, "Monday", 'Bryce')
    {'Monday': ['Bryce', 'Bryce'], 'Tuesday': ['Teressa']}
    """
    # YOUR CODE GOES HERE #
    
    o = added_day(office_hours, day)

    add_tutor = o[day] + [tutor]

    office_hours[day] = add_tutor

    return office_hours


# Question 5.7
def cancel(office_hours, tutor):
    """
    Return an updated dictionary with the tutor's name completely removed

    Args:
        office_hours: dictionary where each key is a day of the week and each 
        value is a list of tutor names for that day
        tutor: string specifying the tutor to remove
    
    Returns: The updated dictionary with the tutor's name removed

    >>> office_hours = {"Monday": ["Bryce"], "Tuesday": ["Teressa"]}
    >>> cancel(office_hours, "Jieqi")
    {'Monday': ['Bryce'], 'Tuesday': ['Teressa']}
    >>> office_hours = {"Monday": ["Ben"], "Tuesday": ["Teressa", "Ben"]}
    >>> cancel(office_hours, 'Ben')
    {'Monday': [], 'Tuesday': ['Teressa']}
    >>> office_hours = {"Monday": []}
    >>> cancel(office_hours, 'ghost')
    {'Monday': []}
    """
    # YOUR CODE GOES HERE #
    
    for day in office_hours:
        temp = office_hours[day]

        if tutor in temp:
            temp.remove(tutor)

        office_hours[day] = temp

    return office_hours




# Question 6 
def my_identification(random_dict):
    """
    Creates a string based on the following rules:
        - If a value is a string, and consists of letters only, reverse the 
        corresponding key
        - If a value is a non-negative integer and even, generate a string of 
        '*' with half of that number
        - If the message is a negative integer, get the second to last 
        character of the corresponding key
        - Otherwise, do not add anything

    Args:
        random_dict: dictionary where keys are strings but values can be
        anything

    Returns: A concatenated string consisting of the substrings generated at 
    each step of the iteration 

    >>> random_dict = {"Guest": "My1time", "Hello": "welcome", \
    "age": 10, "number": -4}
    >>> my_identification(random_dict)
    'olleH*****e'
    >>> random_dict = {'Ja': 2, 'Jo': 'yeh'}
    >>> my_identification(random_dict)
    '*oJ'
    >>> random_dict = {'Jo': 5, 'Ja': 'ab'}
    >>> my_identification(random_dict)
    'aJ'
    """
    # YOUR CODE GOES HERE #

    if random_dict == {}:
        return ""
    
    message = ""

    for i in list(random_dict.keys()):
        if type(random_dict[i]) == str and random_dict[i].isalpha():
            message = message + i[::-1]

        elif type(random_dict[i]) == int and random_dict[i] > 0 and \
        random_dict[i] % 2 == 0:
            message = message + ("*" * int(random_dict[i] / 2))

        elif type(random_dict[i]) == int and random_dict[i] < 0:
            message = message + (i[-2])

        else:
            continue


    return message

                    


