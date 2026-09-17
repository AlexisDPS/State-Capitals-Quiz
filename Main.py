# Group 10
# Broden Black
# Alexis De Paz Salazar
# Lab Assignment 4 - A program that quizzes the user on the state capitals

import random

def read_file_to_dict(file_name):
    """Read in each line, separate the state and the capital, and store them as a key:
    value pair in a dictionary. Return the filled dictionary."""
    file = open(file_name, 'r')
    lines = file.readlines()

    state_dictionary = {}

    for line in lines:
        line = line.strip()

        state, capital = line.split(",")

        state_dictionary[state] = capital
    return state_dictionary

def get_random_state(states):
    """ pass in the states dictionary. Convert the
    dictionary to a list of keys, then choose a random key from the list and return it."""
    state_list = list(states.keys())

    state_random = random.choice(state_list)

    return state_random

def get_random_choices(states, correct_state):
    """pass in the states
dictionary and the correct state. Place the correct state into a list and then call
get_random_state to add three other states to this list. These states should be
different from t    he correct state and also different from each other. Using the list of states,
create a list of capitals, shuffle it, and then return that list. This is the list of possible
answers that the user will choose from."""
    state_choices = [correct_state]

    while len(state_choices) < 4:
        random_state = get_random_state(states)

        if random_state not in state_choices:
            state_choices.append(random_state)

    capital_choices = []

    for state in state_choices:
        capital_choices.append(states[state])

    random.shuffle(capital_choices)

    return capital_choices


def ask_question(correct_state, possible_answers):
    """Pass in the name of the correct state and the list of four possible answers. 
    Display the question to the user and the four possible answers. 
    Take in the user's selection and check that it is an A, B, C, or D. If it isn't, 
    then display an 'Invalid' message and repeat until the user enters a valid choice. 
    If it is, then convert the input to 0-3 (A=0, B=1, C=2, D=3) and return the value."""

    answer = input(". The capital of " + correct_state + " is: \n    A. " + possible_answers[0] + "  B. " + possible_answers[1] + "  C. " + possible_answers[2] + "  D. " + possible_answers[3] + "\nEnter selection (A, B, C, or D): ")
    while answer not in "ABCDabcd":
        answer = input("Invalid input. Input choice A-D.\nEnter selection: ")
    if answer.upper() == "A":
        answer = 0
    elif answer.upper() == "B":
        answer = 1
    elif answer.upper() == "C":
        answer = 2
    else:
        answer = 3
    return answer

def main():
    print("- Welcome to the State Capitals Quiz! -")
    point = 0
    i = 0
    states = read_file_to_dict("statecapitals.txt")
    while(i < 10):
        print(str(i + 1), end = "")
        # Gets a random state from the dictionary
        correct_state = get_random_state(states)
        # Gets a list of possible answers
        possible_answers = get_random_choices(states, correct_state)
        # Asks the question and get the user's answer
        user_answer = ask_question(correct_state, possible_answers)
        # Checks if the answer is correct and update points
        if possible_answers[user_answer] == states[correct_state]:
            print("Correct!")
            point += 1
        else:
            print("Incorrect! The correct answer is: " + states[correct_state] + ".")
        i += 1


    print("End of test. You got " + str(point) + " correct.")
main()