# Group 10
# Broden Black
# Alexis De Paz Salazar
# 9/16/26
# Lab Assignment 4 - A program that quizzes the user on the state capitals, providing 4 possible answers each question for a total of 10 rounds. At the end the user is told how many points they got.

import random

def read_file_to_dict(file_name):
    """Takes the state capitals text file and reads in each line, separates the state and the capital, and 
    stores them as a key-value pair in a dictionary. Returning the filled dictionary."""
    file = open(file_name, 'r')  # Opens the capitals file
    lines = file.readlines()  # 
    file.close()  # Closes the capitals file

    state_dictionary = {}

    for line in lines:  # Iterates through the capitals file lines creating key-value pairs of states and capitals.
        line = line.strip()

        state, capital = line.split(",")

        state_dictionary[state] = capital
    return state_dictionary  # Returns a dictionary with the states

def get_random_state(states):
    """ Takes in the states dictionary. Converts the dictionary to a list of keys, then chooses a random
    key from the list and returns it."""
    state_list = list(states.keys())  # Creates a list of states

    state_random = random.choice(state_list)  # Picks a random state

    return state_random  # Returns a random state

def get_random_choices(states, correct_state):
    """passes in the states dictionary and the correct state. Places the correct state into a list and then calls
    get_random_state to add three other states to this list. These states are different from the correct state
    and also different from each other. Using the list of states it creates a list of capitals, shuffles it, 
    and then returns that list. This is the list of possible answers that the user will choose from."""
    state_choices = [correct_state]  # Creates a list with the correct state

    while len(state_choices) < 4:  # Adds 3 new different states
        random_state = get_random_state(states)

        if random_state not in state_choices:
            state_choices.append(random_state)

    capital_choices = []

    for state in state_choices:  # Adds capitals to capital choices list
        capital_choices.append(states[state])

    random.shuffle(capital_choices)  # Shuffles the choices order

    return capital_choices  # Returns the choices for capitals as a list


def ask_question(correct_state, possible_answers):
    """Passes in the name of the correct state and the list of four possible answers. 
    It displays the question to the user and the four possible answers. 
    Takes in the user's selection and checks that it is an A, B, C, or D. If it isn't, 
    then displays an 'Invalid' message and repeat until the user enters a valid choice. 
    If it is, then it converts the input to 0-3 (A=0, B=1, C=2, D=3) and returns the value."""
    # Asks user to choose an option A-D
    answer = input(". The capital of " + correct_state + " is: \n    A. " + possible_answers[0] + "  B. " + possible_answers[1] + "  C. " + possible_answers[2] + "  D. " + possible_answers[3] + "\nEnter selection (A, B, C, or D): ")
    while answer.upper() not in ["A", "B", "C", "D"]:
        answer = input("Invalid input. Input choice A-D.\nEnter selection: ")
    if answer.upper() == "A":
        answer = 0
    elif answer.upper() == "B":
        answer = 1
    elif answer.upper() == "C":
        answer = 2
    else:
        answer = 3
    return answer  # Returns the number relating to the letter answer chosen

def main():
    print("- Welcome to the State Capitals Quiz! -")  # Greets the user with a message
    point = 0  # Initializes the points as 0
    i = 0  #Initializes the attempt number
    states = read_file_to_dict("statecapitals.txt")  # Reads the capitals file
    while(i < 10):  # Loops through questions 10 times
        print(str(i + 1), end = "")
        correct_state = get_random_state(states)  # Gets a list of possible answers
        possible_answers = get_random_choices(states, correct_state)  # Gets a list of possible answers
        user_answer = ask_question(correct_state, possible_answers)  # Asks the question and get the user's answer
        if possible_answers[user_answer] == states[correct_state]:  # Checks if the answer is correct and update points
            print("Correct!")
            point += 1
        else:
            print("Incorrect! The correct answer is: " + states[correct_state] + ".")
        i += 1  # Increments the counter for attempt number


    print("End of test. You got " + str(point) + " correct.")  # Lets the user know how many correct answers they got at the end
main()