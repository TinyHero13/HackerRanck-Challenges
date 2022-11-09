def matchingStrings(strings, queries):
    lst = []
    for i in queries:
        lst.append(strings.count(i))
    return lst   
