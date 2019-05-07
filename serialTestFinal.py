import csv
import numpy as np
from scipy import stats


with open('C:\\Users\\Cori\\Desktop\\Spring \'19\\Math Research\\diceData3.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    test1 = []

    
    for row in readCSV:
        dice1 = row[1]

        test1.append(dice1)
        
    tuple1 = []
    for x in range(1, 4097,2):
        tuple1.append((test1[x], test1[x+1]))

    print(tuple1)
#count tuples
    r11 = tuple1.count(('1','1'))
    #print(r11)
    r12 = tuple1.count(('1','2'))
    #print(r12)

    r13 = tuple1.count(('1','3'))
    #print(r13)

    r14 = tuple1.count(('1','4'))
    #print(r14)

    r21 = tuple1.count(('2','1'))
    #print(r21)

    r22 = tuple1.count(('2','2'))
    #print(r22)

    r23 = tuple1.count(('2','3'))
    #print(r23)

    r24 = tuple1.count(('2','4'))
    #print(r24)

    r31 = tuple1.count(('3','1'))
    #print(r31)

    r32 = tuple1.count(('3','2'))
    #print(r32)

    r33 = tuple1.count(('3','3'))
    #print(r33)

    r34 = tuple1.count(('3','4'))
    #print(r34)

    r41 = tuple1.count(('4','1'))
    #print(r41)

    r42 = tuple1.count(('4','2'))
    #print(r42)

    r43 = tuple1.count(('4','3'))
    #print(r43)

    r44 = tuple1.count(('4','4'))
    #print(r44)


    test = np.array([r11, r12, r13, r14,
                     r21, r22, r23, r24,
                     r31, r32, r33, r34,
                     r41, r42, r43, r44])

##    
##    chi2_stat, p_val, dof, ex = stats.chi2_contingency(all)
##
##    print ("===Chi2 Stat===")
##    print (chi2_stat)
##    print ("\n")
##
##    print ("===Degrees of Freedom===")
##    print (dof)
##    print ("\n")
## 
##    print ("===P-Value===")
##    print (p_val)
##    print ("\n")
##
##    print ("===Contingency Table===")
##    print (ex)
    
    print(stats.chisquare(f_obs=test))
    print(test)

    #print(test1)
    #print(tuple1)
