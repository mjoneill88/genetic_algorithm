import string
import random

all_ascii_char = string.printable

def get_random_character():
    random_index = random.randint(0,99)
    random_char = all_ascii_char[random_index]
    return random_char

def make_word_into_list(word):
    word_as_list = list(word)
    return word_as_list

def generate_random_word(word):
    random_index = random.randint(0,99)
    random_char = all_ascii_char[random_index]
    random_string = random_char * len(word)
    return random_string



def evolution_function(end_list):
    starting_word = generate_random_word(word_as_list)
    starting_word = make_word_into_list(starting_word)
    index = 0
    count=0

    while starting_word != end_list:
        print('In Progress:', starting_word)
        index = 0
        count += 1
        for word in starting_word:
            if word == end_list[index]:
                index += 1
                pass
            else:
                starting_word[index] = get_random_character()
                index += 1
    print("Count:", count)
    return starting_word

word_as_list = make_word_into_list('Hello')
final_word = evolution_function(word_as_list)
print(final_word)
