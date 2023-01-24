# Dictionary and counter in Python to find winner of election
from collections import Counter

votes =['john','johnny','jackie','johnny','john','jackie',
'jamie','jamie','john','johnny','jamie','johnny','john']

# Count the votes for persons and stores in the dictionary
vote_count = Counter(votes)

# finding maximum number votes
max_votes = max(vote_count.values())

# search people having maximum votes and store in a list
lst = [i for i in vote_count.keys() if vote_count[i] == max_votes]

print(sorted(lst)[0])