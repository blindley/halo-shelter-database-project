#!/bin/python3

import tables.pet as pet

def main():
    print(pet.sql_create_table())
    for i in range(20):
        print(pet.sql_insert_random())

if __name__ == '__main__':
    main()
