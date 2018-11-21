# PROBLEM 5

def kthWord(L,k):
    answer = []
    count = 0
    countLimit = 1
    while True:
        answer.append(L[count])
        count += 1
        if count == countLimit:
            countLimit += 1
            count = 0
        if answer[-1] == L[-1]:
            break
    if k == 0 or k > len(answer):
        return None
    return answer[k-1]

# Method is to append unique words. Count resets to 0 so earlier words will have to
# be said again and limit keeps increasing per loop because one more word is said every round

        
