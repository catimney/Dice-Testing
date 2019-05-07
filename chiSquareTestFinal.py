import csv
import numpy as np
from scipy import stats

with open('C:\\Users\\Cori\\Desktop\\Spring \'19\\Math Research\\diceData3.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    test1 = []

    
    for row in readCSV:
        dice1 = row[1]

        test1.append(dice1)
        
    r1 = []
  
    r1.append(test1.count('1'))

    r2 = []
    r2.append(test1.count('2'))

    r3 = []
    r3.append(test1.count('3'))

    r4 = []
    r4.append(test1.count('4'))
    


    all = np.array([test1.count('1'), test1.count('2'), test1.count('3'), test1.count('4')])
    
##    chi2_stat, p_val, dof, ex = stats.chi2_contingency(test)
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

   # print(stats.chisquare(f_obs=r1))

    print(stats.chisquare(f_obs=all))
    
    print(all)
    
    #print(test)
    
    
   
        
        
