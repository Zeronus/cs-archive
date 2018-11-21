# Task 1 = reverse.py

import reverse

assert reverse.rev_str("nowhere") == "erehwon"
assert reverse.rev_str("gnimmargorpevoli") == "iloveprogramming"
assert reverse.rev_str("y") == "y"
assert reverse.rev_str("suoicodilaipxecitsiligarfilacrepus") == "supercalifragilisticexpialidocious"
assert reverse.rev_str("") == ""

# Task 2 = altsum.py

import altsum

assert altsum.altSum([]) == 0
assert altsum.altSum([1,3,5,2]) == 1
assert altsum.altSum([9,9,9,9]) == 18
assert altsum.altSum([3,7,2,1,5,23]) == 27
assert altsum.altSum([32,74,51,20,0,1,5]) == 71

# Task 3 = aloud.py

import aloud

assert aloud.readAloud([1,1,6,7,7,4]) == [2,1,1,6,2,7,1,4]
assert aloud.readAloud([5,7,2,2,4,1]) == [1,5,1,7,2,2,1,4,1,1]
assert aloud.readAloud([-5,-5,2,2]) == [2,-5,2,2]
assert aloud.readAloud([5,0,2,1,1,1,1]) == [1,5,1,0,1,2,4,1]
assert aloud.readAloud([1,-2,3,-4,5,-7,7]) == [1,1,1,-2,1,3,1,-4,1,5,1,-7,1,7]

# Task 4 = hidden.py

import hidden

assert hidden.is_hidden("aqwedlkrokdjntyrauiejlmvmdtkrnuamwp","donaldtrump") == True
assert hidden.is_hidden("ww12zXuelAxwPxlpxewpqwle","apple") == False
assert hidden.is_hidden("ww12zXuelAxwPxlpxewpqwle","APple") == True
assert hidden.is_hidden("abywoclIsAmCIoPCSLw1940231","ICCS101") == True
assert hidden.is_hidden("alkwhdlkawd;ldawddwad","banana") == False

# Task 5 = cipher.py

import cipher

assert cipher.enc("abc",2) == 'acb'
assert cipher.enc("monosodium glutamate", 7) =='mitouanmmo asgtoledu'
assert cipher.enc("polylogarithmicsubexponential", 3) == 'pygimseonaolatiuxntllorhcbpei'
assert cipher.enc("Antidisestablishmentarianism",13) == 'Aisnsmthimdeinsteasrtiaabnli'
assert cipher.enc("Concentration of incineration",5) == 'Cnifitoto ninrnieoca nrnetoca'

# Task 6 = jogging.py

import jogging

log_book1 = [
    "cycling;time:1,49;distance:2",
    "jogging;time:40,11;distance:6",
    "swimming;time:1,49;distance:1.2",
    "jogging;time:36,25;distance:5.3",
    "hiking;time:106,01;distance:8.29"
]
log_book2 = [
    "cycling;time:1,49;distance:2",
    "joggingAdventure;time:40,11;distance:6",
    "swimming;time:1,49;distance:1.2",
    "joggingTime;time:36,25;distance:5.3",
    "running;time:12,01;distance:6.5"
]
log_book3 = [
    "driving;time:26,05;distance:2.7",
    "cycling;time:15,23;distance:72",
    "running;time:47,00;distsance:1",
    "swimming;time:1,42;distance:7"
]
log_book4 = [
    "cycling;time:1,49;distance:2",
    "jogging;time:40,11;distance:6",
    "joggingfast;time:71,11;distance:7.2"
]
log_book5 = [
    "joggingA;time:1,49;distance:2",
    "jogging;time:40,11;distance:12",
    "jogging;time:88,05;distance:2",
    "joggingB;time:36,25;distance:5.3",
    "joggingC;time:106,01;distance:8.29"
]

assert round(jogging.jogging_average(log_book1),4) == 2.4587
assert round(jogging.jogging_average(log_book2),4) == 0
assert round(jogging.jogging_average(log_book3),4) == 0
assert round(jogging.jogging_average(log_book4),4) == 2.4886
assert round(jogging.jogging_average(log_book5),4) == 1.8191

assert jogging.parse_dist("jogging;time:88,05;distance:2") == 2000
assert jogging.parse_dist("jogging;time:123,23;distance:4.7") == 4700
assert jogging.parse_dist("jogging;time:111,05;distance:0.5") == 500
assert jogging.parse_dist("jogging;time:2,15;distance:1.2") == 1200
assert jogging.parse_dist("jogging;time:8,59;distance:23") == 23000

assert jogging.parse_time("jogging;time:88,05;distance:2") == 5285
assert jogging.parse_time("jogging;time:73,00;distance:12") == 4380
assert jogging.parse_time("jogging;time:1,59;distance:5.4") == 119
assert jogging.parse_time("jogging;time:13,16;distance:7") == 796
assert jogging.parse_time("jogging;time:125,32;distance:3") == 7532