# CS104

# Joseph Nahoum

# average.py

#Averaging test scores

#Set Variables
average = 0
total = 0
howManyEntered = 0

#Set how many scores to average
howMany = int(input("How many test scores would you like to average?"))

#While loop to enter all test scores
while howManyEntered < howMany:
    testScore = int(input("Enter test score: "))
    total = total + testScore
    howManyEntered = howManyEntered + 1
    
#Compute and display average to user
average = total/howMany
print("The average for the test scores you entered is", average)
