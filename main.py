#!/bin/python3

from tables import pet, customer

def main():
    print(pet.sql_create_table())
    print(customer.sql_create_table())

    for i in range(20):
        print(pet.sql_insert_random())
    for i in range(20):
        print(customer.sql_insert_random())

if __name__ == '__main__':
    main()
