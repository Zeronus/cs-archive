# Problem 4 : 'ABBA'

def generateAB(n): 
    if n == 1:
        return ['A','B']
    else:
        lst = []
        for i in generateAB(n-1):
            lst.append(i+'A')
            lst.append(i+'B')
        return lst

    
assert generateAB(5) == sorted(generateAB(5))
assert generateAB(10) == sorted(generateAB(10))
assert generateAB(8) == sorted(generateAB(8))
assert generateAB(12) == sorted(generateAB(12))