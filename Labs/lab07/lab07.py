"""
DSC 20 Winter 2024, Lab 07
Name: TODO
PID: TODO
Source: TODO
"""

# Question 1.1
def max_recursion(lst):
    """
    Find the maximum element in a list recursively.

    Args:
        lst (list): a list of integers
    Returns:
        The maximum number

    >>> max_recursion([1, 2, 3, 4])
    4
    >>> max_recursion([3, 2, 4, 2])
    4
    >>> max_recursion([6, 7, 8, 2, 5])
    8
    """
    # YOUR CODE GOES HERE #
    return



# Question 1.2
def oldest_dragon(all_dragons):
    """
    A recursive function that takes a non-empty list of tuples and returns
    the tuple with the oldest dragon.

    Args:
        all_dragons (list): a list of tuples representing dragon info
    Returns:
        the oldest dragon tuple

    >>> oldest_dragon([('Skakmat', 10)])
    ('Skakmat', 10)
    >>> oldest_dragon([('Skakmat', 5), ('Alduin', 17)])
    ('Alduin', 17)
    >>> oldest_dragon([('Skakmat', 17), ('Alduin', 17)])
    ('Skakmat', 17)
    """
    # YOUR CODE GOES HERE #
    return



# Question 2
def dragon_count(dragons):
    """
    Recursively akes a list of dragon names and return a dictionary recording
    the frequency of each dragon name.

    Args:
        dragons (list):  a list of dragon names
    Returns:
        a dictionary of dragon frequency

    >>> out = dragon_count(['Alduin', 'Alduin', 'Skakmat'])
    >>> out = dict(sorted(out.items()))
    >>> out == {'Alduin': 2, 'Skakmat': 1}
    True
    >>> dragon_count([])
    {}
    """
    # YOUR CODE GOES HERE #
    return


# Question 3
def send_invitations(all_dragons, my_choices):
    """
    Recursion function that takes a tuple of all dragons that want to meet you
    and another tuple of dragons that you wish to invite. Return a list with
    unique names of dragons that you wish to invite and who want to see you
    as well.

    Args:
        all_dragons (list): a list of all dragon names that want to meet you
        my_choices (list): a list of dragon names that will be invited
    Returns:
        a list of unique dragon names in both input lists.

    >>> all_dragons = ['Skakmat', 'Alduin', 'Skakmat', 'Dracora', 'Dracar']
    >>> send_invitations(all_dragons, [])
    []

    >>> send_invitations(all_dragons, ['Alduin'])
    ['Alduin']

    >>> all_dragons = ["Dracora", "Dracar", "Dracar", "Alduin", "Pyrion"]
    >>> sorted(send_invitations(all_dragons, ["Dracar", "Dracar", "Pyrion"]))
    ['Dracar', 'Pyrion']

    >>> sorted(send_invitations(all_dragons, ["Pyrion", "Dracar", "Talonx"]))
    ['Dracar', 'Pyrion']
    """
    # YOUR CODE GOES HERE #
    return


# Question 4
def rsvp(string, sub, i=0, j=0):
    """
    Recursive function that checks if dragons' responses contain a specific
    substring.

    Args:
        string (str): the input string
        sub (str): the target substring
        i (int): index for starting the search
        j (int): index through the substring
    Returns:
       A boolean value indicating whether the substring is found

    >>> rsvp('yes, will be there', 'yes')
    True
    >>> rsvp('no, sorry', 'yes')
    False
    >>> rsvp('yep, will be there', 'yes')
    False
    """
    # YOUR CODE GOES HERE #
    return



class Dragon:
    """
    Class that creates a dragon object.

    >>> dragon1 = Dragon('Skakmat', ['Hun', 'Vah', 'Koor'])
    >>> Dragon.greeting
    'I arrived from the land of recursion!'
    >>> dragon1.shout(2)
    'Hun-Vah'
    >>> dragon1.energy
    500
    >>> dragon1.add_new_word('Lok')
    >>> dragon1.vocabulary
    ['Lok', 'Hun', 'Vah', 'Koor']
    >>> dragon1.shout(3)
    'Lok-Hun-Vah'
    >>> dragon1.shout(1)
    False

    >>> dragon2 = Dragon('Pyrion', [])
    >>> Dragon.greeting
    'I arrived from the land of recursion!'
    >>> dragon2.shout(1)
    ''
    """

    greeting = '*****'

    def __init__(self, name, *****):
        """
        constructor of Dragon
        Args:
            name (str): dragon name
            vocabulary (list): a list of dragon vocabulary

        """
        self.***** = *****
        self.***** = *****
        self.energy = *****

    def shout(*****, amount):
        """
        The shout action of dragons

        Args:
            amount(int): the amount of words to shout
        """
        # TODO: Implement this method
        return

    def add_new_word(*****, *****):
        """
        add a new word at the beginning of vocacbulary
        Args:
            word (str): the word to add
        """
        self.vocabulary = *****
