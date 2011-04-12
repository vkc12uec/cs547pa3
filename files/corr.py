#from Numeric import *
from math import *
import sys

# read the test file	test5.txt

test5dict = {}
lines = []
ip = open ("test5.txt", "r")
lines = ip.readlines()
ip.close()

#print lines[0].strip()
#print lines[1].strip()
# create dict
for line in lines:
	tmp = line.strip().split()
	if tmp[0] in test5dict.keys():
		test5dict[tmp[0]].append(tmp[1] + "," + tmp[2])
		continue
	test5dict[tmp[0]] = [tmp[1] + "," + tmp[2]]

for k in test5dict.keys():
	print str(k) + " "

sys.exit() 

ip = open ("train.txt", "r")
stri = ip.readline()
#print stri
stri.strip()	# remove newlines/blanks

whole_list = stri.split()
print "len = "+str(len(whole_list))

person_id = 0
temp_list = []
x = 0
mydict = {}

for w in whole_list:
	if x == 1000:
		mydict[person_id] = temp_list
		print "person id  ="+str(person_id) + "len ="+ str(len(temp_list))
		person_id = person_id + 1
		temp_list = []
		x = 0
	temp_list.append(w)
	x = x+1

agv_list = []

for k, v in mydict.items():
	#print str (k) + " == " + str(len(v))
	sum_rating = 0
	sum_squares = 0
	for rating in v:
		sum_rating = sum_rating + int (rating)
		sum_squares = sum_squares + ( int (rating) * int (rating) )
	
	average = float(sum_rating) / len(v)
	agv_list.append(str(average))				#avg
	agv_list.append(str(sqrt(sum_squares)))		#sqrt

op = open ("average.txt", "w")
op.write(" ".join(agv_list))
op.close()

#print " %s || %s " % (str(agv_list[0]), str(agv_list[1]))


