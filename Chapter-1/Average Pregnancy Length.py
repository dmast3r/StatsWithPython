"""
    Question 4 of the first exercise. Calculate Average Pregnancy Length for the first child and the other children
    separately, also mention the difference
"""

import survey

# create an instance of the Pregnancies table
table = survey.Pregnancies()

# this table contains a list of records of type Pregnancy. Make sure to call the ReadRecords method on the table object
# which will read the data file and store all the records.
table.ReadRecords()

firstChildCount = 0
firstChildPregnancyLengthSum = 0
restChildrenCount = 0
restChildrenPregnancyLengthSum = 0

for record in table.records:
    if record.birthord != 'NA':
        if record.birthord == 1:
            firstChildCount += 1
            firstChildPregnancyLengthSum += record.prglength
        else:
            restChildrenCount += 1
            restChildrenPregnancyLengthSum += record.prglength


averageFirstChildPregnancyLength = 0 if firstChildCount == 0 else firstChildPregnancyLengthSum / firstChildCount
averageRestChildrenPregnancyLength = 0 if restChildrenCount == 0 else restChildrenPregnancyLengthSum / restChildrenCount

print("Average Pregnancy length for the first child is {} and for rest of the children is {}"
      .format(averageFirstChildPregnancyLength, averageRestChildrenPregnancyLength))
print("And the difference is {:.2f}".format(averageFirstChildPregnancyLength - averageRestChildrenPregnancyLength))