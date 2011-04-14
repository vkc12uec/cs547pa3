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

def read_test20(trainlol):     #input is listoflist
    lines = []
    ip = open ("test20.txt", "r")
    lines = ip.readlines()
    ip.close()

    test20dict = {}      # whole info in this dict
    pid_avg = {}
    pid_nzeros = {}

    for line in lines:
        tmp = line.strip().split()
        pid = tmp[0]

        if pid in test20dict.keys():
    		test20dict[pid].append(str(tmp[1] + "," + tmp[2]))   # movie , rating
        else:
            test20dict[pid] = [str(tmp[1] + "," + tmp[2])]

        if pid in pid_avg.keys():
            pid_avg[pid] += int(tmp[2])
        else:
            pid_avg[pid] = int(tmp[2])

        if int(tmp[2]) == 0:
            if pid in pid_nzeros:
                pid_nzeros[pid] += 1
            else:
                pid_nzeros[pid] = 1

        # find the avg. of the test ratings and store like: pid => average
    for pid in pid_avg.keys():
        pid_avg[pid] = float(pid_avg[pid]) / 20

    averages = []
    averages = read_averages()

    wvalues = {}    # user 201  : list of w values for user 1-200
    wuut = []   # list of list

    for intpid in range(401,501):      #test20dict.keys():
        tmp_list = []
        for train_user in range(0,200):     # 0 to 199
            movieid = 0
            num_sum = 0
            sq_numd1 = 0
            sq_numd2 = 0
            for i in range (0,20):
                pid = str(intpid)
                (movieid, rating) = test20dict[pid][i].split(",")
                movieid = int (movieid) -1
                rating = float (rating)
                if trainlol[train_user][movieid] == 0:
                    continue

                numd1 =  float(rating - pid_avg[str(intpid)])
                numd2 = float(trainlol[train_user][movieid]) - float(averages[train_user])
                if numd1 == 0:
                    numd1 = 1
                if numd2 == 0:
                    numd2 = 1

                num_sum += (numd1*numd2)    # numerator sums
                sq_numd1 += numd1*numd1
                sq_numd2 += numd2*numd2

            if (sq_numd1 == 0 or sq_numd2 == 0):
                Wai = 0
            else:
                Wai = float(num_sum)/sqrt(sq_numd1*sq_numd2)     # w(a,i) test user a, v/s train user i
            tmp_list.append(Wai)
        wuut.append(tmp_list)       # testuser 201 [list of 1-200] .... .so on
                                    # [201, 10] wuut[201][10]

    #info (wuut, test20dict, pid_avg, averages, trainlol)
    predict20 (wuut, test20dict, pid_avg, averages, trainlol)
    #sys.exit()

def predict20(wuut, test20dict, pid_avg, averages, trainlol):
    predicted_list = []                 # 200+i v/s id      wuut[i-1][id]
    sumOfWs = []        # 401 to 500 , their w's added no sign
    sumOfWs = sumList(wuut)

    for testid in range (401,501):
        for entry in test20dict[str(testid)]:
            (movieid, rating) = entry.split(',')
            movieid = int(movieid) - 1
            rating = int(rating)
            if rating != 0:
                continue
            else:
                t_sum = 0
                w_sum = 0
                for i in range(0,200):
                    w = wuut[testid-401][i]

                    if trainlol[i][movieid] == 0:
                        continue
                    t_sum += float(w) * ( trainlol[i][movieid] - float(averages[i]) )
                pr_rating = float(pid_avg[str(testid)]) + float (t_sum)/sumOfWs[testid-401]
                #pr_rating = float(pid_avg[str(testid)]) + float (t_sum)/sumofList(wuut[testid-201])
                new_rating = int(round(pr_rating,0))
                if new_rating > 5:
                    new_rating = 5
                if new_rating < 1:
                    new_rating = 1
                predicted_list.append("%s %s %s" % (testid, movieid+1, new_rating))
    write_to_file_list ("mresult20.txt", predicted_list)
    return

def read_test10(trainlol):     #input is listoflist
    lines = []
    ip = open ("test10.txt", "r")
    lines = ip.readlines()
    ip.close()

    test10dict = {}      # whole info in this dict
    pid_avg = {}
    pid_nzeros = {}

    for line in lines:
        tmp = line.strip().split()
        pid = tmp[0]

        if pid in test10dict.keys():
    		test10dict[pid].append(str(tmp[1] + "," + tmp[2]))   # movie , rating
        else:
            test10dict[pid] = [str(tmp[1] + "," + tmp[2])]

        if pid in pid_avg.keys():
            pid_avg[pid] += int(tmp[2])
        else:
            pid_avg[pid] = int(tmp[2])

        if int(tmp[2]) == 0:
            if pid in pid_nzeros:
                pid_nzeros[pid] += 1
            else:
                pid_nzeros[pid] = 1

        # find the avg. of the test ratings and store like: pid => average
    for pid in pid_avg.keys():
        pid_avg[pid] = float(pid_avg[pid]) / 10

    averages = []
    averages = read_averages()

    wvalues = {}    # user 201  : list of w values for user 1-200
    wuut = []   # list of list

    for intpid in range(301,401):      #test10dict.keys():
        tmp_list = []
        for train_user in range(0,200):     # 0 to 199
            movieid = 0
            num_sum = 0
            sq_numd1 = 0
            sq_numd2 = 0
            for i in range (0,10):
                pid = str(intpid)
                #print "triplet = %d %d %d" % (intpid, train_user, i)
                #print test10dict[pid][i]
                (movieid, rating) = test10dict[pid][i].split(",")
                movieid = int (movieid) - 1
                rating = float (rating)
                if trainlol[train_user][movieid] == 0:
                    continue
                numd1 =  float(rating - pid_avg[str(intpid)])
                numd2 = float(trainlol[train_user][movieid]) - float(averages[train_user])

                if numd1 == 0:
                    numd1 = 1
                if numd2 == 0:
                    numd2 = 1

                num_sum += (numd1*numd2)    # numerator sums
                sq_numd1 += numd1*numd1
                sq_numd2 += numd2*numd2

            if (sq_numd1 == 0 or sq_numd2 == 0):
                Wai = 0
            else:
                Wai = float(num_sum)/sqrt(sq_numd1*sq_numd2)     # w(a,i) test user a, v/s train user i
            tmp_list.append(Wai)
        wuut.append(tmp_list)       # testuser 201 [list of 1-200] .... .so on
                                    # [201, 10] wuut[201][10]

    #info (wuut, test10dict, pid_avg, averages, trainlol)
    predict10 (wuut, test10dict, pid_avg, averages, trainlol)
    #sys.exit()

def predict10(wuut, test10dict, pid_avg, averages, trainlol):
    predicted_list = []                 # 200+i v/s id      wuut[i-1][id]
    sumOfWs = []        # 301 to 400 , their w's added no sign
    sumOfWs = sumList(wuut)

    for testid in range (301,401):
        for entry in test10dict[str(testid)]:
            (movieid, rating) = entry.split(',')
            movieid = int(movieid) - 1
            rating = int(rating)
            if rating != 0:
                continue
            else:
                # wlist = wuut[testid-201]  list of w values
                t_sum = 0
                w_sum = 0
                for i in range(0,200):
                    w = wuut[testid-301][i]

                    if trainlol[i][movieid] == 0:
                        continue
                    t_sum += float(w) * ( trainlol[i][movieid] - float(averages[i]) )
                pr_rating = float(pid_avg[str(testid)]) + float (t_sum)/sumOfWs[testid-301]
                #pr_rating = float(pid_avg[str(testid)]) + float (t_sum)/sumofList(wuut[testid-201])
                new_rating = int(round(pr_rating,0))
                if new_rating > 5:
                    new_rating = 5
                if new_rating < 1:
                    new_rating = 1
                predicted_list.append("%s %s %s" % (testid, movieid+1, new_rating))
    write_to_file_list ("mresult10.txt", predicted_list)
    return

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
    #write_dict_to_file (test5dict)
    #sys.exit()

        # find the avg. of the test ratings and store like: pid => average
    for pid in pid_avg.keys():
        pid_avg[pid] = float(pid_avg[pid]) / 5

    averages = []           # train averages
    averages = read_averages()

    wuut = []   # list of list  for user 201 - 300 columns =

    for intpid in range(201,301):      #test5dict.keys():
        tmp_list = []
        for train_user in range(0,200):     # 0 to 199
            movieid = 0
            num_sum = 0
            sq_numd1 = 0
            sq_numd2 = 0
            for i in range (0,5):
                pid = str(intpid)
                (movieid, rating) = test5dict[pid][i].split(",")
                movieid = int (movieid) - 1
                rating = float (rating)
                if trainlol[train_user][movieid] == 0:
                    continue
                numd1 =  float(rating - pid_avg[str(intpid)])
                numd2 = float(trainlol[train_user][movieid]) - float(averages[train_user])
                #print "numd1 || numd2 " + str(numd1) + " " + str(numd2)
                if numd1 == 0:
                    numd1 = 1
                if numd2 == 0:
                    numd2 = 1
                num_sum += (numd1*numd2)    # numerator sums
                sq_numd1 += numd1*numd1
                sq_numd2 += numd2*numd2

            if (sq_numd1 == 0 or sq_numd2 == 0):
                Wai = 0
            else:
                Wai = float(num_sum)/sqrt(sq_numd1*sq_numd2)     # w(a,i) test user a, v/s train user i
            tmp_list.append(Wai)
        wuut.append(tmp_list)       # testuser 201 [list of 1-200] .... .so on
                                    # [201, 10] wuut[201][10]

    #info (wuut, test5dict, pid_avg, averages, trainlol)
    predict5 (wuut, test5dict, pid_avg, averages, trainlol)
    return
    #sys.exit()

def predict5(wuut, test5dict, pid_avg, averages, trainlol):
    predicted_list = []                 # 200+i v/s id      wuut[i-1][id]
    sumOfWs = []        # 201 to 300 , their w's added no sign
    sumOfWs = sumList(wuut)

    for testid in range (201,301):      #301    200 - 300
        for entry in test5dict[str(testid)]:
            (movieid, rating) = entry.split(',')
            movieid = int(movieid) - 1
            rating = int(rating)
            if rating != 0:
                continue
            else:
                # wlist = wuut[testid-201]  list of w values
                t_sum = 0
                w_sum = 0
                for i in range(0,200):
                    w = wuut[testid-201][i]

                    if trainlol[i][movieid] == 0:
                        continue
                    t_sum += float(w) * ( trainlol[i][movieid] - float(averages[i]) )
                pr_rating = float(pid_avg[str(testid)]) + float (t_sum)/sumOfWs[testid-201]
                #pr_rating = float(pid_avg[str(testid)]) + float (t_sum)/sumofList(wuut[testid-201])
                new_rating = int(round(pr_rating,0))
                if new_rating > 5:
                    new_rating = 5
                if new_rating < 1:
                    new_rating = 1
                predicted_list.append("%s %s %s" % (testid, movieid+1, new_rating))
    write_to_file_list ("mresult5.txt", predicted_list)
    return

def write_dict_to_file(mydict):
    op = open ("dict", 'w')
    for key in mydict.keys():
        for values in mydict[key]:
            op.write(key + "=>" + values)
            op.write("\n")
    op.close()

def info(wuut, test5dict, pid_avg, averages, trainlol):
    return
    print "avg leng = %s" % (len(averages))
    print "test5dict.keys leng = %s" % (len(test5dict.keys()))  # shud be 100 from 201 - 300
    #for k in test5dict.keys():
        #print "%s => %s" % (k, len(test5dict[k]))
    print "wuut leng = %s" % (len(wuut))
    for i in wuut:
        if len(i) != 200:
            print 'smth is wrong2'

    print "pid_avg leng = %s" % (len(pid_avg))
    for i in pid_avg:
        if float(i) == 0:
            print 'smth is wrong1'

    print "trainlol leng = %s" % (len(trainlol))
    for i in range(0,len(trainlol)):
        if len(trainlol[i]) != 1000:
            print 'smth is wrong'

def sumList(wuut):
    elist = []
    for l in wuut:
        elist.append(sumofList(l))
    return elist

def sumofList(mylist):
    s = 0
    for item in mylist:
        s += abs(item)
        """
        if item < 0:
            s += -(item)
        else:
            s += item"""
    return s

def write_to_file_list(name, list):
    op = open (name, 'w')
    op.write("\n".join(list))
    op.close()

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
    #findavgRoot1(listoflist)
    #sys.exit()
    return listoflist

def findavgRoot1(lol):
    agv_list = []
    sqrt_list = []
    for i in lol:
        sum_r = sum(i)
        nzero = 0
        for j in i:
            if j != 0:
                nzero += 1
        average = float(sum_r) / nzero
    	agv_list.append(str(average))				#avg

    op = open ("lolaverage.txt", "w")
    op.write(" ".join(agv_list))
    op.close()

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
    """op = open ("sqrt.txt", "w")
    op.write(" ".join(sqrt_list))
    op.close()"""

import time

def callme():
    listoflist = [] #mydict = {}
    listoflist = read_training()
    #sys.exit()
    #mydict = read_training()
    t1 = time.time()
    read_test5(listoflist)
    read_test10(listoflist)
    read_test20(listoflist)
    t2 = time.time()
    print "time = " + str(t2-t1) + " seconds"

if __name__ == '__main__':
    callme()
    #read_training()
    #read_test5()
