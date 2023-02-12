#!/bin/python3

import random

def load_name_list(filename):
    with open(filename) as f:
        return [name.capitalize() for name in (line.strip() for line in f) if len(name) > 0]

g_female_names = load_name_list('female-names.txt')
g_male_names = load_name_list('male-names.txt')
g_last_names = load_name_list('last-names.txt')

def random_entry(the_list):
    index = random.randint(0, len(the_list) - 1)
    return the_list[index]

def random_male_pet_name():
    return random_entry(g_male_names)

def random_female_pet_name():
    return random_entry(g_female_names)

def random_pet():
    pet = {}
    pet['sex'] = 'FM'[random.randint(0, 1)]
    if pet['sex'] == 'F':
        pet['name'] = random_female_pet_name()
    else:
        pet['name'] = random_male_pet_name()
    pet['species'] = random_entry(['dog', 'cat'])
    pet['size'] = 'small'
    if pet['species'] == 'dog':
        pet['size'] = random_entry(['small', 'medium', 'large'])
    return pet

def sql_insert_pet(pet):
    print(f'INSERT INTO PETS VALUES({pet["name"]}, {pet["sex"]}, {pet["species"]}, {pet["size"]})')

def main():
    for i in range(10):
        p = random_pet()
        sql_insert_pet(p)

if __name__ == '__main__':
    main()
