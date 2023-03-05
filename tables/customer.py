import random
import utility, names
from utility import random_element

table_name = 'CUSTOMER'
table_fields_array = [
        ['LASTNAME',    'VARCHAR(30)'],
        ['FIRSTNAME',   'VARCHAR(30)'],
        ['PHONE',       'VARCHAR(30)'],
        ['ADDRESS',     'VARCHAR(50)'],
    ]
table_fields = [{"name": f[0], "type": f[1]} for f in table_fields_array]

def sql_create_table():
    return utility.sql_create_table(table_name, table_fields)

def sql_insert_random():
    pet = random_customer()
    return utility.sql_insert_by_field_names(
            table_name,
            (f['name'] for f in table_fields),
            pet
        )

def random_address():
    house_number = random.randint(100,9999)
    street_name = random_element(names.last_names)
    prefix = random_element(['N.', 'S.', 'E.', 'W.', ''])
    suffix = random_element(
        ['St.', 'Dr.', 'Blvd.', 'Rd.', 'Ave.', 'Pkwy.']
    )
    return ' '.join(f'{house_number} {prefix} {street_name} {suffix}'.split())

def random_phone_number():
    p1 = random.randint(100,999)
    p2 = random.randint(1000,9999)
    return f'{p1}-{p2}'

def random_customer():
    customer = {}
    if random.randint(0, 1) == 0:
        customer["FIRSTNAME"] = random_element(names.female_names)
    else:
        customer["FIRSTNAME"] = random_element(names.male_names)
    customer["LASTNAME"] = random_element(names.last_names)
    customer["PHONE"] = random_phone_number()
    customer["ADDRESS"] = random_address()
    return customer
