# sort dict by key
myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
 
myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}
print(sorted_dict)

#sort dict by value 
import operator
x = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(sorted_x[0])

people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
# Sort by key
res = dict(sorted(people.items()))
print(res)
#{1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}

# Sort by value
res = dict(sorted(people.items(), key=lambda item: item[1]))
print(res)
#{2: 'Jack', 4: 'Jane', 1: 'Jill', 3: 'Jim'}