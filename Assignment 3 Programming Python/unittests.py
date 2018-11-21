# Multiples of K (Task 3)

import multiplek

#allMultiplesOfK function

assert multiplek.allMultiplesOfK(2, [3,7,42]) == False
assert multiplek.allMultiplesOfK(8, [16,80,40]) == True
assert multiplek.allMultiplesOfK(24, []) == True
assert multiplek.allMultiplesOfK(12, [72,14,22,24]) == False
assert multiplek.allMultiplesOfK(2, [4,12,64,32]) == True




# Happy and Sad Numbers (Task 5)

import happy

#sumOfDigitsSquared function

assert happy.sumOfDigitsSquared(72) == 53
assert happy.sumOfDigitsSquared(123) == 14 
assert happy.sumOfDigitsSquared(5201) == 30
assert happy.sumOfDigitsSquared(21) == 5
assert happy.sumOfDigitsSquared(12345) == 55

#isHappy function

assert happy.isHappy(70) == True
assert happy.isHappy(142) == False
assert happy.isHappy(404) == True
assert happy.isHappy(910) == True
assert happy.isHappy(777) == False

#kThHappy function

assert happy.kThHappy(5) == 19
assert happy.kThHappy(14) == 79
assert happy.kThHappy(140) == 973
assert happy.kThHappy(50) == 320
assert happy.kThHappy(72) == 469



# On Average, No Outlier (Task 6)

import avgno

#robust_avg function

assert round(avgno.robust_avg([1,7,23,5,4]),4) == 5.3333
assert round(avgno.robust_avg([7,15,23,51,32,12,5]),4) == 17.8
assert round(avgno.robust_avg([123,456,322,420,720,360]),4) == 389.5
assert round(avgno.robust_avg([78,32,13,98,25,7]),4) == 37.0
assert round(avgno.robust_avg([1,2,3,4,5,6,7,8,9,10,81,23,45,21,32]),4) == 13.4615

# Anagram (Task 7)

import anagram

#isAnagram function

assert anagram.isAnagram('alert','alter') == True
assert anagram.isAnagram('calipers','replicas') == True
assert anagram.isAnagram('deltas','astldd') == False
assert anagram.isAnagram('drapes','grapes') == False
assert anagram.isAnagram('forest','foster') == True