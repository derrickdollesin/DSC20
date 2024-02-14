"""
DSC 20 Winter 2024 Homework 01
Name: Derrick Dollesin
PID: A18133427
Source: https://www.w3schools.com/python/python_howto_reverse_string.asp,
https://www.geeksforgeeks.org/python-get-unique-values-list/
"""
# Question 1.1

def helper_distance(coord1, coord2):
    """
    Returns the distance between two points 

    Args:
        coord1: list of strings representing the coordinates of 
                a single point
        coord2: list of strings representing the coordinates of 
                a single point

    Returns:
        Euclidean distance (as a float) between two given points

    >>> helper_distance(['1', '2'], ['4', '6'])
    5.0
    >>> round(helper_distance(['3', '2'], ['40', '6']), 3)
    37.216

    # Add your own doctests below

    >>> helper_distance(['1', '3'], ['1', '3'])
    0.0

    >>> round(helper_distance(['4', '2'], ['-3', '1']), 3)
    7.071

    >>> round(helper_distance(['-2', '-3'], ['4', '1']), 3)
    7.211

    """
    # YOUR CODE GOES HERE #

    # convert string coordinates to integer coordinates
    x1, x2 = int(coord1[0]), int(coord2[0])
    y1, y2 = int(coord1[1]), int(coord2[1])

    # computing distance between the two points using distance formula
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1/2)

    # return distance between the two coordinates 
    return distance

# Question 1.2
def safe_location(your_loc, safe_loc, jump_length):
    """
    Compares the distance between a safe location and your location. Outputs
    a message if the jump succeeds. 

    Args:
        your_loc: your coordinates as a string
        safe_loc: coordinates of a safe place to jump as a string
        jump_length: non-negatice integer which determines the jump length

    Returns:
        a message according to if the distance between two the locations is 
        greater than a jump length 

    >>> your_loc = "1, 2"
    >>> safe_loc = "4, 6"
    >>> ans = safe_location(your_loc, safe_loc, 10)
    >>> print(ans)
    Nice jump!
    You are safe to continue.


    >>> your_loc = "3, 2"
    >>> safe_loc = "40, 6"
    >>> ans = safe_location(your_loc, safe_loc, 15)
    >>> print(ans)
    You are sent back home.
    
    # Add your own doctests below

    >>> your_loc = "4, 2"
    >>> safe_loc = "-3, 1"
    >>> ans = safe_location(your_loc, safe_loc, 8)
    >>> print(ans)
    Nice jump!
    You are safe to continue.

    >>> your_loc = "-2, -3"
    >>> safe_loc = "4, 1"
    >>> ans = safe_location(your_loc, safe_loc, 7)
    >>> print(ans)
    You are sent back home.

    >>> your_loc = "0, 0"
    >>> safe_loc = "0, 0"
    >>> ans = safe_location(your_loc, safe_loc, 0)
    >>> print(ans)
    Nice jump!
    You are safe to continue.


    """
    # YOUR CODE GOES HERE #

    # converting strings to a list
    your_loc_list = your_loc.split(", ")
    safe_loc_list = safe_loc.split(", ")
    
    # convert string to individual characters to coordinates
    y_loc_x, y_loc_y = your_loc_list[0], your_loc_list[1]
    s_loc_x, s_loc_y = safe_loc_list[0], safe_loc_list[1]

    # your location and safe location as coordinates
    y_loc = [y_loc_x, y_loc_y]
    s_loc = [s_loc_x, s_loc_y]

    # finding the distance between the two locations
    distance = helper_distance(y_loc, s_loc)

    # comparing the distance to jump length and returning a message 
    if distance > jump_length:
        return "You are sent back home."
    else:
        return "Nice jump!\nYou are safe to continue."


# Question 2.1
def first_pattern(repeat, symbol):
    """
    Outputs a symbol repeating a certain number of times according to the
    integer repeat

    Args:
        repeat: a positive integer representing a number of repetitions
        symbol: a single character (possibly empty)
    
    Returns:
        a string of one symbol repeated a number of times

    >>> first_pattern(3, '*')
    '***'
    >>> first_pattern(6, '$')
    '$$$$$$'

    # Add your own doctests below

    >>> first_pattern(7, '!')
    '!!!!!!!'

    >>> first_pattern(3, ',')
    ',,,'

    >>> first_pattern(4, '4')
    '4444'

    """
    # YOUR CODE GOES HERE #

    # making a string of multiple symbols
    symbol_string = symbol * repeat

    return symbol_string
    


# Question 2.2
def second_pattern(repeat, symbol, word, repeat_again):
    """
    Outputs a patterned message in reverse order

    Args:
        repeat: a positive integer representing a number of repetitions
        symbol: a single character (possibly empty)
        word: a string (possibly empty)
        repeat_again: a positive integer (possibly empty)

    Returns:
        a string where a symbol is repeated repeat number of times, then word
        is attached, the symbol is repeated repeat_again number of times and
        in reverse order

    >>> second_pattern(3, '*', 'pattern', 2)
    '**nrettap***'
    >>> second_pattern(6, '$', 'journey', 3)
    '$$$yenruoj$$$$$$'
    >>> second_pattern(3, '', '', 2)
    ''

    # Add your own doctests below

    >>> second_pattern(4, '4', 'four', 4)
    '4444ruof4444'

    >>> second_pattern(10, '~', 'racecar', 3)
    '~~~racecar~~~~~~~~~~'

    >>> second_pattern(1, 'a', 'aaa', 3)
    'aaaaaaa'

    """
    # YOUR CODE GOES HERE #

    # creating the patterns
    f_pattern = first_pattern(repeat, symbol) 
    s_pattern = first_pattern(repeat_again, symbol)

    # steps
    step = -1

    # reversing the word
    reverse_word = word[::step]

    # return the full message
    return s_pattern + reverse_word + f_pattern

# Question 2.3
def third_pattern(word, switch):
    """
    Outputs a patterned message according to the boolean value of switch

    Args:
        word: a string (might be empty) 
        switch: a boolean

    Returns:
        if the switch is True, return a string where the word is repeated three
        times: first time in capitals, then lowercase and then capital letters 
        again
        if the switch is False, return a string where the word is repeated
        three
        times: first time in lowercase, then captials and then lowercase
        letters again 

    >>> third_pattern("trip", True)
    'TRIPtripTRIP'
    >>> third_pattern("dangerous", False)
    'dangerousDANGEROUSdangerous'

    # Add your own doctests below

    >>> third_pattern("", False)
    ''

    >>> third_pattern('3', True)
    '333'

    >>> third_pattern('superbigwordlikethis', True)
    'SUPERBIGWORDLIKETHISsuperbigwordlikethisSUPERBIGWORDLIKETHIS'

    """
    # YOUR CODE GOES HERE #

    # creating an upper and lower cases of the word
    upper_word = word.upper()
    lower_word = word.lower()

    # creating the patterns
    false_pattern = lower_word + upper_word + lower_word
    true_pattern = upper_word + lower_word + upper_word

    # determine which messsage to send according to the value of switch
    if switch is True:
        return true_pattern
    elif switch is False:
        return false_pattern

    
    
# Question 2.4
def fourth_pattern(symbols, repeats, switch):
    """
    Outputs a patterned message according to the given arguments 

    Args:
        symbols: a list of symbols (as characters)
        repeats: a list of repetitions (as positive integers)
        switch: a boolean

    Returns:
        a string containing characters from the symbols list repeated the 
        corresponding numbers of times if the boolean parameter is True, and 
        reversed if otherwise

    >>> fourth_pattern(['-', '+'], [4, 5], True)
    '----+++++'
    >>> fourth_pattern(['-', '+'], [4, 5],  False)
    '+++++----'

    >>> fourth_pattern([], [],  False)
    ''

    # Add your own doctests below

    >>> fourth_pattern(['4', '5'], [4, 5],  False)
    '555554444'

    >>> fourth_pattern(['!', '?'], [1, 2],  False)
    '??!'

    >>> fourth_pattern(['!', '?', '&'], [1, 2, 3],  True)
    '!??&&&'

    """
    # YOUR CODE GOES HERE #
    
    # returning an empty string if both lists are empty
    if symbols == [] and repeats == []:
        return ""

    # using a temp list to store patterns
    patterns = []

    # appending the patterns to temp
    for i in range(len(symbols)):
        patterns.append(symbols[i] * repeats[i])

    # joining the patterns into one big pattern string
    pattern = "".join(patterns)

    # steps
    step = -1 

    if switch is True:
        return pattern
    else:
        return pattern[::step]


# Question 3
def shortest_bridge(bridge1, bridge2, bridge3):
    """
    Outputs the bridge with the shortest description

    Args:
        bridge1: a string describing bridge 1
        bridge2: a string describing bridge 2
        bridge3: a string describing bridge 3

    Returns:
        'bridge1' if the description of bridge1 is shorter or equal to bridge2
        'bridge2' if the description of bridge2 is shorter or equal to bridge3
        'bridge3' if it's description is the shortest


    >>> shortest_bridge("flame","deep river", "flower")
    'bridge1'
    >>> shortest_bridge("hot flames","river", "flower")
    'bridge2'
    >>> shortest_bridge("flame","river", "calm and green")
    'bridge1'
    >>> shortest_bridge("very dangerous","deep river", "red flower")
    'bridge2'

    # Add your own doctests below

    >>> shortest_bridge("","", "")
    'bridge1'

    >>> shortest_bridge("long","wide", "big")
    'bridge3'

    >>> shortest_bridge(" ","", "")
    'bridge2'

    """
    # YOUR CODE GOES HERE #
    
    # finding the length of each description 
    bridge_1 = len(bridge1)
    bridge_2 = len(bridge2)
    bridge_3 = len(bridge3)

    # comparing the len of each description to determine output
    if bridge_1 <= bridge_2 and bridge_1 <= bridge_3:
        return 'bridge1'
    elif bridge_2 <= bridge_3:
        return 'bridge2'
    else: 
        return 'bridge3'


# Question 4.1
def average_without_min_max(people):
    """
    Outputs the average number of people excluding the minimum and maximum 
    values in the list

    Args:
        people: a list of a number of people who crossed a bridge

    Returns:
        the average of the list without adding the minimum or maximum value.
        0.0 if the length of people is less than or equal to two

    >>> average_without_min_max([10, 10, 1, 16])
    10.0
    >>> average_without_min_max([2, 4, 10, 7, 9])
    6.67
    >>> average_without_min_max([2, 0, 10, 5])
    3.5

    # Add your own doctests below

    >>> average_without_min_max([])
    0.0

    >>> average_without_min_max([2, 0])
    0.0

    >>> average_without_min_max([100, 200, 300, 300, 100, 200])
    200.0

    """
    # YOUR CODE GOES HERE #

    # minimum people length
    minimum = 2

    # end value in list
    end = -1

    # sorting the list
    sorted_people = sorted(people)
    
    # checking if the length of the list is two or less
    if len(people) <= minimum:
        return 0.0
    else:
        # finding the average
        average = sum(sorted_people[1:end]) / len(sorted_people[1:end])

        return round(average, minimum)




# Question 4.2
def best_average_bridge(people, bridges):
    """
    Outputs the bridge with the highest average number of people crossing

    Args:
        people: list of lists where each list represents different bridges and
        the number of people who've crossed it
        bridges: list of names of bridges corresponding to list of people

    Returns:
        bridge with highest average that appears first, if there is a tie -
        "No bridges to choose from", if bridges is an empty list -
        the first route if all bridges have average rating 0.0

    >>> ratings = [[1, 10, 5], [4, 6, 9]]
    >>> names = ["flames", "river"]
    >>> best_average_bridge(ratings, names)
    'river'

    >>> ratings = [[6, 10, 5, 3, 8], [10, 10, 9], [6, 6, 90]]
    >>> names = ["flames", "flower", "river"]
    >>> best_average_bridge(ratings, names)
    'flower'

    >>> ratings = [[], [], []]
    >>> names = ["flames", "flower", "river"]
    >>> best_average_bridge(ratings, names)
    'flames'

    >>> best_average_bridge([], [])
    'No bridges to choose from'

    # Add your own doctests below

    >>> ratings = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
    >>> names = ["flames", "flower", "river", 'mountain', 'valley']
    >>> best_average_bridge(ratings, names)
    'flames'

    >>> ratings = [[1, 2, 3], [4, 6, 13, 5], [4, 6, 13, 5]]
    >>> names = ["flames", "flower", "river"]
    >>> best_average_bridge(ratings, names)
    'flower'

    >>> ratings = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 5, 3]]
    >>> names = ["flames", "flower", "river", 'mountain', 'valley']
    >>> best_average_bridge(ratings, names)
    'valley'
    """
    # YOUR CODE GOES HERE #
    
    # need a temp list to store avg values
    avg_list = []

    # return message if there are no bridges in the list
    if len(bridges) == 0:
        return "No bridges to choose from"

    # finding the average num of people crossing each bridge and storing in 
    # list
    for i in people:
            avg_list.append(average_without_min_max(i))

    # will return index of max avg or index of first max avg if tie
    highest_avg = avg_list.index(max(avg_list)) 

    # if only one unique value in temp and it's 0.0 return the first route 
    if list(set(avg_list)) == 1 and avg_list[0] == 0.0:
        return bridges[0]
    # returns the bridge with highest avg
    else:
        return bridges[highest_avg]



# Question 5
def sleepy_vs_awake(flowers):
    """
    Iterates through a list of flowers and returns the most common flower 
    between Sleeprose and Awakentia

    Args:
        flowers: list of flower names as strings

    Returns:
        'Awakentia' if there are more Awakentia type in the list
        'Sleeperose' if there are more Sleeperose type in the list
        True, if there is a tie and the number of these flowers are positive
        False, if none of these flowers appear

    >>> sleepy_vs_awake(["Sleeperose", "Rose", "Sleeperose"])
    'Sleeperose'
    >>> sleepy_vs_awake(["Sleeperose", "Awakentia", "rose"])
    True
    >>> sleepy_vs_awake(["rose", "sleeperose", "awakentia", "daisy"])
    False
    >>> sleepy_vs_awake(["rose", "sleeperose", "Awakentia", "daisy"])
    'Awakentia'

    # Add your own doctests below

    >>> sleepy_vs_awake([])
    False

    >>> sleepy_vs_awake(['Sleeperose', 'Awakentia'])
    True

    >>> sleepy_vs_awake(["Sleeperose", "Sleeperose", "sleeperose", \
    "Awakentia", "awakentia", 'awakentia'])
    'Sleeperose'
    """
    # YOUR CODE GOES HERE #
    
    # count per flower
    awakentia = 0
    sleeperose = 0

    # iterate through flowers and count number of occurences 
    for flower in flowers:
        if flower == 'Awakentia':
            awakentia += 1
        elif flower == 'Sleeperose':
            sleeperose += 1

    # determine output 
    if awakentia > sleeperose:
        return "Awakentia"
    elif sleeperose > awakentia:
        return "Sleeperose"
    elif awakentia == sleeperose and (awakentia + sleeperose) > 0:
        return True
    else:
        return False


# Question 6
def sign(bridge_type, hint, your_name):
    """
    Outputs a message warning travelers about the bridges

    Args:
        bridge_type: a string representing bridge name
        hint: a string giving a hint to travelers
        your_name: a string representing the name of the traveler

    Returns:
        "Dear traveler,
         Please be careful with the <type of the bridge>. My advice is: <hint>

         See you in Pythonia: <your name>
        "

    >>> print(sign("Flower bridge", "Do the opposite.", "Dr. Who"))
    Dear traveler,
    Please be careful with the Flower bridge. My advice is: Do the opposite.
    <BLANKLINE>
    See you in Pythonia: Dr. Who
    >>> print(sign("Flame Bridge", "Do not be afraid of it.", ""))
    Dear traveler,
    Please be careful with the Flame Bridge. My advice is: Do not be \
afraid of it.
    <BLANKLINE>
    See you in Pythonia: 

    # Add your own doctests below
    
    >>> print(sign("Death bridge", "Don\'t die.", "Mr. Poop"))
    Dear traveler,
    Please be careful with the Death bridge. My advice is: Don\'t die.
    <BLANKLINE>
    See you in Pythonia: Mr. Poop

    >>> print(sign("", "", ""))
    Dear traveler,
    Please be careful with the . My advice is: 
    <BLANKLINE>
    See you in Pythonia: 

    >>> print(sign("Bridge bridge", "Be a bridge.", "Sir Bridge"))
    Dear traveler,
    Please be careful with the Bridge bridge. My advice is: Be a bridge.
    <BLANKLINE>
    See you in Pythonia: Sir Bridge

    """
    # YOUR CODE GOES HERE #
    
    # creating the message
    message = f"Dear traveler,\nPlease be careful with the {bridge_type}. My \
advice is: {hint}\n\nSee you in Pythonia: {your_name}"

    return message



# Question 7
def my_nickname(first, last, age):
    """
    Outputs a string representing a nickname

    Args:
        first: a string representing a first name
        last: a string representing a last name
        age: an integer representing a person's age

    Returns:
        'Error' if the first and/or last names are not strings -
        'Error' if the age parameter is not an integer, less than 0, or greater
        than or equal to 100 -
        nickname (as a string) constructed as the first digit of age, every 
        other char of first starting at index 1, last in upper case, and the 
        last digit of age


    >>> my_nickname("Marina", "Langlois", 25)
    '2aiaLANGLOIS5'
    >>> my_nickname("Marina", "Langlois", 2.5)
    'Error'
    >>> my_nickname("", "Langlois", 25)
    '2LANGLOIS5'
    >>> my_nickname("", "Langlois", 5)
    '0LANGLOIS5'

    # Add your own doctests below

    >>> my_nickname("", "", 0)
    '00'

    >>> my_nickname("", 3, 5)
    'Error'

    >>> my_nickname("", ["Langlois"], 5)
    'Error'
    """
    # YOUR CODE GOES HERE #

    # age cannot be lower than 0 and higher than or equal to 100
    lower_bound = 0
    upper_bound = 100

    # checking first and last are type str
    parameter_1 = type(first) != str or type(last) != str

    # checking age is an integer, less than 0, or greater than or equal to 100
    parameter_2 = type(age) != int or age < lower_bound or age >= upper_bound
    
    # if type of first and last aren't string return error
    if parameter_1 or parameter_2:
        return "Error"

    # double digit age
    double_digits = 10

    # steps
    step = 2

    # creating components for nickname
    last_upper = last.upper()
    first_skip = first[1::step]
    if age < double_digits: # make the first digit 0 if age is a single digit 
        digit_1 = '0'
        digit_2 = str(age)
    else:
        digit_1 = str(age)[0]
        digit_2 = str(age)[1]

    # making the nickname
    nickname = digit_1 + first_skip + last_upper + digit_2

    return nickname

