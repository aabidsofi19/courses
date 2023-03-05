import time
import copy
i = 0
mincut = []

with open('graph1.txt') as f:
        dictionary = {}
        for line in f:
            number = line.strip().split('\t')
            dictionary[number[0]] = number[1:]
    

for i in range(0,200):
    import random
    a = copy.deepcopy(dictionary)
    length = len(a)
    i += 1
    print(i)
    while length > 2:
      
        
        #calculating length of dictionary
        vertex_1 = random.choice(list(a.keys())) # selecting the first node of the edge randomly
        vertex_2 = random.choice(a[vertex_1]) # selecting the second node of the edge randomly 
    
        #print "%d and %d are the node edges" % (vertex_1, vertex_2)# selecting the second node of the edge randomly
        a[vertex_1] = a[vertex_1] + a[vertex_2] # fusing the nodes part 1 - UNION (adding edges of second node to first node)
        a.pop(vertex_2) # fusing the nodes part 2 - REMOVE (removing edges of second node)
        for key,value in a.items():
            while(vertex_2 in a[key]):
                a[key].remove(vertex_2)
                a[key].append(vertex_1)
            
        for key,value in a.items():
            while key in a[key]:
                a[key].remove(key)
        length = len(a) 
    
    #print a 
    for key,value in a.items():
        mincut.append(len(a[key])) 
        break

print(min(mincut))
