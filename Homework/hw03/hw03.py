"""
DSC 20 Winter 2024 Homework 03
Name: Derrick Dollesin
PID: A18133427
Source: TODO
"""

# Question 1.1
def animals(animal_dict, target):
    """
    Iterates through each animal in a dictinary and returns a list of animals
    that are a specified species

    Args:
        animal_dict: dictionary where each dictionary key is a string of an \
                     animal name and its value is a string that states the \
                     type of that animal
        target: a string of a type of animal

    Returns:
        a list of animal name(s) that are of the same type as target (case \
        sensitive)

    >>> animals_dict = {"dogs": "mammals", "snakes": "reptiles", \
    "dolphins": "mammals", "sharks": "fish"}
    >>> target = "mammals"
    >>> animals(animals_dict, target)
    ['dogs', 'dolphins']

    >>> target = "amphibians"
    >>> animals(animals_dict, target)
    []

    >>> animals_dict = {True: "mammals"}
    >>> animals(animals_dict, target)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below

    >>> animals_dict = {"dogs": True}
    >>> animals(animals_dict, target)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> animals_dict = {"dogs": "mammals", "snakes": "reptiles", \
    "dolphins": "reptiles", "sharks": "fish"}
    >>> target = "reptiles"
    >>> animals(animals_dict, target)
    ['snakes', 'dolphins']

    >>> animals_dict = {"dogs": "mammals", "snakes": "reptiles", \
    "dolphins": "Mammals", "sharks": "fish"}
    >>> target = "mammals"
    >>> animals(animals_dict, target)
    ['dogs']

    """
    # YOUR CODE GOES HERE #

    # initializing key and value lists from animal dict
    animal_keys = list(animal_dict.keys())
    animal_values = list(animal_dict.values())
    
    # all assertion checks
    assert type(animal_dict) == dict
    assert all([type(key) == str for key in animal_keys])
    assert all([type(value) == str for value in animal_values])
    assert type(target) == str

    # creating the output
    output = [animal for animal in animal_dict if animal_dict[animal] == \
    target]

    # return list
    return output


# Question 1.2
def animal_type(animals):
    """
    Iterates through animals and returns a list of predator types for each \
    animal

    Args:
        animals: a dictionary where each key is a string of an animal name \
                 and its value is a list with two elements
            <current_energy> is an integer representing the current energy \
                             state of the animal.
            <animal_type> is a string representing the type of the animal.

    Returns:
        a list with the corresponding animal type

    >>> animals = {"dogs": [10, "omnivores"], "snakes": [8, "carnivores"], \
    "lions": [12, "carnivores"], "sheep": [7, "herbivores"]}
    >>> animal_type(animals)
    ['omnivores', 'carnivores', 'carnivores', 'herbivores']

    >>> animals = {"bears": [5, "omnivores"]}
    >>> animal_type(animals)
    ['omnivores']

    >>> animals = {"dogs": [0.8, "omnivores"], "snakes": [8.1, "carnivores"], \
    "lions": [12, "carnivores"], "sheep": [7, "herbivores"]}
    >>> animal_type(animals)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below

    >>> animals = {}
    >>> animal_type(animals)
    []

    >>> animals = {True: [9, "omnivores"], "snakes": [8, "carnivores"]}
    >>> animal_type(animals)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> animals = {"dogs": ["omnivores", 10], "snakes": ["carnivores", 8], \
    "lions": ["carnivores", 12], "sheep": ["herbavores", 12]}
    >>> animal_type(animals)
    Traceback (most recent call last):
    ...
    AssertionError

    """
    # YOUR CODE GOES HERE #

    # key and value lists from animal dictionary
    animal_keys = list(animals.keys())
    animal_values = list(animals.values())

    # writing assertion checks
    assert type(animals) == dict
    assert all([type(key) == str for key in animal_keys])
    assert all([type(value) == list for value in animal_values])
    assert all(len(value) == 2 for value in animal_values)
    assert all([type(value[0]) == int for value in animal_values])
    assert all([type(value[1]) == str for value in animal_values])
    
    # creating the output variable
    output = [animal[1] for animal in animal_values]

    # returning the output list
    return output


# Question 1.3
def hungry(animals, food, target_energy):
    """
    Iterates through animals and returns a list contaning a tuple of the \
    animal name and the number of units of food it needs to consume, or a \
    string representing it's distaste for the food

    Args:
        animals: a dictionary described in Question 1.2
        food: a tuple with three elements
            <food> is a string of the name of the food that will be given
            <animal_type> is a list that contains strings of the types of \
                          animals that the food would be given to \
                          (case sensitive)
            <gained_energy> is a positive integer representing the energy \
                            level that the animal would gain if they consume \
                            one unit of food
        target_energy: is a positive integer that is the desired energy state \
                       for each animal

    Returns:
        a list that contains tuple(s) of length 2 and/or string(s):
            - if an animal can consume the given food (animal_type matches), \
              append a tuple where the first element is the name of the \
              animal and the second element is the number of units the animal \
              has to consume to meet the target energy state
            - If the animal cannot consume the food, it would be mapped to \
              the string 'dislike :('

    >>> animals = {"dogs": [10, "omnivores"], "snakes": [8, "carnivores"], \
    "lions": [12, "carnivores"], "sheep": [7, "herbivores"]}
    >>> target = 15
    >>> food = ("lettuce", ["omnivores", "herbivores"], 2)
    >>> hungry(animals, food, target)
    [('dogs', 3), 'dislike :(', 'dislike :(', ('sheep', 4)]

    >>> animals = {"dogs": [10, "omnivores"], "snakes": [8, "carnivores"], \
    "lions": [12, "carnivores"], "bears": [5, "omnivores"]}
    >>> target = 15
    >>> food = ("grass", ["herbivores"], 2)
    >>> hungry(animals, food, target)
    ['dislike :(', 'dislike :(', 'dislike :(', 'dislike :(']

    >>> food = ("berries", "herbivores", 2)
    >>> hungry(animals, food, target)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below

    >>> animals = {"dogs": [10, "omnivores"], "snakes": [8, "carnivores"], \
    "lions": [12, "carnivores"], "bears": [5, "omnivores"]}
    >>> target = 15
    >>> food =  ("lettuce", ["Omnivores", "herbivores"], 2)
    >>> hungry(animals, food, target)
    ['dislike :(', 'dislike :(', 'dislike :(', 'dislike :(']

    >>> animals = {"dogs": ["omnivores", 10], "snakes": ["carnivores", 8], \
    "lions": ["carnivores", 12], "sheep": ["herbavores", 12]}
    >>> target = 15
    >>> food = ("lettuce", ["Omnivores", "herbivores"], 2)
    >>> hungry(animals, food, target)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> animals = {"dogs": [10, "omnivores"], "snakes": [8, "carnivores"], \
    "lions": [12, "carnivores"], "bears": [5, "omnivores"]}
    >>> target = 'fifteen'
    >>> food =  ("lettuce", ["Omnivores", "herbivores"], 2)
    >>> hungry(animals, food, target)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    # YOUR CODE GOES HERE #

    # key and value lists from animals dictionary
    animal_keys = list(animals.keys())
    animal_values = list(animals.values())

    # assert statements
    assert type(animals) == dict
    assert all([type(key) == str for key in animal_keys]) 
    assert all([type(value) == list for value in animal_values])
    assert all([len(value) == 2 for value in animal_values])
    assert all([type(value[0]) == int for value in animal_values])
    assert all([type(value[1]) == str for value in animal_values])
    assert type(food) == tuple
    assert len(food) == 3
    assert type(food[0]) == str
    assert type(food[1]) == list
    assert type(food[2]) == int
    assert type(target_energy) == int
    assert target_energy > 0
    
    # creating the output list
    output = [(animal, len([i for i in range(animals[animal][0], \
    target_energy, food[2])])) if animals[animal][1] in food[1] else \
    "dislike :(" for animal in animals]

    # returning output list
    return output


# Question 2
def affordable_arcade_game(arcade_games, budget):
    """
    Iterate through arcade games and return the game with the highest rating \
    and within price range

    Args:
        arcade_games: a dictionary where the keys are the names of the arcade \
                      games, and the values are lists of tupeles. Each tuple \
                      contains two items: the price (an int) of the game and \
                      its rating
        budget: an integer representing your budget for purchasing an arcade \
                game

    Returns:
        the title of the arcade game with the highest rating that is \
        affordable within the given budget. If there is a tie, return the \
        title with the highest alphabetical order

    >>> arcade_games = {'Pac-Man': [(5, 4.7), (10, 4.9)],\
    'Galaga': [(8, 4.8), (12, 4.6)],\
    'Street Fighter II': [(15, 4.9)],\
    'Mortal Kombat': [(12, 4.7), (18, 4.8)],\
    'Donkey Kong': [(10, 4.5), (14, 4.6)]}
    >>> affordable_arcade_game(arcade_games, 10)
    'Pac-Man'
    >>> affordable_arcade_game(arcade_games, 15)
    'Street Fighter II'

    # Add your own doctests below

    >>> affordable_arcade_game(arcade_games, 5)
    'Pac-Man'

    >>> affordable_arcade_game(arcade_games, 8.01)
    'Pac-Man'

    >>> affordable_arcade_game(arcade_games, 7.99)
    'Pac-Man'

    """
    # YOUR CODE GOES HERE #

    # initializng the output of the function
    output = max([(key, detail[1]) for key, value in \
    arcade_games.items() for detail in value if detail if detail[0] <= \
    budget])[0]

    # returning the output
    return output


# Question 3
def calculate_probability_ratio(prizes, probabilities, target_prize):
    """
    Outputs the probability corresponding the the target_prize

    Args:
        prizes: a list of strings of all the prize names
        probabilities: a list of floats, each probabilitiy corresponds to the \
                       corresponding prize at the same index
        target_prize: a string

    Returns:
        the ratio of the probability of winning the target prize to the sum \
        of probabilities of all prizes

    >>> calculate_probability_ratio(["Gold Coin", "Silver Coin", "Gem", \
        "Key"], [0.1, 0.2, 0.3, 0.4], "Gem")
    0.3

    >>> calculate_probability_ratio(["Sword", "Shield", "Bow", "Staff"], \
        [0.25, 0.2, 0.3, 0.25], "Shield")
    0.2

    >>> calculate_probability_ratio(["Coin", "Shield", "Gem"], \
        [0.25, 0.2, 0.5], 0)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below

    >>> calculate_probability_ratio(["Coin", "Shield", "Gem"], \
        [0.25, 0.2], "Gem")
    Traceback (most recent call last):
    ...
    AssertionError

    >>> calculate_probability_ratio([True, "Shield", "Gem"], \
        [0.25, 0.2, 0.5], "Gem")
    Traceback (most recent call last):
    ...
    AssertionError

    >>> calculate_probability_ratio(["Shield", "Gem"], \
        [0.25, 0.2, 0.5], "Gem")
    Traceback (most recent call last):
    ...
    AssertionError
    """
    # YOUR CODE GOES HERE #

    assert type(prizes) == list
    assert all([type(prize) == str for prize in prizes])
    assert type(probabilities) == list
    assert all([type(num) == float for num in probabilities])
    assert len(prizes) == len(probabilities)
    assert type(target_prize) == str
    assert target_prize in prizes
    
    output = [probabilities[i] for i in range(len(prizes)) if prizes[i] == \
    target_prize][0]

    return output


# Question 4
def account(string):
    """
    Takes a string and scrambles it according to certain words

    Args:
        string: an alphanumeric message

    Returns:
        the string account after transforming the input using the following \
        rules:
            - all non-vowel alphabets should be in lowercase
            - all vowels should be uppercase
            - all digits should be moved to the front of the string in order
            - the numeric part of the string should repeat i number of times \
              wher i is the last digit in the input string 

    >>> string = "helloDSC20"
    >>> account(string)
    'hEllOdsc'

    >>> string = "DSC2023python"
    >>> account(string)
    '202320232023dscpythOn'

    >>> string = "hello!! DSC20"
    >>> account(string)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below

    >>> string = "hello!!DSC20"
    >>> account(string)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> string = "hello323"
    >>> account(string)
    '323323323hEllO'

    >>> string = True
    >>> account(string)
    Traceback (most recent call last):
    ...
    AssertionError

    """
    # YOUR CODE GOES HERE #

    # assertion statements
    assert type(string) == str
    assert all([i.isalnum() for i in string])
    
    vowels = "AaEeIiOoUu"

    # creating a string of just alphabetical characters
    chars = "".join([i.upper() if i in vowels else i.lower() for i in string \
    if i.isalpha()])

    # creating a string of just the numbers
    nums = "".join([i for i in string if i.isdigit()])
 
    # number representing the number of times to multiply the num portion of \
    # output
    mult = int(nums[-1])

    # creating the output string
    output = f"{nums * mult}{chars}"

    # returning output string
    return output


# Question 5
def prize_combinations(prizes, target_tickets):
    """
    Iterates over the prizes and outputs the combinations of prizes that are
    equal or less than the number of tickets

    Args:
        prizes: a list of tuples, each tuple contains the prize name as a \
                string and the ticket cost as an integer
        target_tickets: the total amount of tickets you can spend at the \
                        prize booth, which is represented as an integer

    Returns:
        all possible pairs of prizes that can be redeemed without exceeding \
        the target number of tickets (sorted in alphabetical order)

    >>> prizes = [("Plush Toy", 10), ("Board Game", 20), ("Puzzle", 5), \
        ("Remote Control Car", 30)]
    >>> prize_combinations(prizes, 15)
    [('Plush Toy', 'Puzzle'), ('Puzzle', 'Plush Toy')]

    >>> prize_combinations(prizes, 10)
    []

    >>> prize_combinations(prizes, 1.0)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below

    >>> prizes = [("Plush Toy", 10), ("Board Game", 20), ("Puzzle", 5), \
        ("Remote Control Car", 30)]
    >>> prize_combinations(prizes, 50)
    [('Plush Toy', 'Board Game'), ('Plush Toy', 'Puzzle'), \
('Plush Toy', 'Remote Control Car'), ('Board Game', 'Plush Toy'), \
('Board Game', 'Puzzle'), ('Board Game', 'Remote Control Car'), \
('Puzzle', 'Plush Toy'), ('Puzzle', 'Board Game'), \
('Puzzle', 'Remote Control Car'), ('Remote Control Car', 'Plush Toy'), \
('Remote Control Car', 'Board Game'), ('Remote Control Car', 'Puzzle')]

    >>> prizes = [("Plush Toy", 10.3), ("Board Game", 20), ("Puzzle", 5), \
        ("Remote Control Car", 30)]
    >>> prize_combinations(prizes, 15)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> prizes = [(True, 10), ("Board Game", 20), ("Puzzle", 5), \
        ("Remote Control Car", 30)]
    >>> prize_combinations(prizes, 15)
    Traceback (most recent call last):
    ...
    AssertionError

    """
    # YOUR CODE GOES HERE #

    assert type(prizes) == list
    assert all([type(tup) == tuple for tup in prizes])
    assert all([type(tup[0]) == str for tup in prizes])
    assert all([type(tup[1]) == int for tup in prizes])
    assert type(target_tickets) == int

    output = [(i[0], j[0]) for i in prizes for j in prizes if i[1] + \
    j[1] <= target_tickets and i != j]

    return output
    
# Question 6
def manage_inventory(inventory, action, item_name, quantity):
    """
    Updates a given inventory by adding and reducing item quantities 

    Args:
        inventory: a dictionary, wher keys are item names, and values are \
                   quantities (positive integers)
        action: specific operation (represented as a string)
        item_name: item to update (represented as a string)
        quantity: used in action (represented as an integer equal to or more \
                  than 0)

    Returns:
        a dictionary with the updated values. Construct the returned \
        dictionary with a one-line dictionary comprehension

    >>> inventory = {'coins': 100, 'health potions': 5}
    >>> manage_inventory(inventory, 'add', 'coins', 50)
    {'coins': 150, 'health potions': 5}

    >>> manage_inventory(inventory, 'remove', 'health potions', 10)
    {'coins': 100, 'health potions': 5}

    >>> manage_inventory(inventory, 'remove', 'health potions', 3)
    {'coins': 100, 'health potions': 2}

    >>> manage_inventory([], 'remove', 'health potions', 3)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below

    >>> manage_inventory(inventory, 'remove', 'health potions', 6)
    {'coins': 100, 'health potions': 5}

    >>> manage_inventory(inventory, 'add', 'health potions', 6.4)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> inventory = {'coins': 100, True: 10}
    >>> manage_inventory(inventory, 'add', 'coins', 6)
    Traceback (most recent call last):
    ...
    AssertionError

    """
    # YOUR CODE GOES HERE #

    assert type(inventory) == dict 
    assert all([type(key) == str for key in list(inventory.keys())])
    assert all([type(value) == int for value in list(inventory.values())])
    assert all([value > 0 for value in list(inventory.values())])
    assert type(action) == str
    assert type(item_name) == str
    assert type(quantity) == int

    output = {key: value + quantity if item_name == key and action == "add" \
    else value - quantity if item_name == key and action == "remove" and \
    value >= quantity else value for key, value in inventory.items()}

    return output 

# Question 7 Extra Credit
def arcade(games, money):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> games = {"Pac-Man": [(20, 5), (15, 8), (-25, 12)], \
    "Space Invaders": [(-10, 3), (3, 5)], \
    "Street Fighter II": [(10, 2), (5, 8), (10, 7)]}
    >>> money = 5
    >>> arcade(games, money)
    'Street Fighter II'

    >>> money = 10
    >>> arcade(games, money)
    'Pac-Man'

    >>> money = -2
    >>> arcade(games, money)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add your own doctests below
    """
    # YOUR CODE GOES HERE #
    return
