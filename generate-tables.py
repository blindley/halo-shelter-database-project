#!/bin/python3

import random

def load_name_list(filename):
    with open(filename) as f:
        return [name.capitalize() for name in (line.strip() for line in f) if len(name) > 0]

g_female_names = load_name_list('data/female-names.txt')
g_male_names = load_name_list('data/male-names.txt')
g_last_names = load_name_list('data/last-names.txt')

def random_entry(the_list):
    index = random.randint(0, len(the_list) - 1)
    return the_list[index]

def generate_sql_insert_statement(table_name, field_values):
    values_string = ','.join((f"'{v}'" for v in field_values))
    return f'INSERT INTO {table_name} VALUES({values_string});'

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
    statement = generate_sql_insert_statement('PETS', [pet["name"], pet["sex"], pet["species"], pet["size"]])
    print(statement)

def main():
    print('CREATE TABLE PETS (NAME VARCHAR(32), SEX CHAR, SPECIES VARCHAR(10), SIZE VARCHAR(10));')

    for i in range(20):
        p = random_pet()
        sql_insert_pet(p)

if __name__ == '__main__':
    main()
