import itertools
import heapq




# Greedy implementation. Very subpar. Will change to graph implementation as soon as I can. 

def producePermuations(n):
    characters = []
    counter = 0
    while (counter < n):
        characters.append(str(counter))
        counter += 1
    permutationsList = list(itertools.permutations(characters))
    for i in range(len(permutationsList)):
        permutationsList[i] = "".join(permutationsList[i])
    return permutationsList

def findOverlap(base, addition):
    overlap = addition
    permLen = len(addition)
    baseTail = base[-permLen:]
    while overlap != baseTail:
        overlap = overlap[:-1]
        baseTail = baseTail[1:]
        print("hi: " + baseTail)
        print(overlap)
    return addition[len(overlap):]

def difference(base, addition):
    return len(findOverlap(base, addition))

def findSuper():
    n = int(input("Please enter the number of characters you want in the superpermutation: "))
    perms = producePermuations(n)
    baseString = perms[0]
    perms.pop(0)
    while perms != []:
        overlaps = list(map(lambda x: difference(baseString, x), perms))
        mostOverlapIndex = overlaps.index(min(overlaps))
        baseString = baseString + findOverlap(baseString, perms[mostOverlapIndex])
        perms = list(filter(lambda x: x not in baseString, perms))

    print(verifySuper(baseString, n))
    print(len(baseString))
    return baseString

def verifySuper(superCandidate, n):
    perms = list(producePermuations(n))
    for perm in perms:
        if perm not in superCandidate:
            return False
    return True


print(findSuper())



# Graph implementation, hopefully using asymmetrical
# travelling salesman. TODO: Finish this

# class Node:
#     def __init__(self, perm):
#         """Perm is a string that is a permutation of n characters. """
#         self.value = perm
#         self.edges = []
#         self.visited = False

#     def getValue(self):
#         return self.value

#     def getEdges(self):
#         return self.edges
    
#     def findWeight(self, n2):
#         """Finds weight from self to n2"""
#         weight = 0
#         p1 = self.getValue()
#         p2 = n2.getValue()
#         while p1 != p2:
#             p1 = p1[1:]
#             p2 = p2[:-1]
#             weight += 1
#         return weight

# class Edge:
    
#     def __init__(self, n1, n2):
#         """edge from n1 to n2"""
#         self.origin = n1
#         self.destination = n2
#         self.weight = n1.findWeight(n2)
    
#     def __lt__(self, other):
#         if self.destination
#         return self.weight < other.weight
        


# class Graph:


#     def __init__(self, n):
#         perms = producePermuations(n)
#         for index in list(range(perms)):
#             perms[index] = Node(perms[index])
#         self.nodes = perms


        