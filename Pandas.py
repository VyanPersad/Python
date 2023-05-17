import pandas

data_frame = pandas.DataFrame([[45, 85, 97], [41, 36, 85], [78, 96, 41]],
                              columns=["C1", "C2", "C3"],
                              index=["R1", "R2", "R3"])

print(data_frame)

avg = data_frame.C1.mean()
print("{:.2f}".format(avg))
#OR
avg = "{:.2f}".format(data_frame.C1.mean())
print(avg)

#Note the use of the curly brackets.
data_frame2 = pandas.DataFrame([{
    "Name": "Ralph",
    "Surname": "Lundgreen"
}, {
    "Name": "John",
    "Surname": "Smith"
}, {
    "Name": "Roger",
    "Surname": "Hamilton"
}])

print(data_frame2)
