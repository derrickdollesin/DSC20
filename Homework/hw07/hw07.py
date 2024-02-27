"""
DSC 20 Winter 2024 Homework 07
Name: Derrick Dollesin
PID: A18133427
Source: 
"""

# Question 1
def marketplace(start, market_map, directions, spent=0):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> market_map = [
    ... "...............",
    ... ".5_1_7_x___4_7.",
    ... ".x__8_3__2___6.",
    ... "._5_2_87_35__2.",
    ... ".___6___5_8x2_.",
    ... ".2_7_9_44_3_2_.",
    ... "..............."]

    >>> directions = ['U','R','R','U','L','U','L','L']
    >>> marketplace((5,7), market_map, directions)
    15
    >>> marketplace((1,7), market_map, directions)
    'scammed!'

    >>> directions = ['L','L','L','L','L','L','L','L','L','L','L','L']
    >>> marketplace((3,10), market_map, directions)
    30

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #

    # list of available numbers in the map
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # finding the current position on the map
    curr_pos = market_map[start[0]][start[1]]

    # base cases
    if curr_pos == ".": # you've hit an edge
        return spent

    elif curr_pos == "x": # you've been scammed
        return "scammed!"

    elif len(directions) == 0: # you've completed the directions

        # if the last position in a number add to spent
        if curr_pos in nums:
            spent += int(curr_pos)

        return spent
    
    # creating variables for new locations based on directions
    mov_up = (start[0] - 1, start[1])
    mov_down = (start[0] + 1, start[1])
    mov_left = (start[0], start[1] - 1)
    mov_right = (start[0], start[1] + 1)

    # finding the current direction you are heading
    curr_dir = directions[0]

    # conditions for current direction
    if curr_dir == "U": # going up

        # checking if the current position is a number and adding it to spent
        if curr_pos in nums:
            spend = spent + int(curr_pos)
        else:
            spend = spent

        # getting the remaining directions recursively
        remaining = marketplace(mov_up, market_map, directions[1:], \
        spent=spend)

        # returning the remaining
        return remaining

    elif curr_dir == "D":

        # checking if the current position is a number and adding it to spent
        if curr_pos in nums:
            spend = spent + int(curr_pos)
        else:
            spend = spent

        # getting the remaining directions recursively
        remaining = marketplace(mov_down, market_map, directions[1:], \
        spent=spend)

        # returning the remaining
        return remaining

    elif curr_dir == "L":

        # checking if the current position is a number and adding it to spent
        if curr_pos in nums:
            spend = spent + int(curr_pos)
        else:
            spend = spent

        # getting the remaining directions recursively
        remaining = marketplace(mov_left, market_map, directions[1:], \
        spent=spend)

        # returning the remaining
        return remaining

    elif curr_dir == "R":

        # checking if the current position is a number and adding it to spent
        if curr_pos in nums:
            spend = spent + int(curr_pos)
        else:
            spend = spent

        # getting the remaining directions recursively
        remaining = marketplace(mov_right, market_map, directions[1:], \
        spent=spend)

        # returning the remaining
        return remaining
        

# Question 2  (EXTRA CREDIT)
def palindromes(word):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> palindromes("aaa")
    3
    >>> palindromes("abcba")
    2
    >>> palindromes("ababaa")
    5

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return


# Question 3
def doctests_q3():
    """
    >>> event = EventTracker(2)
    >>> date = "2-20-2024"
    >>> event.months_left(date)
    '0 months left to midterm.'
    
    >>> EventTracker.change_event("final")
    >>> event.change_event_month(6)
    >>> event.months_left(date)
    '4 months left to final.'

    >>> event.change_event_month(1)
    >>> event.months_left(date)
    'You missed final.'

    >>> event = EventTracker(7)
    >>> EventTracker.change_event("4th of July")
    >>> date = "5-24-2024"
    >>> event.months_left(date)
    '2 months left to 4th of July.'
    >>> date = "12-24-2024"
    >>> event.months_left(date)
    'You missed 4th of July.'

    # Add your own doctests below for better testing, although not required.
    """
    return

class EventTracker:
    event = 'TODO'

    def __init__(self, event_month):
        pass

    #@ TODO: what kind of method is it?
    def change_event(cls, new_event):
        pass

    #@ TODO: what kind of method is it?
    def extract_month(date):
        pass

    def months_left(self, date):
        pass

    def change_event_month(self, new_month):
        pass


# Question 4
def doctests_q4():
    """
    >>> n1 = Notebook("My encounters", "Marina", 12, \
    {'people': [], 'animals': []})
    >>> n1.description
    'This notebook is to keep track of encountered people and animals.'
    >>> n1.title
    'My encounters'
    >>> n1.author
    'Marina'
    >>> n1.tip
    12
    >>> n1.get_people()
    []
    >>> n1.new_encounter('people', 'tutors')
    True
    >>> n1.new_encounter('animals', 'recursive dragon')
    True
    >>> n1.new_encounter('people', 'tutors')
    'Already encountered'
    >>> n1.new_encounter('animals', 'baby pandas')
    True
    >>> n1.encounters
    {'people': ['tutors'], 'animals': ['recursive dragon', 'baby pandas']}
    >>> n1.get_people()
    ['tutors']
    >>> n1.get_animals()
    ['recursive dragon', 'baby pandas']
    >>> n1.info()
    "Marina has spent 12 months in Pythonia and has encountered 1 people and \
2 animals. These are noted in 'My encounters'."

    >>> n2 = Notebook("Encounters", "Noto", 1, \
    {'people': ['Ben', 'Matilda', 'Charisse'], 'animals': ['cat']})
    >>> n2.get_people()
    ['Ben', 'Matilda', 'Charisse']
    >>> Notebook.edit_description()
    'This notebook only has 1 purpose - there is no need to modify its \
description!'

    # Add your own doctests below for better nesting, although not required.
    """
    return

class Notebook:
    """
    Implementation of Notebook
    """
    # YOUR CODE GOES HERE #
    pass


# Question 5
def doctests_q5():
    """
    >>> shoem = Merchant('shoemaker', {'boots': [5, 10], 'sandals': \
    [2, 3], 'heels': [1, 20]}, 100, ['Pythonia', 'Garthon'])
    >>> print(shoem)
    shoemaker has brought boots, sandals, heels. \
They are able to sell their wares in Pythonia, Garthon.
    >>> shoem.get_type()
    'shoemaker'
    >>> shoem.get_stock()
    {'boots': [5, 10], 'sandals': [2, 3], 'heels': [1, 20]}
    >>> shoem.get_cash()
    100
    >>> shoem.get_kingdom_licenses()
    ['Pythonia', 'Garthon']
    >>> shoem.sell('boots', 2)
    'shoemaker sold 2 of boots.'
    >>> shoem.get_stock()
    {'boots': [3, 10], 'sandals': [2, 3], 'heels': [1, 20]}
    >>> shoem.get_cash()
    120
    >>> shoem.restock('heels', 4)
    'shoemaker restocked 4 of heels.'
    >>> shoem.get_stock()
    {'boots': [3, 10], 'sandals': [2, 3], 'heels': [5, 20]}
    >>> shoem.travel_to_kingdom('Pythonia')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> pythonia = Kingdom('Pythonia')
    >>> shoem.travel_to_kingdom(pythonia)
    True
    >>> javatown = Kingdom('Javatown')
    >>> shoem.travel_to_kingdom(javatown)
    False
    >>> pythonia.get_name()
    'Pythonia'
    >>> assert isinstance(pythonia.get_curr_merchants(), list)
    >>> assert [isinstance(m, Merchant) for m in pythonia.get_curr_merchants()]
    >>> print(pythonia)
    Kingdom Pythonia has 1 active merchants.
    >>> blacksmith = Merchant('Blacksmith', {'hammers': [25, 5], \
    'nails': [90, 1]}, 10, ['Pythonia'])
    >>> blacksmith.get_id()
    2
    >>> pythonia.new_merchant(blacksmith)
    True
    >>> pythonia.get_total_cash()
    130

    >>> print(pythonia.promote_market())
    shoemaker sold 3 of boots. 
    shoemaker sold 2 of sandals. 
    shoemaker sold 5 of heels. 
    Blacksmith sold 25 of hammers. 
    Blacksmith sold 90 of nails. 
    <BLANKLINE>

    >>> len(pythonia.get_curr_merchants())
    2
    >>> pythonia.temp_ban(blacksmith)
    True
    >>> tailor = Merchant('tailor', {}, 10000, ['Pythonia'])
    >>> pythonia.temp_ban(tailor)
    False
    >>> len(pythonia.get_curr_merchants())
    1

    # Add your own doctests below
    """

class Merchant:
    """
    Implementation of a merchant
    """

    # TODO: Add class attribute(s) here

    def __init__(
        self, merchant_type, stock, cash, kingdom_licenses
    ):
        """
        Constructor of Merchant

        Parameters:
        merchant_type (str): type of the merchant
        stock (dict): dictionary containing the merchant's products
        cash (int): amount of money the merchant has
        kingdom_licenses (list): list of kingdoms the merchant can sell in
        """
        # YOUR CODE GOES HERE #
        pass

    def get_type(self):
        """ Getter for name attribute """
        # YOUR CODE GOES HERE #
        pass

    def get_stock(self):
        """ Getter for the stock attribute """
        # YOUR CODE GOES HERE #
        pass

    def get_cash(self):
        """ Getter for cash attribute """
        # YOUR CODE GOES HERE #
        pass

    def get_kingdom_licenses(self):
        """ Getter for kingdom_licenses attribute """
        # YOUR CODE GOES HERE #
        pass
    
    def get_id(self):
        """ Getter for id attribute """
        # YOUR CODE GOES HERE #
        pass

    def __str__(self):
        """ String representation of Merchant """
        # YOUR CODE GOES HERE #
        pass

    def sell(self, product, count):
        """
        Updates merchant's cash and product amount when a sale is completed
        """
        # YOUR CODE GOES HERE #
        pass

    def restock(self, product, count):
        """
        Adds more product to the Merchant's stock for them to sell
        """
        # YOUR CODE GOES HERE #
        pass

    def travel_to_kingdom(self, kingdom):
        """
        Returns a boolean indicating whether the merchant can travel to the 
        specified kingdom
        """
        # YOUR CODE GOES HERE #
        pass


class Kingdom:
    """
    Implementation of a kingdom
    """

    # TODO: Add class attribute(s) here

    def __init__(self, name):
        """
        Constructor of Kingdom
        
        Parameters:
        name (str): name of the kingdom
        """
        # YOUR CODE GOES HERE #
        pass

    def get_name(self):
        """ Getter of Kingdom's name """
        # YOUR CODE GOES HERE #
        pass

    def get_curr_merchants(self):
        """ Getter of current active merchants """
        # YOUR CODE GOES HERE #
        pass

    def __str__(self):
        """ String representation of the kingdom """
        # YOUR CODE GOES HERE #
        pass
    
    def new_merchant(self, merchant):
        """
        Adds a new merchant to the kingdom
        """
        # YOUR CODE GOES HERE #
        pass
       
    def temp_ban(self, merchant):
        """
        Temporarilty bans a certain merchant
        """
        # YOUR CODE GOES HERE #
        pass

    def get_total_cash(self):
        """
        Returns the total amount of cash the merchants have
        """
        # YOUR CODE GOES HERE #
        pass

    def promote_market(self):
        """
        Sell out every market in the kingdom
        """
        # YOUR CODE GOES HERE #
        pass
