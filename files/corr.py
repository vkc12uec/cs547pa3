from math import *
import sys

def read_averages():
    averages = []
    ip = open("average.txt", "r")
    averages = ip.read().strip().split()
    ip.close()
    print "here2"
    print "averages.length = "+str(len(averages))
    print averages[3]
    print averages[1]
    return averages

# read the test file	test5.txt
def read_test5(trainlol):     #input is listoflist
    lines = []
    ip = open ("test5.txt", "r")
    lines = ip.readlines()
    ip.close()

    test5dict = {}      # whole info in this dict
    pid_avg = {}
    pid_nzeros = {}

    for line in lines:
        tmp = line.strip().split()
        pid = tmp[0]

        if pid in test5dict.keys():
    		test5dict[pid].append(str(tmp[1] + "," + tmp[2]))   # movie , rating
        else:
            test5dict[pid] = [str(tmp[1] + "," + tmp[2])]

        if pid in pid_avg.keys():
            pid_avg[pid] += int(tmp[2])
        else:
            pid_avg[pid] = int(tmp[2])

        if int(tmp[2]) == 0:
            if pid in pid_nzeros:
                pid_nzeros[pid] += 1
            else:
                pid_nzeros[pid] = 1

    print " ~~~ " + str(test5dict["201"])

        # find the avg. of the test ratings and store like: pid => average
    for pid in pid_avg.keys():
        pid_avg[pid] = float(pid_avg[pid]) / 5

    print "here1"
    print " ~~~ " + str(pid_avg["201"])     #correct
    print " ~~~ " + str(pid_avg["202"])
    print " ~~~ " + str(pid_avg["207"])

    averages = []
    averages = read_averages()

    wvalues = {}    # user 201  : list of w values for user 1-200
    wuut = []   # list of list

    for intpid in range(201,301):      #test5dict.keys():
        tmp_list = []
        for train_user in range(0,200):     # 0 to 199
            movieid = 0
            num_sum = 0
            sq_numd1 = 0
            sq_numd2 = 0
            for i in range (0,5):
                pid = str(intpid)
                #print "triplet = %d %d %d" % (intpid, train_user, i)
                #print test5dict[pid][i]
                (movieid, rating) = test5dict[pid][i].split(",")
                movieid = int (movieid) #test5dict[pid][i].split(",")[0])
                rating = int (rating)   #test5dict[pid][i].split(",")[1])
                #print ("movie id %d and rating %d") % (movieid, rating)

                numd1 =  float(rating - pid_avg[str(intpid)])
                numd2 = float(trainlol[train_user][movieid]) - float(averages[train_user])
                #print "numd1 || numd2 " + str(numd1) + " " + str(numd2)
                if numd1 == 0:
                    numd1 = 1
                if numd2 == 0:
                    numd2 = 1
                #print "numd1 || numd2 " + str(numd1) + " " + str(numd2)
                #print "culprit = "+str(pid_avg[str(intpid)])
                num_sum += (numd1*numd2)    # numerator sums
                sq_numd1 += numd1*numd1
                sq_numd2 += numd2*numd2

            Wai = float(num_sum)/sqrt(sq_numd1*sq_numd2)     # w(a,i) test user a, v/s train user i
            print "triplet = %d %d %f" % (intpid, train_user, Wai)
            tmp_list.append(str(Wai))
        wuut.append(tmp_list)       # testuser 201 [list of 1-200] .... .so on

    #sys.exit()
    print "doom"
    op = open("doom", 'w')
    for i in wuut:
        op.write(str(" || ".join(i)))
    op.close()

    sys.exit()

def read_training():
    ip = open ("train.txt", "r")
    stri = ip.readline()
    stri.strip()	# remove newlines/blanks

    whole_list = stri.split()
    wlist = []
    wlist = whole_list
    print "len = "+str(len(whole_list))
    #print "len = "+str(len(wlist))

    person_id = 1
    temp_list = []
    x = 0
    mydict = {}
    listoflist = []

    for w in whole_list:
    	temp_list.append(int(w))
    	x = x+1
        if x == 1000:
            listoflist.append(temp_list)
            mydict[person_id] = temp_list            # this will be a list of rating with columns as movieid
            person_id = person_id + 1
            temp_list = []
            x = 0

    """print "list of list info"
    print len(listoflist)
    print len(listoflist[0])
    print len(listoflist[198])"""
    #sys.exit()

    findavgRoot(mydict)
    return listoflist

def findavgRoot(mydict):
    agv_list = []
    sqrt_list = []
    for k, v in mydict.items():
    	#print str (k) + " == " + str(len(v))
    	sum_rating = 0
    	sum_squares = 0
        nzero = 0
    	for rating in v:
            if rating != 0:
                sum_rating = sum_rating + int (rating)
                sum_squares = sum_squares + ( int (rating) * int (rating) )
                nzero += 1
    	average = float(sum_rating) / nzero
    	agv_list.append(str(average))				#avg
    	sqrt_list.append(str(sqrt(sum_squares)))		#sqrt

    op = open ("average.txt", "w")
    op.write(" ".join(agv_list))
    op.close()
    op = open ("sqrt.txt", "w")
    op.write(" ".join(sqrt_list))
    op.close()

def callme():
    listoflist = [] #mydict = {}
    listoflist = read_training()
    #sys.exit()
    #mydict = read_training()
    read_test5(listoflist)


if __name__ == '__main__':
    callme()
    #read_training()
    #read_test5()
