# 19) Given two sets, Checks if One Set is Subset or superset of Another Set. if the subset is found delete all elements from that set

# For Example:
# firstSet = {27, 43, 34}
# secondSet = {34, 93, 22, 27, 43, 53, 48}
# Expected Output:
# First Set  {57, 83, 29}
# Second Set  {67, 73, 43, 48, 83, 57, 29}
# First set is subset of second set - True
# Second set is subset of First set -  False
# First set is Super set of second set -  False
# Second set is Super set of First set -  True
# First Set  set()
# Second Set  {67, 73, 43, 48, 83, 57, 29}

firstSet  = {27, 43, 34}
SecondSet = {34, 93, 22, 27, 43, 53, 48}
if firstSet.issubset(SecondSet):
    for i in firstSet:
       SecondSet.remove(i)
print(SecondSet)
