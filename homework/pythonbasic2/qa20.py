#  Iterate a given list and Check if a given element already exists in a dictionary as
#   a key’s value if not delete it from the list
# Given:
# rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
# sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# Expected Outcome:after removing unwanted elemnts from list [47, 69, 76, 97]

rollnumber  = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict  = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97} 
sampleDict_values = sampleDict.values()

to_remove = []
for roll in rollnumber:
    if roll in sampleDict_values:
        continue
  
    else:
        to_remove.append(roll)
for each in to_remove:
    rollnumber.remove(each)
print(rollnumber)
