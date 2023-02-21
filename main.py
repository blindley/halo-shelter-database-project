#!/bin/python3

import table_pet

def main():
    print(table_pet.sql_create_table())
    for i in range(20):
        print(table_pet.sql_insert_random())

if __name__ == '__main__':
    main()
