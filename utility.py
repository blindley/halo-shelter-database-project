
import random

def random_element(the_list):
    index = random.randint(0, len(the_list) - 1)
    return the_list[index]

def sql_create_table(table_name, fields):
    fields_str = ', '.join((f'{f["name"]} {f["type"]}' for f in fields))
    return f'CREATE TABLE {table_name} ({fields_str});'

def sql_insert(table_name, field_values):
    values_string = ','.join((f"'{v}'" for v in field_values))
    return f'INSERT INTO {table_name} VALUES({values_string});'

def sql_insert_by_field_names(table_name, field_names_array, field_values):
    return sql_insert(table_name, (field_values[name] for name in field_names_array))
