import random
import utility, names
from utility import random_element

table_name = 'PET'
table_fields = [
        ['NAME',    'VARCHAR(30)'],
        ['SEX',     'CHAR(1)'],
        ['SPECIES', 'VARCHAR(10)'],
        ['SIZE',    'VARCHAR(10)'],
    ]

def sql_create_table():
    return utility.sql_create_table(table_name, table_fields)

def sql_insert_random():
    pet = random_pet()
    return utility.sql_insert('PETS', [pet["name"], pet["sex"], pet["species"], pet["size"]])

def random_male_pet_name():
    return random_element(names.male_names)

def random_female_pet_name():
    return random_element(names.female_names)

def random_pet():
    pet = {}
    pet['sex'] = 'FM'[random.randint(0, 1)]
    if pet['sex'] == 'F':
        pet['name'] = random_female_pet_name()
    else:
        pet['name'] = random_male_pet_name()
    pet['species'] = random_element(['dog', 'cat'])
    pet['size'] = 'small'
    if pet['species'] == 'dog':
        pet['size'] = random_element(['small', 'medium', 'large'])
    return pet
