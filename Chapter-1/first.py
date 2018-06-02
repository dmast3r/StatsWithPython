import survey
table = survey.Pregnancies()
table.ReadRecords()
print("Number of pregnancies {}".format(len(table.records)))

