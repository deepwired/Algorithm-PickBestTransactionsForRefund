__author__ = 'deepsinghbaweja'
import copy

#Algorithm to select the correct transaction

def optimizerA(total_amount_to_refund,total_amount_to_refund_A,transactions_A,list_values_A,list_index_A):
    for i in range(0, len(transactions_A)):
        flaga = 0;
        flagd = 0;
        donea = 0;
        if sum(list_values_A) >= total_amount_to_refund:
            donea = 1;
        elif transactions_A[i] == total_amount_to_refund_A:
            #add to list
            list_values_A.append(transactions_A[i])
            list_index_A.append(i)
            total_amount_to_refund_A -= transactions_A[i]
            flaga = 1;
            #donea = 1
            #removing from original
            del transactions_A[i]

        elif transactions_A[i] > total_amount_to_refund_A:
            if i==0:
                list_values_A.append(transactions_A[i])
                list_index_A.append(i)
                total_amount_to_refund_A -= transactions_A[i]
                donea = 1;
                #removing from original
                del transactions_A[i-1]
            else:
                #add to list
                list_values_A.append(transactions_A[i-1])
                list_index_A.append(i-1)
                total_amount_to_refund_A -= transactions_A[i-1]
                flaga = 1;
                #removing from original
                del transactions_A[i-1]

        elif i == len(transactions_A)-1:
            #add to list
            list_values_A.append(transactions_A[i])
            list_index_A.append(i)
            total_amount_to_refund_A -= transactions_A[i]
            flaga = 1;
            #removing from original
            del transactions_A[i]

        if flaga == 1:
            optimizerA(total_amount_to_refund, total_amount_to_refund_A, transactions_A, list_values_A,list_index_A)
        elif donea == 1:
            return [sum(list_values_A), list_values_A, list_index_A]
        # print "---------------------------------------"
        # print str(donea)+"--"+str(flaga)
        # print str(sum(list_values_A))+"=="+str(list_values_A)
        # print list_index_A
        # print "---------------------------------------"
    return [sum(list_values_A), list_values_A, list_index_A]

def optimizerD(total_amount_to_refund, total_amount_to_refund_D, transactions_D, list_values_D, list_index_D):
    for i in range(0, len(transactions_D)):
        flaga = 0;
        flagd = 0;
        donea=0;
        #print "SUM :"+str(sum(list_values_D))
        if sum(list_values_D) >= total_amount_to_refund:
            #print 1
            donea=1;
        elif float(transactions_D[i]) <= float(total_amount_to_refund_D):
            #add to list
            #print 2
            #print str(transactions_D[i]) +"<="+ str(total_amount_to_refund_D)
            if i==0:
                i=1;
            list_values_D.append(transactions_D[i-1])
            list_index_D.append(i-1)
            total_amount_to_refund_D -= transactions_D[i-1]
            flaga = 1;
            #removing from original
            del transactions_D[i-1]
        elif i == len(transactions_D)-1:
            #print "i="+str(i)
            #print 3
            #add to list
            list_values_D.append(transactions_D[i])
            list_index_D.append(i)
            total_amount_to_refund_D -= transactions_D[i]
            flaga = 1;
            #removing from original
            del transactions_D[i]

        if flaga == 1:
            optimizerD(total_amount_to_refund, total_amount_to_refund_D, transactions_D, list_values_D, list_index_D)
        elif donea == 1:
            return [sum(list_values_D), list_values_D, list_index_D]
        # print "---------------------------------------"
        # print str(donea)+"--"+str(flaga)
        # print str(sum(list_values_A))+"=="+str(list_values_A)
        # print list_index_A
        # print "---------------------------------------"
    return [sum(list_values_D),list_values_D, list_index_D]

def optimizer(transactions, refund):
    transactions_A = copy.deepcopy(transactions)
    list_values_A = []
    list_index_A = []
    transactions_D = copy.deepcopy(transactions)
    list_values_D = []
    list_index_D = []
    transactions_D.reverse()
    A = optimizerA(refund, refund, transactions_A, list_values_A,list_index_A)
    D = optimizerD(refund, refund, transactions_D, list_values_D,list_index_D)
    print A
    print D
    print "#####"
    if A[0]-refund < D[0]-refund:
        print "A is better"
    else:
        print "D is better"

transactions = [100.0, 200.6, 700.2, 750.5, 820.5, 900.4, 900.10, 1010.32, 1100.7, 1222.0]
optimizer(transactions, 900)