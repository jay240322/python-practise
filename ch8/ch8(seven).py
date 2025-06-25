# Write a python function to remove a given word from a list ad strip it at the same
# time.

def rem(L,word):
    n = []
    for item in L:
        if not(item == word):
            n.append(item.strip(word))
    return n

L = ["ronak","mohan","janak","manak"]

print(rem(L,"ak"))