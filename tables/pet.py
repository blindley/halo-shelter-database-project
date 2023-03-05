import random
import utility, names
from utility import random_element

table_name = 'PET'
table_fields_array = [
        ['NAME',    'VARCHAR(30)'],
        ['SEX',     'CHAR(1)'],
        ['SPECIES', 'VARCHAR(10)'],
        ['SIZE',    'VARCHAR(10)'],
    ]
table_fields = [{"name": f[0], "type": f[1]} for f in table_fields_array]

def sql_create_table():
    return utility.sql_create_table(table_name, table_fields)

def sql_insert_random():
    pet = random_pet()
    return utility.sql_insert_by_field_names(
            table_name,
            (f['name'] for f in table_fields),
            pet
        )

def random_male_pet_name():
    return random_element(names.male_names)

def random_female_pet_name():
    return random_element(names.female_names)

def random_pet():
    pet = {}
    pet['SEX'] = 'FM'[random.randint(0, 1)]
    if pet['SEX'] == 'F':
        pet['NAME'] = random_female_pet_name()
    else:
        pet['NAME'] = random_male_pet_name()
    pet['SPECIES'] = random_element(['dog', 'cat'])
    pet['SIZE'] = 'small'
    if pet['SPECIES'] == 'dog':
        pet['SIZE'] = random_element(['small', 'medium', 'large'])
    return pet
