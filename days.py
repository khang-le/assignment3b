#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Sep 2019
# This program show numbers matched days


def main():
    # this function guesses random number

    # input
    user_input = input("Enter a number from 2 to 8: ")
    print("")

    # process

    try:
        huhuhu = int(user_input)
        if huhuhu == 2:
            print("Monday")
            print("")
        elif huhuhu == 3:
            print("Tuesday")
            print("")
        elif huhuhu == 4:
            print("Wedsnday")
            print("")
        elif huhuhu == 5:
            print("Thursday")
            print("")
        elif huhuhu == 6:
            print("Friday")
            print("")
        elif huhuhu == 7:
            print("Saturday")
            print("")
        elif huhuhu == 8:
            print("Sunday")
            print("")
        else:
            print("no idea if the number is not from 2 to 8 :(")
            print("")
    except Exception:
        print("This is not an integer")
        print("")
    finally:
        print("Thank you for wasting your time")


if __name__ == "__main__":
    main()
