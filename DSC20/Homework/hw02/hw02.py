"""
DSC 20 Winter 2024 Homework 02
Name: Derrick Dollesin
PID: A18133427
Source: https://stackoverflow.com/questions/12897374/ \
get-unique-values-from-a-list-in-python
"""

# Question 1
def valid_pairs(keys, values):
    """
    Appends tuples to a list in which each tuple will have a pair of values 
    taken from lists of same size

    Args:
        keys: list of keys (of any datatype)
        values: list of values (of any datatype)

    Returns:
        a list of tuples in which the first value in the tuples will be an item
        in keys, and the second value will be an item corresponding to the 
        same position as the key in keys but the value in values


    >>> keys = ["fun", ["not so much"]]
    >>> values = [("learning",), 6]
    >>> valid_pairs(keys, values)
    [('fun', ('learning',)), ('not valid',)]

    >>> keys = [1, "fun", [2], (1,), {}]
    >>> values = [1, {}, (1,), "island", [2]]
    >>> valid_pairs(keys, values)
    [(1, 1), ('fun', {}), ('not valid',), ((1,), 'island'), ('not valid',)]

    >>> keys =[]
    >>> values =[]
    >>> valid_pairs(keys, values)
    []

    # Add at least 3 doctests below here #
    
    >>> keys = [2.3, 'hello', []]
    >>> values = [{}, 3, "(3, 6)"]
    >>> valid_pairs(keys, values)
    [(2.3, {}), ('hello', 3), ('not valid',)]

    >>> keys = [[2], [3, 6], ['x', 'y']]
    >>> values = [1, 2, 3]
    >>> valid_pairs(keys, values)
    [('not valid',), ('not valid',), ('not valid',)]

    >>> keys = [True, False]
    >>> values = [1, 2]
    >>> valid_pairs(keys, values)
    [(True, 1), (False, 2)]

    """
    # YOUR CODE GOES HERE #

    # initializing important variables and output
    output = []
    valid_types = [int, float, str, bool, tuple]

    # return empty list if lists are empty
    if keys == [] and values == []:
        return []

    # iterate over each list and create a tuple
    for i in range(len(keys)):

        # check if type of key is a valid key type in a dictionary
        if type(keys[i]) not in valid_types:
            error = "not valid"
            pair = (error, )
        else:
            pair = (keys[i], values[i])

        # append to output 
        output.append(pair)

    # return the list of tuples
    return output


# Question 2
def tup_to_dict(tuples):
    """
    Convert a list of tuples to a dictionary using the first index of each 
    tuple as a key, and the second index as a value

    Args:
        tuples: a list containing tuples with key/value pairs from tuples


    Returns:
        a dictionary with key/value pairs from each tuple

    >>> lst = [(1, 1), ('fun', {}), ('not valid',), ((1,), 'island'), \
    ('not valid',)]
    >>> tup_to_dict(lst)
    {1: [1], 'fun': [{}], (1,): ['island']}

    >>> lst = [("not valid",), ("tree", "green"), ("tree", "blue"),\
    (1, ["key"])]
    >>> tup_to_dict(lst)
    {'tree': ['green', 'blue'], 1: [['key']]}

    # Add at least 3 doctests below here #

    >>> lst = []
    >>> tup_to_dict(lst)
    {}

    >>> lst = [("not valid",), ("not valid",)]
    >>> tup_to_dict(lst)
    {}

    >>> lst = [('fire', 'hot'), ('water', 'cold')]
    >>> tup_to_dict(lst)
    {'fire': ['hot'], 'water': ['cold']}

    """
    # YOUR CODE GOES HERE #

    # initializing output
    output = {}
    after_removal = [] # needed for removing "not valid" tuples

    # removing not valid tuples
    for tup in tuples:
        if tup[0] == "not valid":
            continue
        elif tup[0] != "not valid":
            after_removal.append(tup)

    # returning empty dict if tuples is empty
    if tuples == [] or after_removal == []:
        return {}
        
    # creating each key/value pair in the dictionary
    for pair in after_removal:
        # key/value pairs
        key = pair[0]
        value = [pair[1]]

        # check if key is already in the dictionary
        if key in output:
            value = output[key] + value

        # adding to dictionary
        output[key] = value

    # return dictionary output
    return output


# Question 3
def foods(items, prices):
    """
    Combines two lists into a dictionary, with keys being foods, and 
    values being average prices per food

    Args:
        items: a list of foods (as strings)
        prices: a list of lists where each inner list represents a price

    Returns:
        a dictionary where the keys are the food items from the first list
        and values are the average amount of money for this food

    >>> items = ["Ziblo","Crinx"]
    >>> prices = [[1, 2], [3, 4], [5, 6]]
    >>> foods(items, prices)
    {'Ziblo': 3.0, 'Crinx': 4.0}

    >>> items = ["Yumzo","Fluzu"]
    >>> prices = [[2, 3], [3, 4], [4, 5], [5, 6.2]]
    >>> foods(items, prices)
    {'Yumzo': 3.5, 'Fluzu': 4.55}

    # Add at least 3 doctests below here #

    >>> items = ["Strawberry", "Banana"]
    >>> prices = []
    >>> foods(items, prices)
    {'Strawberry': 0, 'Banana': 0}

    >>> items = ["Strawberry", "Banana"]
    >>> prices = [[1, 2], [1.1, 2.2], [1.11, 2.22]]
    >>> foods(items, prices)
    {'Strawberry': 1.07, 'Banana': 2.14}

    >>> items = ["Strawberry", "Banana"]
    >>> prices = [[100, 2], [1.1, 2.2], [1.11, 2.22]]
    >>> foods(items, prices)
    {'Strawberry': 34.07, 'Banana': 2.14}

    """
    # YOUR CODE GOES HERE #
    
    # initializing necessary variables and output
    output = {}
    num_decimals = 2
    food1 = items[0]
    food2 = items[1]
    food1_price_total = 0
    food2_price_total = 0

    # if prices is empty set the averages to 0
    if len(prices) == 0:
        food1_avg = 0
        food2_avg = 0
    else:
        # summing the prices of each food
        for price in prices:
            food1_price_total += price[0]
            food2_price_total += price[1]

        # calculating the average price
        food1_avg = round(food1_price_total / len(prices), num_decimals)
        food2_avg = round(food2_price_total / len(prices), num_decimals)

    # generating output dictionary
    output[food1] = food1_avg
    output[food2] = food2_avg

    # return output dictionary
    return output


# Question 4
def total_cost(items_you_have, ingredients):
    """
    Calculates the total price of a meal

    Args:
        items_you_have: a dictionary where keys are strings (food items) and
        values are non-negative numbers (floats)
        ingredients: a list of ingredients as strings

    Returns:
        a float which represents the total price of items given in the 
        dictionary

    >>> items = {'Yumzo': 3.5, 'Fluzu': 4.55}
    >>> ingredients = ['Yumzo', 'Fluzu']
    >>> total_cost(items, ingredients)
    8.05

    >>> items = {'Yumzo': 3.5, 'Fluzu': 4.55}
    >>> ingredients = ['Ziblo','Yumzo', 'Fluzu']
    >>> total_cost(items, ingredients)
    8.05

    >>> items = {'Yumzo': 3.5, 'Fluzu': 4.55, 'Crinx': 5.34}
    >>> ingredients = ['Ziblo','Yumzo']
    >>> total_cost(items, ingredients)
    3.5

    # Add at least 3 doctests below here #

    >>> items = {}
    >>> ingredients = []
    >>> total_cost(items, ingredients)
    0

    >>> items = {}
    >>> ingredients = ['Ziblo','Yumzo']
    >>> total_cost(items, ingredients)
    0

    >>> items = {'Yumzo': 3.5, 'Fluzu': 4.55, 'Crinx': 5.34}
    >>> ingredients = []
    >>> total_cost(items, ingredients)
    0

    """
    # YOUR CODE GOES HERE #

    # check if either arg is empty
    if ingredients == [] or items_you_have == {}:
        return 0
    
    # initializing important variables and output
    output = 0

    # iterate through ingredients and add prices if ingredient in your items 
    for ingredient in ingredients:
        if ingredient in items_you_have:
            output += items_you_have[ingredient]

    # return output float
    return output


# Question 5
def shopping(grocery_bag):
    """
    Iterates through a dictionary and returns a list of unique foods items in
    the dictionary.

    Args:
        grocery_bag: a dictionary where each key is the name of the store and
        each value is a list of foods purchased from that store

    Returns:
        a list of unique foods from the dictionary list, sorted alphabetically


    >>> bag = {'shop1': ['Munchi', 'Chirp'], 'shop2': ['Blipz', 'Sprova']}
    >>> shopping(bag)
    ['Blipz', 'Chirp', 'Munchi', 'Sprova']
    >>> bag = {'shop1': ['Munchi', 'Chirp'], 'shop2': ['Munchi', 'Sprova']}
    >>> shopping(bag)
    ['Chirp', 'Munchi', 'Sprova']
    >>> bag = {'shop1': ['Munchi', 'Chirp', 'Blipz'], \
    'shop2': ['Munchi', 'Sprova', 'Sprova'], \
    'shop3': ['Blipz', 'Sprova', 'Eggs']}
    >>> shopping(bag)
    ['Blipz', 'Chirp', 'Eggs', 'Munchi', 'Sprova']

    # Add at least 3 doctests below here #

    >>> bag = {"shop1": ['Munchi', 'egg', 'chirp'], \
    "shop2": ['Egg', 'Chirp', 'Blipz'], \
    "shop3": ['blipz', 'egg', 'Blipz']}
    >>> shopping(bag)
    ['Blipz', 'Chirp', 'Egg', 'Munchi']

    >>> bag = {}
    >>> shopping(bag)
    []

    >>> bag = {}
    >>> shopping(bag)
    []

    """
    # YOUR CODE GOES HERE #
    
    # initialize important variables and output
    output = []
    foods = list(grocery_bag.values())

    # create a list of only foods from the dictionary
    for food in foods:
        title_foods = []

        # turn the foods into title case
        for i in food:
            title_foods.append(i.title())

        # append the foods to output
        output = output + title_foods

    # sort output in alphabetical order and remove duplicates
    output = sorted(list(set(output))) 

    # return output list
    return output


# Question 6.1
def count_lines_1(filepath):
    """
    Counts the number of lines written in a file

    Args:
        filepath: a string representing a filepath

    Returns:
        an integer representing the number of lines written in a file

    >>> count_lines_1('files/test1.txt')
    6
    >>> count_lines_1('files/test2.txt')
    24

    # Add at least 3 doctests below here #

    >>> count_lines_1('files/file3_empty.txt')
    0

    >>> count_lines_1('files/bridges1.txt')
    4

    >>> count_lines_1('files/bridges2.txt')
    2

    """
    # YOUR CODE GOES HERE #

    # initializing output variable
    output = 0
    
    # opening the file and counting the number of lines written
    with open(filepath, "r") as f_out:
        for line in f_out:
            output += 1

    # returning count of lines
    return output


# Question 6.2
def count_lines_2(filepath):
    """
    Counts the number of lines written in a file

    Args:
        filepath: a string representing a filepath

    Returns:
        the number of lines written in the file as an integer

    >>> count_lines_2('files/test1.txt')
    6
    >>> count_lines_2('files/test2.txt')
    24

    # Add at least 3 doctests below here #

    >>> count_lines_2('files/bridges6.txt')
    5

    >>> count_lines_2('files/bridges1.txt')
    4

    >>> count_lines_2('files/bridges2.txt')
    2

    """
    # YOUR CODE GOES HERE #
    
    # intitializing the output variable
    output = 0

    # opening and reading the file
    with open(filepath, "r") as f_out:
        read_data = f_out.read()
        read_list = read_data.split("\n") # turn the data into a list
        output = len(read_list)

    # return output count
    return output


# Question 6.3
def count_lines_3(filepath):
    """
    Counts the number of lines written in a file

    Args:
        filepath: a string representing a filepath

    Returns:
        the number of lines written in the file as an interger

    >>> count_lines_3('files/test1.txt')
    6
    >>> count_lines_3('files/test2.txt')
    24

    # Add at least 3 doctests below here #

    >>> count_lines_3('files/file3_empty.txt')
    0

    >>> count_lines_3('files/bridges1.txt')
    4

    >>> count_lines_3('files/bridges2.txt')
    2

    """
    # YOUR CODE GOES HERE #
    
    # initialize output variable
    output = 0

    # opening and reading the file
    with open(filepath, "r") as f_out:
        read_data = f_out.readlines()
        output = len(read_data)

    # return output integer
    return output


# Question 7
def emails(filepath):
    """
    Sorts through file and returns only the emails in the file 

    Args:
        filepath: a string representing a filepath

    Returns:
        a list of emails in the same order in the input file

    >>> emails('files/file1.txt')
    ['milo@pythonia.py', 'ben@discussion.py', 'bryce@gradescope.py']
    >>> emails('files/file2.txt')
    ['milo@pythonia.py', 'ben@discussion.py', 'bryce@gradescope.py', \
'dave@gmail.com']
    >>> emails('files/file3_empty.txt')
    []

    # Add at least 3 doctests below here #

    >>> emails('files/file3.txt')
    ['ddollesin@ucsd.py', 'ddollesin@ucsd.edu', 'derdollesin@comcast.net']

    >>> emails('files/file4.txt')
    ['ddollesin@ucsd.py', 'ddollesin@ucsd.edu', 'derdollesin@comcast.net']

    >>> emails('files/file5.txt')
    ['ddollesin@ucsd.edu', 'derdollesin@comcast.net', 'derdollesin@gmail.com']

    """
    # YOUR CODE GOES HERE #
    
    # initialize output variables
    output = []
    read_lines = []

    # open and read data from file
    with open(filepath, "r") as f_out:
        read_data = f_out.readlines()
        # create a new list of each line from file as a list
        for line in read_data:
            data_to_list = line.split(",") 
            read_lines.append(data_to_list)

    # append only lines with "@" to output
    for lines in read_lines:
        for line in lines:
            if "@" in line:
                output.append(line.strip())

    # return output list
    return output


# Question 8
def counter(filepath_to_fix):
    """
    Converts a string into a filepath, and writes into the file two integers
    representing number of chars and digits in the filename.  

    Args:
        filepath_to_fix: a string representing an incorrectly written filepath

    Returns:
        Nothing ~ writes to a text file - two integer values:
            1. number of digits in filename
            2. number of characters in filename

    >>> counter('list123')
    >>> with open('files/list123.txt', 'r') as outfile1:
    ...    print(outfile1.read().strip())
    3
    4
    >>> counter('one1two2three3')
    >>> with open('files/one1two2three3.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    3
    11
    >>> counter('tricky ')
    >>> with open('files/tricky.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    0
    7

    # Add at least 3 doctests below here #

    >>> counter('idk221idk')
    >>> with open('files/idk221idk.txt', 'r') as outfile1:
    ...    print(outfile1.read().strip())
    3
    6

    >>> counter('    a')
    >>> with open('files/a.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    0
    5

    >>> counter(' 2')
    >>> with open('files/2.txt') as outfile3:
    ...    print(outfile3.read().strip())
    1
    1

    """
    # YOUR CODE GOES HERE #
    
    # initialize necessary variable
    filename = filepath_to_fix.strip()
    filepath = "files/" + filename + ".txt"
    num_chars = 0
    num_digits = 0

    # check each char in filename for digits
    for i in list(filepath_to_fix):
        if i.isalpha() or i == " ": # checks if char is an char
            num_chars += 1

    # calculate the number of characters
    num_digits = len(filepath_to_fix) - num_chars

    # create message to write into file
    to_txt = f"{num_digits}\n{num_chars}"

    # write to filepath
    with open(filepath, "w") as f_in:
        f_in.write(to_txt)


# Question 9
def combine_bridges(bridges):
    """
    Take in bridge data from a file and calculates the total number of people 
    who cross each bridge and writes that data to a new text file

    Args:
        bridges: a filepath to a file which contains bridge data

    Returns:
        Nothing ~ writes to a text file each bridge and the total number of 
        people who've crossed each bridge

    >>> combine_bridges('files/bridges1.txt')
    >>> with open('files/combined_bridges.txt', 'r') as f:
    ...    print(f.read().strip())
    bridge1:9
    bridge2:3
    bridge3:1

    >>> combine_bridges('files/bridges2.txt')
    >>> with open('files/combined_bridges.txt', 'r') as f:
    ...    print(f.read().strip())
    bridge1:5
    bridge2:0

    >>> combine_bridges('files/bridges3.txt')
    >>> with open('files/combined_bridges.txt', 'r') as f:
    ...    print(f.read().strip())
    bridge2:3
    bridge3:1
    bridge1:5

    # Add at least 3 doctests below here #

    >>> combine_bridges('files/bridges4.txt')
    >>> with open('files/combined_bridges.txt', 'r') as f:
    ...    print(f.read().strip())
    bridge1:0
    bridge2:0
    bridge3:0

    >>> combine_bridges('files/bridges5.txt')
    >>> with open('files/combined_bridges.txt', 'r') as f:
    ...    print(f.read().strip())
    bridge17:34
    bridge2:3
    bridge3:1

    >>> combine_bridges('files/bridges6.txt')
    >>> with open('files/combined_bridges.txt', 'r') as f:
    ...    print(f.read().strip())
    bridge1:1
    bridge2:2
    bridge3:3
    bridge4:4
    bridge5:5

    """
    # YOUR CODE GOES HERE #
    
    # initializing important variables
    bridge_data = {}
    filepath = "files/combined_bridges.txt"

    # extracting data from input text file
    with open(bridges, "r") as f_out:
        read_data = f_out.readlines()

    # sorting data and calculating number of people crossing each bridge
    for i in range(len(read_data)):
        # position in the string of the colon
        col_pos = read_data[i].find(":") 

        bridge = read_data[i][0:col_pos]

        # calculating total number of people per bridge
        if bridge in bridge_data:
            bridge_data[bridge] = bridge_data[bridge] \
            + int(read_data[i][(col_pos + 1):].strip())
        else:
            bridge_data[bridge] = \
            int(read_data[i][(col_pos + 1):].strip())

    # writing new data to output text file
    with open(filepath, "w") as f_in:
        for bridge in bridge_data:
            text = f"{bridge}:{bridge_data[bridge]}\n"

            f_in.write(text)

