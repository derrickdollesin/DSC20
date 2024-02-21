"""
DSC 20 Winter 2024 Homework 06
Name: Derrick Dollesin
PID: A18133427
Source: 
"""

#Question 1
def reverse_str(name):
    """
    Reverses any input name through recursion.

    Args:
        name: a string representing some name

    Returns:
        the input name reversed

    >>> reverse_str('Lina')
    'aniL'
    >>> reverse_str('anna')
    'anna'
    >>> reverse_str('Hello World')
    'dlroW olleH'

    # Add your own doctests below

    >>> reverse_str('')
    ''
    >>> reverse_str(' ')
    ' '
    >>> reverse_str('<*><4><?><!>')
    '>!<>?<>4<>*<'

    """

    # return just the name if the input is a single character
    if len(name) == 1:
        return name

    # return an empty string if the name is empty
    elif len(name) == 0:
        return ""

    # recursively return the last element of each string
    else:
        return name[-1] + reverse_str(name[:-1]) 

#Question 2
def reverse_all(names_lst):
    """
    Iterates over a list of names and returns a list of each name reveresed

    Args:
        names_lst: a list of strings

    Returns:
        a list with where each element is a reversed string

    >>> names_lst = ["Emma", "Liam", "Olivia", "Noah", "Ava"]
    >>> reverse_all(names_lst)
    ['ammE', 'maiL', 'aivilO', 'haoN', 'avA']
    >>> names_lst = ["William"]
    >>> reverse_all(names_lst)
    ['mailliW']
    >>> names_lst = ["Isabella", "Oliver", "Mia"]
    >>> reverse_all(names_lst)
    ['allebasI', 'revilO', 'aiM']

    # Add your own doctests below

    >>> names_lst = ['ammE', 'maiL', 'aivilO', 'haoN', 'avA']
    >>> reverse_all(names_lst)
    ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava']
    >>> names_lst = ['?!?', '!?!']
    >>> reverse_all(names_lst)
    ['?!?', '!?!']
    >>> names_lst = ['racecar', 'tacocat']
    >>> reverse_all(names_lst)
    ['racecar', 'tacocat']

    """

    # returns empty list if input is empty
    if not names_lst:
        return []

    # reverse the first element of the list and recurse the function starting \
    # at the next index of the list
    else:
         return [reverse_str(names_lst[0])] + reverse_all(names_lst[1:])

#Question 3
def num_tables(total_ppl, table_size=4):
    """
    Outputs the number of tables required for a total number of people and the 
    number of people that can sit at one table

    Args:
        total_ppl (non-negative integer): total number of people coming
        table_size (positive integer): table size, by default set at 4

    Returns:
        an integer as the number of tables you would like to use

    >>> num_tables(35)
    9
    >>> num_tables(20, 2)
    10
    >>> num_tables(2, 20)
    1

    # Add your own doctests below

    >>> num_tables(0)
    0
    >>> num_tables(16, 16)
    1
    >>> num_tables(1090, 10)
    109

    """

    # if there is no one coming return 0
    if not total_ppl:
        return 0
    # return 1 if there are less people coming than table_size
    elif total_ppl <= table_size:
        return 1
    # return 1 for every table needed to fit the total_ppl
    else:
        return 1 + num_tables(total_ppl - table_size, table_size)

#Question 4
def orders(price_lst, order_size=3):
    """
    Outputs a list where each price is grouped into a designated order and 
    each order is summed

    Args:
        price_lst (list of positive integers): the prices of each item that you
                                               purchase
        order_size (postive integer): size of each order, be default set to 3

    Returns:
        a list taht contains the total cost of each order

    >>> orders([2, 2, 2, 4, 4, 4])
    [6, 12]
    >>> orders([])
    []
    >>> orders([2, 2, 2, 2])
    [6, 2]

    # Add your own doctests below

    >>> orders([0, 0, 0, 0, 0])
    [0, 0]
    >>> orders([2, 2, 2, 2, 2, 2, 2, 2, 2], 2)
    [4, 4, 4, 4, 2]
    >>> orders([1, 2, 3, 4, 5, 6], 1)
    [1, 2, 3, 4, 5, 6]

    """
    # return empty list if price lst is empty
    if not price_lst:
        return []

    # returns the sum of the first order and recurses through the rest of the \
    # orders
    else:
        return [sum(price_lst[0:order_size])] + orders(price_lst[order_size:],\
        order_size)


#Question 5
def confuse(reminder_str):
    """
    If there are two repeated characters in a string replace the second with *

    Args:
        reminder_str: a string

    Returns:
        string with the second duplicate character in a row replaced by a *

    >>> confuse('book')
    'bo*k'
    >>> confuse('successful')
    'suc*es*ful'
    >>> confuse('')
    ''

    # Add your own doctests below

    >>> confuse("yellowwooddoor")
    'yel*ow*o*d*o*r'
    >>> confuse("foOl")
    'foOl'
    >>> confuse("therearenorepeatedlettersjkthereisone")
    'therearenorepeatedlet*ersjkthereisone'

    """

    # returns just the input if it's length is one or less since there can't
    # be any repeated characters
    if len(reminder_str) <= 1:
        return reminder_str

    # returns the second repeated character as a * and repeats the code
    elif reminder_str[0] == reminder_str[1]:
        return reminder_str[0] + "*" + confuse(reminder_str[2:])

    # if there is not a repeated character add the character and keep running
    else:
        return reminder_str[0] + confuse(reminder_str[1:])


#Question 6
def seating_chart(group_sizes, table_sizes):
    """
    Determines how many more tables are needed to fit every group

    Args:
        group_sizes: a list of integers, where every integer represents the 
                     size of a group
        tables_sizes: a list of intergers, where every integer represents the 
                      total number of seats at the tables

    Returns:
        the number of groups that are assigned to a table that does not have
        enough seats for everyone at the table

    >>> seating_chart([3, 3, 3], [4, 4, 4])
    0
    >>> seating_chart([2, 3, 4, 5], [3, 3, 3])
    2
    >>> seating_chart([2, 2], [])
    2

    # Add your own doctests below

    >>> seating_chart([5, 4, 3], [5, 4, 3])
    0
    >>> seating_chart([5, 10], [6, 3])
    1
    >>> seating_chart([1, 1, 1, 1], [1, 1, 1, 1])
    0

    """
    if not group_sizes:
        return 0 

    group_size = group_sizes[0]

    for table_size in table_sizes:
        if group_size <= table_size:
            return seating_chart(group_sizes[1:], table_sizes)

    return 1 + seating_chart(group_sizes[1:], table_sizes)

#Question 7

def allergens(ingredients, item_to_remove):
    """
    Removes ingredients from a list and creates a new list of the items in 
    the reveres order

    Args:
        ingredients: a list of strings
        item_to_remove: a string that needs to be removed from ingredients

    Returns:
        a new list wher all occurences of items_to_remove are removed (case \
        sensitive) and the list is in the reveresed order

    >>> allergens(["Sugar", "Jam", "Honey", "Honey"], "Honey")
    ['Jam', 'Sugar']
    >>> allergens(["Kefir", "", "Juice", "Water", "Milk"], "milk")
    ['Water', 'Juice', '', 'Kefir']
    >>> allergens(["Pecans", "PECANS", "PeCANS"], "Pecans")
    []
 
    # Add your own doctests below

    >>> allergens([], '')
    []
    >>> allergens(["", "", ""], " ")
    ['', '', '']
    >>> allergens(["pickles", "p!ckles"], 'p!ckles')
    ['pickles']
    

    """
    if not ingredients:
        return []
    
    elif ingredients[0].lower() == item_to_remove.lower():
        return allergens(ingredients[1:], item_to_remove)

    else:
        return allergens(ingredients[1:], item_to_remove) + [ingredients[0]]
