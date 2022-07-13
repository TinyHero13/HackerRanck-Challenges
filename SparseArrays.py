strings = ['aba', 'baba', 'aba', 'xzxb']
queries = ['aba', 'xzxb', 'ab']

arr, result = [], []
for i in strings:
    if(i in queries):
       arr.append(i)
for i in queries:
    if(i in arr):
       result.append(arr.count(i))
    elif(i not in strings):
       result.append(0)

print(result)