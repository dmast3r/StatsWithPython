import survey

# create an instance of the Pregnancies table
table = survey.Pregnancies()

# this table contains a list of records of type Pregnancy. Make sure to call the ReadRecords method on the table object
# which will read the data file and store all the records.
table.ReadRecords()

# now traverse each record from the list of records that you can obtain by calling table.records.
# now for each record, check if the outcome instance is set to 1(which indicates Live Birth).
# If you have implemented the below part correctly you should get output equals to 9148
print('Total count of Live Births is {}'.format(sum(1 for record in table.records if record.outcome == 1)))


# -------------------- Solution to question 3 : Categorise Live births into first child and others ------------------- #
# In this part we are supposed to count the Live Births separately for the first and the rest of the Children
firstChildCount = 0
otherChildrenCount = 0

for record in table.records:
    if record.outcome == 1 and record.birthord != 'NA': # handle the edge case of getting an inapplicable birth-order
        if record.birthord == 1: # if it's the first baby
            firstChildCount += 1
        else:
            otherChildrenCount += 1

# if your implementation is correct then you should be getting 4413 and 4735 as answer.
print('Total of count of Live Births for the child is {} and for rest of the children it\'s {}'
      .format(firstChildCount, otherChildrenCount))

