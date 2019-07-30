import itertools
import heapq
import datetime

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
        perms.pop(mostOverlapIndex)
    print("Now verifying that all permutations are contained within the string: " + str(verifySuper(baseString, n)))
    print("The superpermtation is " + str(len(baseString)) + " characters long")
    return baseString

def verifySuper(superCandidate, n):
    perms = list(producePermuations(n))
    for perm in perms:
        if perm not in superCandidate:
            return False
    return True

print(datetime.datetime.now())
print(findSuper())
print(datetime.datetime.now())


        