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
    for x in range(1, 4096,3):
        tuple1.append((test1[x], test1[x+1],  test1[x+2]))

    print(tuple1)
#count tuples
    r111 = tuple1.count(('1','1', '1'))
    r112 = tuple1.count(('1','1', '2'))
    r113 = tuple1.count(('1','1', '3'))
    r114 = tuple1.count(('1','1', '4'))
    
    #print(r11)
    r121 = tuple1.count(('1','2', '1'))
    r122 = tuple1.count(('1','2', '2'))
    r123 = tuple1.count(('1','2', '3'))
    r124 = tuple1.count(('1','2', '4'))
    
    
    #print(r12)

    r131 = tuple1.count(('1','3', '1'))
    r132 = tuple1.count(('1','3', '2'))
    r133 = tuple1.count(('1','3', '3'))
    r134 = tuple1.count(('1','3', '4'))
    
    #print(r13)

    r141 = tuple1.count(('1','4', '1'))
    r142 = tuple1.count(('1','4', '2'))
    r143 = tuple1.count(('1','4', '3'))
    r144 = tuple1.count(('1','4', '4'))
    #print(r14)

    r211 = tuple1.count(('2','1', '1'))
    r212 = tuple1.count(('2','1', '2'))
    r213 = tuple1.count(('2','1', '3'))
    r214 = tuple1.count(('2','1', '4'))
    
    #print(r21)

    r221 = tuple1.count(('2','2', '1'))
    r222 = tuple1.count(('2','2', '2'))
    r223 = tuple1.count(('2','2', '3'))
    r224 = tuple1.count(('2','2', '4'))

    #print(r22)

    r231 = tuple1.count(('2','3', '1'))
    r232 = tuple1.count(('2','3', '2'))
    r233 = tuple1.count(('2','3', '3'))
    r234 = tuple1.count(('2','3', '4'))
    
    #print(r23)

    r241 = tuple1.count(('2','4', '1'))
    r242 = tuple1.count(('2','4', '2'))
    r243 = tuple1.count(('2','4', '3'))
    r244 = tuple1.count(('2','4', '4'))
    
    #print(r24)

    r311 = tuple1.count(('3','1', '1'))
    r312 = tuple1.count(('3','1', '2'))
    r313 = tuple1.count(('3','1', '3'))
    r314 = tuple1.count(('3','1', '4'))
    
    #print(r31)

    r321 = tuple1.count(('3','2', '1'))
    r322 = tuple1.count(('3','2', '2'))
    r323 = tuple1.count(('3','2', '3'))
    r324 = tuple1.count(('3','2', '4'))
    
    #print(r32)

    r331 = tuple1.count(('3','3', '1'))
    r332 = tuple1.count(('3','3', '2'))
    r333 = tuple1.count(('3','3', '3'))
    r334 = tuple1.count(('3','3', '4'))
    #print(r33)

    r341 = tuple1.count(('3','4', '1'))
    r342 = tuple1.count(('3','4', '2'))
    r343 = tuple1.count(('3','4', '3'))
    r344 = tuple1.count(('3','4', '4'))
    #print(r34)

    r411 = tuple1.count(('4','1', '1'))
    r412 = tuple1.count(('4','1', '2'))
    r413 = tuple1.count(('4','1', '3'))
    r414 = tuple1.count(('4','1', '4'))
    #print(r41)

    r421 = tuple1.count(('4','2', '1'))
    r422 = tuple1.count(('4','2', '2'))
    r423 = tuple1.count(('4','2', '3'))
    r424 = tuple1.count(('4','2', '4'))
    
    #print(r42)

    r431 = tuple1.count(('4','3', '1'))
    r432 = tuple1.count(('4','3', '2'))
    r433 = tuple1.count(('4','3', '3'))
    r434 = tuple1.count(('4','3', '4'))
    #print(r43)

    r441 = tuple1.count(('4','4', '1'))
    r442 = tuple1.count(('4','4', '2'))
    r443 = tuple1.count(('4','4', '3'))
    r444 = tuple1.count(('4','4', '4'))
    
    #print(r44)


    test = np.array([r111, r112, r113, r114,
                     r121, r122, r123, r124,
                     r131, r132, r133, r134,
                     r141, r142, r143, r144,
                     r211, r212, r213, r214,
                     r221, r222, r223, r224,
                     r231, r232, r233, r234,
                     r241, r242, r243, r244,
                     r311, r312, r313, r314,
                     r321, r322, r323, r324,
                     r331, r332, r333, r334,
                     r341, r342, r343, r344,
                     r411, r412, r413, r414,
                     r421, r422, r423, r424,
                     r431, r432, r433, r434,
                     r441, r442, r443, r444])

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
