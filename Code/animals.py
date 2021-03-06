from dictionary_words import getWords
from pprint import pprint

def count_animals(animals_list):
    """Count occurences in the given list of animals
    and return that data structure"""
    animal_counts = {}
    for animal_name in animals_list:
        if animal_name in animal_counts:
            animal_counts[animal_name] += 1
        else :
            animal_counts[animal_name] = 1

    return animal_counts

def print_table(animal_counts):
    """prints out a tabel of animals and their counts."""
    print('Animal || Count')
    print('------------')
    # for animal_name in animal_counts:
    #     count = animal_counts[animal_name]
    #     print('{} | {}'.format(animal_name, count))
    total_count = 0
    for animal_name, count in animal_counts.items():
        total_count += count
        print('{} | {}'.format(animal_name, count))
    print('------------')
    print(f'Total: {total_count}')



# pprint(count_animals(getWords('animals.txt')))
print_table(count_animals(getWords('animals.txt')))



# def get_words(filename):
#     """Open the file and 
#     returns a list of all words in it."""
#     all_words_list = []
#     with open(filename) as file:
#         for line in file:
#             words_list = line.split()
#             for word in words_list:
#                 all_words_list.append(word)
#     return all_words_list

# print(get_words('animals.txt'))
