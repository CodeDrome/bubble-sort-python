import bubblesort
import random


def main():

    """
    Create a list of random numbers and pass them to the bubblesort function.
    """

    print("-----------------")
    print("| codedrome.com |")
    print("| Bubble Sort   |")
    print("-----------------\n")

    data = []

    for i in range(0, 16):
        data.append(random.randint(1, 99))

    bubblesort.bubblesort(data)


main()
