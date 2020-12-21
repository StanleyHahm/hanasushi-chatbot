# hanasushi.py
# our family's restaurant recently had to close due to bankruptcy
# and despite our plans to start again in another city, COVID-19
# unfortunately put a stop to this. Despite this, we've tried our
# best to start up again and we have successfully started as of a week
# ago. I started w/ another project (Encryption) however I've changed
# courses as I not only want to make an interesting chatbot, but
# I wanted to make something that'll put a smile on my parents' faces.
# Thus, I made hanasushi.py, named after our restaurant.#hanasushi.py
# our family's restaurant recently had to close due to bankruptcy
# and despite our plans to start again in another city, COVID-19
# unfortunately put a stop to this. Despite this, we've tried our
# best to start up again and we have successfully started as of a week
# ago. I started w/ another project (Encryption) however I've changed
# courses as I not only want to make an interesting chatbot, but
# I wanted to make something that'll put a smile on my parents' faces.
# Thus, I made hanasushi.py, named after our restaurant.

"""It starts off laying out the functions I need to create a chatbot.
There are 'string_concatenator' which puts together two strings,
'remove_punctuation' to remove any unnecessary punctuation,
'prepare_text' to separate string into a list of words, etc.
Each of the functions' descriptions are listed in its respective cell.
Then, there's a testing function that allows the user to interact with
the chatbot.
"""

import string
import random


#removes uncessary punctuation
def remove_punctuation(input_string):
    out_string = ''

    for item in input_string:
        if item not in string.punctuation:
            out_string += item
        else:
            continue

    return out_string


#prepares text for interpreting by separating string into a list
#of words
def prepare_text(input_string):

    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()

    return out_list


#selects appropriate output based on if item is in a certain input list
def selector(input_list, check_list, return_list):
    output = None

    for item in input_list:
        if item in check_list:
            output = random.choice(return_list)
            break
        else:
            continue

    return output


#puts together two strings
def string_concatenator(string1, string2, separator):

    output = string1 + separator + string2

    return output

#puts lists of strings to one string
def list_to_string(input_list, separator):
    output = input_list[0]

    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)

    return output


# In[44]:


#ends chat if input is 'quit'
def end_chat(input_list):

    if 'quit' in input_list:
        return True
    else:
        return False


# checking and finding if input is in any lists

def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""

    for element in list_one:
        if element in list_two:
            return True

    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""

    for element in list_one:
        if element in list_two:
            return element

    return None


# This cell defines a collection of input and output things our chatbot can say and respond to

GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
GREETINGS_OUT = ["Hello, it's nice to talk to you! How can I help you?",
                 'Nice to meet you! How can I help you?',  "Hey - Let's chat! How can I help you?"]

SUSHI_IN = ['sushi','roll','rolls','raw']
SUSHI_OUT = ['We have an array of sushi! We have Salmon Rolls, Tuna Rolls, Baked Eel Rolls, and many others.'
            'We have an array of sushi! You can check it out at hanasushigrill.com']

SEAFOOD_IN = ['seafood','fish','cooked fish']
SEAFOOD_OUT = ['We have seafood dishes!', 'If you like cooked fish, we have grilled Salmon.'
              'You like stir fried seafood? We have that complimented with a bowl of rice!']

KOREAN_IN = ['korea', 'korean', 'meat', 'bulgogi', 'kalbi', 'BBQ']
KOREAN_OUT = ['We have Korean food!', 'We have Korean BBQ dishes served with a side of rice!',
             'There are bulgogi, kalbi, and fire chicken options.']

LUNCH_IN = ['lunch', 'cheap']
LUNCH_OUT = ['Some of our lunch options are beef plate, chicken plate, sashimi lunch box, and many more!',
            'We offer lunch boxes with various proteins tht come with California rolls, tempura, salad, and rice.',
            'Not only do we offer lunch boxes, but we offer Hana Bowls which are protein, rice mixed with egg and sour cream.']

TOGO_IN = ['to go', 'to-go','togo', 'take out', 'takeout', 'dine in', 'dinein']
TOGO_OUT = ['Unfortunately given the current situations, we are only offering Take Out options. However all of our food items are available for to-go options!',
           'We are only offering take out services right now', 'We only offer takeout, but we will soon be offering delivery services as well.']

LOVE_IN = ['merced', 'central valley']
LOVE_OUT = ['is the best! We love it here.', "is where we're at! Come on thru!"]
LOVE_NAMES = {'merced':'City of', 'central valley':'Here in the'}

NONO_IN = ['Maroo', 'Fresno']
NONO_OUT = ["I'm sorry, I don't think I can talk about that."]

UNKNOWN = ["I'm sorry. Can you word that differently?","Ah, I don't seem to understand."]


# In[47]:


def have_a_chat():
    """Main function to run our chatbot."""

    chat = True
    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))

            # Check if the input looks like a computer thing, add a computer output if so
            outs.append(selector(msg, SUSHI_IN, SUSHI_OUT))
            outs.append(selector(msg, SEAFOOD_IN, SEAFOOD_OUT))
            outs.append(selector(msg, KOREAN_IN, KOREAN_OUT))
            outs.append(selector(msg, LUNCH_IN, LUNCH_OUT))
            outs.append(selector(msg, TOGO_IN, TOGO_OUT))

            # Check if the input mentions a person that is specified, add a person output if so
            if is_in_list(msg, LOVE_IN):
                name = find_in_list(msg, LOVE_IN)
                outs.append(list_to_string([LOVE_NAMES[name], name.capitalize(),
                                            selector(msg, LOVE_IN, LOVE_OUT)], ' '))

            # Check if the input has some words we don't want to talk about, say that, if so
            if is_in_list(msg, NONO_IN):
                outs.append(list_to_string([selector(msg, NONO_IN, NONO_OUT), find_in_list(msg, NONO_IN)], ' '))


            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)

have_a_chat()
