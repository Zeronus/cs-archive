# PROBLEM 2

def triplet(text):
    startIndex = 0
    repeats = 0
    while startIndex < len(text) - 1:
        if text[startIndex + 1] == text[startIndex]:
            repeatIndex = startIndex - 1 # Minus one because startIndex will update regardless of repeat
            repeats += 1
        else:
            repeats = 0
            repeatIndex = 0
        if repeats == 2:
            return repeatIndex
        startIndex += 1
    if repeats == 0:
        return -1
            
# Loop through each letter and count the number of repeats. Keep track of the index of the
# first letter to repeat with repeatIndex variable. If there are 0 repeats, return -1 but 
# if there are 3 repeats (repeat == 2) then return repeatIndex

assert triplet('x') == -1
assert triplet('jklmn') == -1
assert triplet('abbcccd') == 3
assert triplet('hhhhhhkhgdfuuu') == 0