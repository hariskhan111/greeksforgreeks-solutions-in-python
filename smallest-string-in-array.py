def stringChallenge(tofind, tobefind, pi):
    lst = []
    ind = None
    for i in range(len(tofind)):
        if ind:
            find, index = findIndex(tofind[i], tobefind, pi, ind)
        else:
            find, index = findIndex(tofind[i], tobefind, pi)
        if not find:
            return False, []
        lst.append(index)
        ind = index
        print("ind", ind)
    return True, lst   


def findIndex(tofind, tobefind, pi, pic=None):
    iter = int(pic)+1 if pic else 0 
    for index in range(iter, len(tobefind)):
        print(index, 787878)
        if index < pi:
            continue
        if tobefind[index] == tofind:
            return True, index
    return False, "not found"


def handle_arr(arr): 
    tobefind = arr[0]
    tofind = arr[1]
    strings_indexes = []
    for i in range(len(tobefind)):
        find, index_list = stringChallenge(tofind, tobefind, i)
        if find:
            strings_indexes.append([index_list[0], index_list[-1]])
    return strings_indexes
    
arr = ['ababdccdbcaacd','aad']
string = handle_arr(arr)
dicts = {}
for strg in string:
    strg = sorted(strg)
    dicts[strg[-1] - strg[0]] = strg
myKeys = list(dicts.keys())
myKeys = sorted(myKeys)
shortest = dicts[myKeys[0]]
print(shortest)
res = arr[0][shortest[0]:shortest[1]+1]
print(res)
    
    