"""
DSC 20 Winter 2024 Homework 04
Name: Derrick Dollesin
PID: A18133427
Source: 
"""

# Question 1
def know_plant(path):
    """
    Sorts through data in a file and outputs only plant data

    Args:
        path: a string representing a filepath

    Returns:
        a dictionary with plant names as keys and a list of its properties as \
        values

    >>> know_plant('files/diary01.txt')
    {'Harrada': ['Paralyze', 'Silence']}
    >>> know_plant('files/diary02.txt')
    {'Harrada': ['Paralyze'], 'Flame Stalk': ['Invisibility']}

    # Add at least 3 doctests below here #

    >>> know_plant('files/diary03.txt')
    {'Moon Blossom': ['Healing', 'Invisibility', 'Ethereal'], 'Sunflower': \
['Fire Resistance']}

    >>> know_plant('files/diary04.txt')
    {'Harrada': ['Paralyze'], 'Sunflower': ['Fire Resistance'], \
'Moon Blossom': ['Healing', 'Invisibility', 'Ethereal']}

    >>> know_plant('files/diary05.txt')
    {'Harrada': ['Paralyze'], 'Moon Blossom': ['Healing', 'Invisibility', \
'Ethereal'], 'Sunflower': ['Fire Resistance']}

    """
    # YOUR CODE GOES HERE #

    second_item = 2

    # the data we want will be the lines in the file between these two lines
    header = "Experiment Results:"
    ender = "End"
    
    # open the file and extract the data
    with open(path, "r") as f_out:
        read_data = f_out.readlines()

    # strip any newline and spaces from the lines
    stripped_data = list(map(lambda x: x.strip(), read_data))

    # convert all the strings to title case
    titled_data = list(map(lambda x: x.title(), stripped_data))

    # initialize variables for the positions of the header and ender
    start = titled_data.index(header) + 1
    end = titled_data.index(ender)

    # extract only the data we wanted
    experiment_results = titled_data[start: end]

    # remove "?" and convert to csv
    remove_questions = [x.replace("?", ",") if "?" in x else x for x in \
    experiment_results]

    # turn the strings into lists
    data = list(map(lambda x: x.split(","), remove_questions))

    # extracting only the plant information
    items = [(x[0], x[second_item]) for x in data]

    # initialize the output dictionary
    output = {}

    # iterate through the items and create our output dictionary
    for i in items:

        # append values to keys if key already in dictionary
        if i[0] in list(output.keys()):
            output[i[0]] = output[i[0]] + [i[1]]
        # add key/value pair to output
        else:
            output[i[0]] = [i[1]]

    # return output dictionary
    return output


# Question 2
def create_potion(plants, path):
    """
    Writes to a .txt file the name of a plant and it's affect

    Args:
        plants: a dictionary like from question 1
        path: path to a .txt file as a string

    Returns:
        Writes the plant names and their affects to a file and determines \
        whether they are poisonous or potions

    >>> dict1 = {'Harrada': ['Paralyze', 'Silence']}
    >>> create_potion(dict1, "files/potion1.txt")
    >>> with open("files/potion1.txt", 'r') as f:
    ...     for l in f:
    ...         print(l.strip())
    Harrada
    Potion
    Paralyze,Silence
    >>> dict2 = {'Harrada': ['Paralyze'], 'Flame Stalk': ['Paralyze'],\
'Stone Flower': ['Paralyze']}
    >>> create_potion(dict2, "files/potion2.txt")
    >>> with open("files/potion2.txt", 'r') as f:
    ...     for l in f:
    ...         print(l.strip())
    Harrada
    Flame Stalk
    Stone Flower
    Poison
    Paralyze

    # Add at least 3 doctests below here #

    >>> dict3 = {'Moon Blossom': ['Healing'], 'Sunflower': ['Fire Resistance']}
    >>> create_potion(dict3, "files/potion3.txt")
    >>> with open("files/potion3.txt", 'r') as f:
    ...     for l in f:
    ...         print(l.strip())
    Moon Blossom
    Sunflower
    Potion
    Fire Resistance
    Healing

    >>> dict4 = {'Harrada': ['Paralyze'], 'Sunflower': ['Paralyze']}
    >>> create_potion(dict4, "files/potion4.txt")
    >>> with open("files/potion4.txt", 'r') as f:
    ...     for l in f:
    ...         print(l.strip())
    Harrada
    Sunflower
    Poison
    Paralyze

    >>> dict5 = {'Nightshade': ['Poison'], 'Wolfsbane': ['Poison']}
    >>> create_potion(dict5, "files/potion5.txt")
    >>> with open("files/potion5.txt", 'r') as f:
    ...     for l in f:
    ...         print(l.strip())
    Nightshade
    Wolfsbane
    Potion
    Poison

    """
    # YOUR CODE GOES HERE #

    # initializing the list of key/value pairs where each item in titlecase
    keys = [key.title() for key in list(plants.keys())]
    values = []

    # initializing the value of plant types whether poison or potion
    plant_types = ""

    # loop through plants and update values depending on if the value is a 
    # list type or just a string
    for key in plants:

        # update values list
        if type(plants[key]) == list:
            values = values + [",".join([value.title() for value in \
            plants[key]])]
        else:
            values = values + [plants[key].title()]

    # encode plant type if there are multiple "Paralyze"s then it's "Poison"
    # else it's a "Potion"
    if values.count("Paralyze") > 1:
        plant_types = plant_types + "\nPoison\n"
    else:
        plant_types = plant_types + "\nPotion\n"

    # create a string output where keys and values lists are joined by a 
    # newline and plant type goes in between 
    output = "\n".join(keys) + plant_types + \
    "\n".join(sorted(list(set(values))))

    # write output to file
    with open(path, "w") as f_in:
        f_in.write(output)

# Question 3
def potion_name(plants):
    """
    Creates a potion name based on given plants, defined by a certain rules

    Args:
        plants:

    Returns:
        the name of a potion defined by:
        1. only plants that are strictly less than $20
        2. number of plants that pass the price check is even, then the first \
        three characters of each plant name put together to create potion name
        3. number of plants that pass the price check is odd, then the last \
        three characters of each plant name put together to create potion name

    >>> input_1 = [('Harrada', 'yellow', 19), ('Flame Stalk', 'red', 13), \
('Stone Flower', 'gray', 32), ('Crystal Snowflake', 'blue', 48), \
('Foxglove', 'pink', 20), ('Dangerous Nightshade', 'purple', 18)]
    >>> potion_name(input_1)
    'Adaalkade'

    >>> input_2 = [('White Snakeroot', 'white', 19), \
('Bitter Hogweed', 'black', 13)]
    >>> potion_name(input_2)
    'Whibit'

    >>> input_3 = []
    >>> potion_name(input_3)
    ''

    # Add at least 3 doctests below here #

    >>> input_4 = [('Wolfsbane', 'white', 15), ('Belladonna', 'green', 18), \
('Mandrake', 'brown', 22), ('Aconitum', 'blue', 9)]
    >>> potion_name(input_4)
    'Anennatum'

    >>> input_5 = [('Sunflower', 'yellow', 14), ('Lavender', 'purple', 21), \
('Rosemary', 'green', 18), ('Chamomile', 'white', 12)]
    >>> potion_name(input_5)
    'Weraryile'

    >>> input_6 = [('Basil', 'green', 25), ('Peppermint', 'green', 17), \
('Thyme', 'gray', 19), ('Sage', 'blue', 8)]
    >>> potion_name(input_6)
    'Intymeage'


    """
    # YOUR CODE GOES HERE #
    len_tuple = 3
    third_item = 2
    max_price = 20
    first_char = -3

    # assertion statements
    assert type(plants) == list 
    assert all([type(item) == tuple for item in plants])
    assert all([len(item) == len_tuple for item in plants])
    assert all([type(item[0]) == str for item in plants])
    assert all([type(item[1]) == str for item in plants])
    assert all([type(item[third_item]) == int and item[third_item] > 0 for \
    item in plants])

    # filter by plants that can be purchased
    affordable = list(filter(lambda x: x[third_item] < max_price, plants))

    # only take the first three letters of each plant or the last three and 
    # put them into a list
    three_chars = list(map(lambda x: x[0][0:len_tuple] if len(affordable) % \
    third_item == 0 \
    else x[0][first_char:len(x[0])], affordable))

    # join the list of letters into one string
    return "".join(three_chars).title()


# Question 4
def trade(potions, prices, consumer_list):
    """
    Calculates the most expensive combination of potions that a consumer wants

    Args:
        potions: a list of strings representing potion names. these are \
                 potions you have
        prices: a list of non-negative integers representing the prices of \
                potions. It has the same length as potions
        consumer_lists: a list of strings representing potions demanded by \
                        the consumer. You should only consider those in your \
                        inventory. 

    Returns:
        return the price of the most expensive combination

    >>> trade(['health', 'magic'], [10, 10], ['health', 'magic'])
    20
    >>> trade(['health', 'magic', 'large_health'], [10, 20, 30], \
    ['health', 'large_health', 'magic'])
    50
    >>> trade(['health', 'magic', 'large_health', 'large_magic'],\
    [5, 10, 15, 20], ['magic', 'health', 'large_health'])
    25

    # Add at least 3 doctests below here #

    >>> trade(['strength', 'speed'], [15, 20], ['speed', 'strength'])
    35

    >>> trade(['invisibility', 'fire_resistance', 'healing'], [25, 30, 15], \
['invisibility', 'healing', 'fire_resistance'])
    55

    >>> trade(['love', 'happiness', 'joy', 'peace'], [10, 15, 20, 25], \
['peace', 'love', 'joy'])
    45


    """
    # YOUR CODE GOES HERE #

    last_item = -1
    second_last_item = -2

    assert type(potions) == list
    assert all([type(value) == str for value in potions])
    assert type(prices) == list
    assert all([type(value) == int for value in prices])
    assert type(consumer_list) == list
    assert all([type(value) == str for value in consumer_list])

    combined = zip(potions, prices)

    available = list(filter(lambda x: x[0] in consumer_list, combined))

    sorted_prices = sorted(list(map(lambda x: x[1], available)))

    output = sorted_prices[last_item] + sorted_prices[second_last_item]

    return output


# Question 5
def potion_magic(potions, operations):
    """
    Executes the operations in the order they appear and returns their output

    Args:
        potions: a list of potion names (string)
        operations: a list of operations (string) ["mix", "reduce", \
        "eliminate"]

    Returns:
        executes operations in operations in the order they appear and returns
        the result

    >>> potion_magic("incorrect input", ['mix'])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> potion_magic(['health', 'magic'], ['eliminate', 'reduce'])
    ['hea', 'mag']
    >>> potion_magic(['health_large_potion', 'health'], ['eliminate', 'mix'])
    'htlaeh'

    # Add at least 3 doctests below here #

    >>> potion_magic(['strength', 'speed', 'mana'], ['reduce', 'mix'])
    'namepsrts'

    >>> potion_magic(['fire', 'ice', 'earth'], ['eliminate', 'reduce', 'mix'])
    'raeecirif'

    >>> potion_magic(['love', 'happiness', 'joy'], ['eliminate', 'mix'])
    'yojevol'


    """
    max_length = 6
    reduce_length = 3
    step = -1

    # Break lines if go past 79 characters
    op_dict = {
        'mix': lambda lst: ''.join(lst)[::step],
        'reduce': lambda lst: list(map(lambda x: x[:reduce_length] if len(x) \
        > reduce_length else x, \
        lst)),
        'eliminate': lambda lst: list(filter(lambda x: len(x) <= max_length, \
        lst))
    }

    # YOUR CODE GOES HERE #

    assert type(potions) == list
    assert all([type(item) == str for item in potions])
    assert type(operations) == list
    assert all([type(item) == str for item in operations])
    assert all(op in op_dict for op in operations)

    for op in operations:
        potions = op_dict[op](potions)

    return potions
