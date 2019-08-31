#Raul Solorio
#September 15
#This program displays the students name, degree name and the amount of credits
#left until graduation

studentName = input('Enter student name. ')
degreeName = input('Enter degree name. ')
creditsDegree = input('Enter the number of credits required for the degree. ')
creditsTaken = input('Enter the number of credits taken so far. ')
creditsLeft = float(creditsDegree) - float(creditsTaken)
print ()
print ("The student\'s name is", studentName)
print ('The degree name is', degreeName)
print ('There are', creditsLeft, 'credits left until graduation.')
input('Press enter to exit')

