import csv
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

with open('C:\\Users\\Cori\\Desktop\\Spring \'19\\Math Research\\diceData3.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    test1 = []

    
    for row in readCSV:
        dice1 = row[1]
        dice = int(dice1)
        test1.append(dice)
    tuple1 = []
    for x in range(1, 4098):
        tuple1.append(test1[x])
    tuple1.append(test1[0])

print(np.corrcoef(test1, tuple1))

m = -1.0/4097.0
s = (1.0/4097.0)*math.sqrt(4098*(4098-3.0)/(4099))
print((m-2*s), (m+2*s))

#print("dw of range=%f" % dw(np.arange(2000)))
#print("dw of rand=%f" % dw(np.random.randn(2000)))
#print("dw of rand=%f" % dw(test1, tuple1))
matplotlib.style.use('ggplot')
tuples = []
for x in range(0, 4098):
    tuples.append((test1[x], tuple1[x]))

r11 = tuples.count((1,1))
#print(r11)
r12 = tuples.count((1,2))
#print(r12)

r13 = tuples.count((1,3))
#print(r13)

r14 = tuples.count((1,4))
#print(r14)

r21 = tuples.count((2,1))
#print(r21)

r22 = tuples.count((2,2))
#print(r22)

r23 = tuples.count((2,3))
#print(r23)

r24 = tuples.count((2,4))
#print(r24)

r31 = tuples.count((3,1))
#print(r31)

r32 = tuples.count((3,2))
#print(r32)

r33 = tuples.count((3,3))
#print(r33)

r34 = tuples.count((3,4))
#print(r34)

r41 = tuples.count((4,1))
#print(r41)

r42 = tuples.count((4,2))
#print(r42)

r43 = tuples.count((4,3))
#print(r43)

r44 = tuples.count((4,4))
#print(r44)

test = np.array([r11, r12, r13, r14,
                     r21, r22, r23, r24,
                     r31, r32, r33, r34,
                     r41, r42, r43, r44])
x = [1,1,1,1,
     2,2,2,2,
     3,3,3,3,
     4,4,4,4]
y = [1,2,3,4,
     1,2,3,4,
     1,2,3,4,
     1,2,3,4]
print(test)
plt.scatter(x, y, s=test*10, alpha=0.5)



plt.xlim(0, 5)
plt.ylim(0, 5)

#plt.scatter(x, y, s=test, alpha=0.5)
plt.show()
