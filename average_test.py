""" Python to get the average of a given list with numbers.
    Using the statistical function mean.
    Print the given list and the result on the terminal 
    and round the result to two decimal places
"""

# importing the tatistical function mean
from statistics import mean


# neue Funktion definieren
def average2():
    pass

# create a list with number of your choice
listOfNumbers = [1, 2, 3, 4, 5, 6, 3.14, 1.414]

# calculate the average
averageOfList = mean(listOfNumbers)

# print the list and the result
print(" The content of the is =", listOfNumbers , " the average of the list is = ", round(averageOfList,2))