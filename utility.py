
import random

def random_element(the_list):
    index = random.randint(0, len(the_list) - 1)
    return the_list[index]

def sql_create_table(table_name, fields):
    fields_str = ', '.join((f'{f[0]} {f[1]}' for f in fields))
    return f'CREATE TABLE {table_name} ({fields_str});'

def sql_insert(table_name, field_values):
    values_string = ','.join((f"'{v}'" for v in field_values))
    return f'INSERT INTO {table_name} VALUES({values_string});'
