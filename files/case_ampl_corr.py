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

mypow = 1.7

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
                # wlist = wuut[testid-201]  list of w values
                t_sum = 0
                w_sum = 0
                for i in range(0,200):
                    w = wuut[testid-401][i]
                    #print "%s %s" % (i , movieid)
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
    write_to_file_list ("casresult20.txt", predicted_list)
    return

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
                    #print "%s %s" % (i , movieid)
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
    write_to_file_list ("casresult10.txt", predicted_list)
    return

def info(wuut, test5dict, pid_avg, averages, trainlol):
    print "avg leng = %s" % (len(averages))
    print "test5dict.keys leng = %s" % (len(test5dict.keys()))  # shud be 100 from 201 - 300
    for k in test5dict.keys():
        print "%s => %s" % (k, len(test5dict[k]))
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
                    #print "%s %s" % (i , movieid)
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
    write_to_file_list ("casresult5.txt", predicted_list)
    return

def sumList(wuut):
    elist = []
    for l in wuut:
        elist.append(sumofList(l))
    return elist

def sumofList(mylist):
    s = 0
    for item in mylist:
        if item < 0:
            s += -(item)
        else:
            s += item
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

    findavgRoot(mydict)
    findavgRoot1(listoflist)
    return listoflist

def findavgRoot1(listoflist):
    agv_list = []
    sqrt_list = []
    for i in listoflist:
		sum_r = 0
		nzero = 0
		for j in i:
			if j != 0:
				nzero += 1
		sum_r = sum(i)
		average = float(sum_r) / nzero
		agv_list.append(str(average))

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

def computefj (lol):
    elist = []
    transposedList = []
    transposedList = transposed(lol)
    for i in transposedList:
        nj = sum(x > 0 for x in i)
        if nj == 0:
            nj = 1
        elist.append(log(float(200/nj)))     #200 is total no. of users in db
    return elist

def transposed(lists):
   if not lists: return []
   return map(lambda *row: list(row), *lists)

# read the test file	test5.txt
def iuftest5(trainlol, fjarray):     #input is listoflist
    lines = []
    sumfj = sum(fjarray)

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

        # find the avg. of the test ratings and store like: pid => average
    for pid in pid_avg.keys():
        pid_avg[pid] = float(pid_avg[pid]) / 5

    averages = []
    averages = read_averages()

    wuut = []   # list of list

    for intpid in range(201,301):      #test5dict.keys():
        tmp_list = []
        for train_user in range(0,200):     # 0 to 199
            movieid = 0
            s1 =0
            s2 =0
            s3 =0
            s4 =0
            s5 =0
            for i in range (0,5):
                pid = str(intpid)
                (movieid, rating) = test5dict[pid][i].split(",")
                movieid = int (movieid) - 1
                rating = int (rating)
                if trainlol[train_user][movieid] == 0:
                    continue

                t1 = fjarray[movieid] * float(rating) * trainlol[train_user][movieid]
                t2 = fjarray[movieid] * float(rating)
                t3 = fjarray[movieid] * trainlol[train_user][movieid]
                t4 = fjarray[movieid] * float(rating) * float(rating)
                t5 = fjarray[movieid] * trainlol[train_user][movieid] * trainlol[train_user][movieid]
                s1 += t1
                s2 += t2
                s3 += t3
                s4 += t4
                s5 += t5
            bigNum = (sumfj*s1) - (s2*s3)
            bigU =  abs(s4 - (s2*s2))
            bigV =  abs(s5 - (s3*s3))
            bigDen = sumfj * sqrt (bigU * bigV)
            if bigDen == 0:
                bigDen = 1
            Wai = float(bigNum/bigDen)
            nWai = sign(Wai)*pow(Wai, mypow)
            tmp_list.append(nWai)
        wuut.append(tmp_list)       # testuser 201 [list of 1-200] .... .so on
                                    # [201, 10] wuut[201][10]
    predict5 (wuut, test5dict, pid_avg, averages, trainlol)
    #sys.exit()

def sign(number):
    return cmp(number,0)

def iuftest10(trainlol, fjarray):     #input is listoflist
    lines = []
    sumfj = sum(fjarray)

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
        pid_avg[pid] = float(pid_avg[pid]) / 5

    averages = []
    averages = read_averages()

    wuut = []   # list of list

    for intpid in range(301,401):      #test10dict.keys():
        tmp_list = []
        for train_user in range(0,200):     # 0 to 199
            movieid = 0
            s1 =0
            s2 =0
            s3 =0
            s4 =0
            s5 =0
            for i in range (0,10):
                pid = str(intpid)
                (movieid, rating) = test10dict[pid][i].split(",")
                movieid = int (movieid) - 1
                rating = int (rating)
                if trainlol[train_user][movieid] == 0:
                    continue

                t1 = fjarray[movieid] * float(rating) * trainlol[train_user][movieid]
                t2 = fjarray[movieid] * float(rating)
                t3 = fjarray[movieid] * trainlol[train_user][movieid]
                t4 = fjarray[movieid] * float(rating) * float(rating)
                t5 = fjarray[movieid] * trainlol[train_user][movieid] * trainlol[train_user][movieid]
                s1 += t1
                s2 += t2
                s3 += t3
                s4 += t4
                s5 += t5
            bigNum = (sumfj*s1) - (s2*s3)
            bigU =  abs(s4 - (s2*s2))
            bigV =  abs(s5 - (s3*s3))
            bigDen = sumfj * sqrt (bigU * bigV)
            if bigDen == 0:
                bigDen = 1
            Wai = float(bigNum/bigDen)
            nWai = sign(Wai)*pow(Wai, mypow)
            tmp_list.append(nWai)
        wuut.append(tmp_list)       # testuser 201 [list of 1-200] .... .so on
                                    # [201, 10] wuut[201][10]
    predict10 (wuut, test10dict, pid_avg, averages, trainlol)
    #sys.exit()

def iuftest20(trainlol, fjarray):     #input is listoflist
    lines = []
    sumfj = sum(fjarray)

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
        pid_avg[pid] = float(pid_avg[pid]) / 5

    averages = []
    averages = read_averages()

    wuut = []   # list of list

    for intpid in range(401,501):      #test20dict.keys():
        tmp_list = []
        for train_user in range(0,200):     # 0 to 199
            movieid = 0
            s1 =0
            s2 =0
            s3 =0
            s4 =0
            s5 =0
            for i in range (0,20):
                pid = str(intpid)
                (movieid, rating) = test20dict[pid][i].split(",")
                movieid = int (movieid) - 1
                rating = int (rating)
                if trainlol[train_user][movieid] == 0:
                    continue

                t1 = fjarray[movieid] * float(rating) * trainlol[train_user][movieid]
                t2 = fjarray[movieid] * float(rating)
                t3 = fjarray[movieid] * trainlol[train_user][movieid]
                t4 = fjarray[movieid] * float(rating) * float(rating)
                t5 = fjarray[movieid] * trainlol[train_user][movieid] * trainlol[train_user][movieid]
                s1 += t1
                s2 += t2
                s3 += t3
                s4 += t4
                s5 += t5
            bigNum = (sumfj*s1) - (s2*s3)
            bigU =  abs(s4 - (s2*s2))
            bigV =  abs(s5 - (s3*s3))
            bigDen = sumfj * sqrt (bigU * bigV)
            if bigDen == 0:
                bigDen = 1
            Wai = float(bigNum/bigDen)
            nWai = sign(Wai)*pow(Wai, mypow)
            tmp_list.append(nWai)
        wuut.append(tmp_list)       # testuser 201 [list of 1-200] .... .so on
                                    # [201, 10] wuut[201][10]
    predict20 (wuut, test20dict, pid_avg, averages, trainlol)
    #sys.exit()

def callme():
    listoflist = []
    listoflist = read_training()
    fjarray = [] # for storing fj values j = [1-1000]
    fjarray = computefj (listoflist)
    iuftest5(listoflist, fjarray)
    iuftest10(listoflist, fjarray)
    iuftest20(listoflist, fjarray)
    sys.exit()

if __name__ == '__main__':
    callme()

    """lol = [[1,2,3], [4,5,6], [7,8,9]]
    nlol = transposed(lol)
    for i in nlol:
        print str(i)

    sys.exit()"""
    """el = [1,2,3,0,5,6,0,0,9,0]
    print sum(x > 0 for x in el)
    sys.exit()"""