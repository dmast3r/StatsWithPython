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