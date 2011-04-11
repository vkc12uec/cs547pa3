
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

agv_list = {}

for k, v in mydict.items():
	print str (k) + " == " + str(len(v)
	"""
	average = float(sum(v)) / 1000	#len(v)
	agv_list[k] = average 
	"""

#print " %s || %s " % (str(agv_list[0]), str(agv_list[1]))
