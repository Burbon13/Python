from domain.transactions import *
from domain.utils import *

#t1 = [{'day': 22,'amount' : 2200,'ttype' : 0},{'day': 15,'amount' : 120,'ttype' : 1},
#     {'day': 4, 'amount' : 1220, 'ttype' : 0}, {'day': 30,'amount' : 330,'ttype' : 1},
#      {'day' : 26, 'amount' : 132, 'ttype' : 0}]

t1 = createDataBase()
addNewTransaction(createTransaction(22,2200,0),t1)
addNewTransaction(createTransaction(15,120,1),t1)
addNewTransaction(createTransaction(4,1220,0),t1)
addNewTransaction(createTransaction(30,330,1),t1)
addNewTransaction(createTransaction(26,132,0),t1)


#t2 = [{'day': 2,'amount' : 200,'ttype' : 0},{'day': 25,'amount' : 12,'ttype' : 1},
#      {'day': 14, 'amount' : 120, 'ttype' : 1}, {'day': 1,'amount' : 33330,'ttype' : 0},
#      {'day' : 3, 'amount' : 1332, 'ttype' : 0}, {'day': 22,'amount' : 123,'ttype' : 1}]

t2 = createDataBase()
addNewTransaction(createTransaction(2,200,0),t2)
addNewTransaction(createTransaction(25,12,1),t2)
addNewTransaction(createTransaction(14,120,1),t2)
addNewTransaction(createTransaction(1,33330,0),t2)
addNewTransaction(createTransaction(3,1332,0),t2)
addNewTransaction(createTransaction(22,123,1),t2)

#t3 = [{'day': 2,'amount' : 200,'ttype' : 0},{'day': 25,'amount' : 12,'ttype' : 1},
#      {'day': 2, 'amount' : 120, 'ttype' : 1}, {'day': 1,'amount' : 33330,'ttype' : 0},
#      {'day' : 3, 'amount' : 1332, 'ttype' : 0}, {'day': 2,'amount' : 123,'ttype' : 1}]

t3 = createDataBase()
addNewTransaction(createTransaction(2,200,0),t3)
addNewTransaction(createTransaction(25,12,1),t3)
addNewTransaction(createTransaction(2,120,1),t3)
addNewTransaction(createTransaction(1,33330,0),t3)
addNewTransaction(createTransaction(3,1332,0),t3)
addNewTransaction(createTransaction(2,123,1),t3)

#addNewTransaction

#t1_1 = [{'day': 22,'amount' : 2200,'ttype' : 0},{'day': 15,'amount' : 120,'ttype' : 1},
#      {'day': 4, 'amount' : 1220, 'ttype' : 0}, {'day': 30,'amount' : 330,'ttype' : 1},
#      {'day' : 26, 'amount' : 132, 'ttype' : 0}, {'day': 2, 'amount': 200, 'ttype': 0}]

t1_1 = createDataBase()
addNewTransaction(createTransaction(22,2200,0),t1_1)
addNewTransaction(createTransaction(15,120,1),t1_1)
addNewTransaction(createTransaction(4,1220,0),t1_1)
addNewTransaction(createTransaction(30,330,1),t1_1)
addNewTransaction(createTransaction(26,132,0),t1_1)
addNewTransaction(createTransaction(2,200,0),t1_1)

#changeTransaction

#t1_2 = [{'day': 15,'amount' : 120,'ttype' : 1},
#      {'day': 4, 'amount' : 1220, 'ttype' : 0}, {'day': 30,'amount' : 330,'ttype' : 1},
#      {'day' : 26, 'amount' : 132, 'ttype' : 0},{'day': 2, 'amount': 200, 'ttype': 1}]

t1_2 = createDataBase()
addNewTransaction(createTransaction(15,120,1),t1_2)
addNewTransaction(createTransaction(4,1220,0),t1_2)
addNewTransaction(createTransaction(30,330,1),t1_2)
addNewTransaction(createTransaction(26,132,0),t1_2)
addNewTransaction(createTransaction(2,200,1),t1_2)

#t2_1 = [{'day': 2,'amount' : 200,'ttype' : 0},{'day': 25,'amount' : 12,'ttype' : 1},
#      {'day': 14, 'amount' : 120, 'ttype' : 1}, {'day': 1,'amount' : 33330,'ttype' : 0},
#      {'day': 22,'amount' : 123,'ttype' : 1}, {'day': 2, 'amount': 200, 'ttype': 1}]

t2_1 = createDataBase()
addNewTransaction(createTransaction(2,200,0),t2_1)
addNewTransaction(createTransaction(25,12,1),t2_1)
addNewTransaction(createTransaction(14,120,1),t2_1)
addNewTransaction(createTransaction(1,33330,0),t2_1)
addNewTransaction(createTransaction(22,123,1),t2_1)
addNewTransaction(createTransaction(2,200,1),t2_1)

#deleteTransactions

#t3_1 = [{'day': 25,'amount' : 12,'ttype' : 1}, {'day': 1,'amount' : 33330,'ttype' : 0},
#      {'day' : 3, 'amount' : 1332, 'ttype' : 0}]

t3_1 = createDataBase()
addNewTransaction(createTransaction(25,12,1),t3_1)
addNewTransaction(createTransaction(1,33330,0),t3_1)
addNewTransaction(createTransaction(3,1332,0),t3_1)

#t3_2 = [{'day': 25,'amount' : 12,'ttype' : 1}, {'day': 1,'amount' : 33330,'ttype' : 0}]

t3_2 = createDataBase()
addNewTransaction(createTransaction(25,12,1),t3_2)
addNewTransaction(createTransaction(1,33330,0),t3_2)

#t3_3 = [{'day': 1,'amount' : 33330,'ttype' : 0}]

t3_3 = createDataBase()
addNewTransaction(createTransaction(1,33330,0),t3_3)

#deleteTransactionsBetweenDays

#t1_3 = [{'day': 22,'amount' : 2200,'ttype' : 0},{'day': 15,'amount' : 120,'ttype' : 1},
#       {'day': 30,'amount' : 330,'ttype' : 1},{'day' : 26, 'amount' : 132, 'ttype' : 0}]

t1_3 = createDataBase()
addNewTransaction(createTransaction(22,2200,0),t1_3)
addNewTransaction(createTransaction(15,120,1),t1_3)
addNewTransaction(createTransaction(30,330,1),t1_3)
addNewTransaction(createTransaction(26,132,0),t1_3)

#t1_4 = [ {'day': 30,'amount' : 330,'ttype' : 1},{'day' : 26, 'amount' : 132, 'ttype' : 0}]

t1_4 = createDataBase()
addNewTransaction(createTransaction(30,330,1),t1_4)
addNewTransaction(createTransaction(26,132,0),t1_4)

#deleteTransactionsOfOneType

#t1_5 = [{'day': 15,'amount' : 120,'ttype' : 1}, {'day': 30,'amount' : 330,'ttype' : 1}]

t1_5 = createDataBase()
addNewTransaction(createTransaction(15,120,1),t1_5)
addNewTransaction(createTransaction(30,330,1),t1_5)

#t1_6 = [{'day': 22,'amount' : 2200,'ttype' : 0},{'day': 4, 'amount' : 1220, 'ttype' : 0},
#      {'day' : 26, 'amount' : 132, 'ttype' : 0}]

t1_6 = createDataBase()
addNewTransaction(createTransaction(22,2200,0),t1_6)
addNewTransaction(createTransaction(4,1220,0),t1_6)
addNewTransaction(createTransaction(26,132,0),t1_6)

#searchTransactionsByAmount

#t1_7 = [{'day': 22,'amount' : 2200,'ttype' : 0},{'day': 4, 'amount' : 1220, 'ttype' : 0}]

t1_7 = createDataBase()
addNewTransaction(createTransaction(22,2200,0),t1_7)
addNewTransaction(createTransaction(4,1220,0),t1_7)

#t1_8 = [{'day': 22,'amount' : 2200,'ttype' : 0}]

t1_8 = createDataBase()
addNewTransaction(createTransaction(22,2200,0),t1_8)

#searchTransactionsByAmountAndDate

#t3_4 = [{'day': 2,'amount' : 200,'ttype' : 0}, {'day': 1,'amount' : 33330,'ttype' : 0},
#      {'day' : 3, 'amount' : 1332, 'ttype' : 0}]

t3_4 = createDataBase()
addNewTransaction(createTransaction(2,200,0),t3_4)
addNewTransaction(createTransaction(1,33330,0),t3_4)
addNewTransaction(createTransaction(3,1332,0),t3_4)

#t1_9 = [{'day': 22,'amount' : 2200,'ttype' : 0},{'day': 4, 'amount' : 1220, 'ttype' : 0}]

t1_9 = createDataBase()
addNewTransaction(createTransaction(22,2200,0),t1_9)
addNewTransaction(createTransaction(4,1220,0),t1_9)

#t1_10 = [{'day': 15,'amount' : 120,'ttype' : 1},{'day': 4, 'amount' : 1220, 'ttype' : 0}]

t1_10 = createDataBase()
addNewTransaction(createTransaction(15,120,1),t1_10)
addNewTransaction(createTransaction(4,1220,0),t1_10)

#t2_2 = [{'day': 1,'amount' : 33330,'ttype' : 0},{'day' : 3, 'amount' : 1332, 'ttype' : 0}]

t2_2 = createDataBase()
addNewTransaction(createTransaction(1,33330,0),t2_2)
addNewTransaction(createTransaction(3,1332,0),t2_2)

#searchByType

#t1_11 = [{'day': 15,'amount' : 120,'ttype' : 1},{'day': 30,'amount' : 330,'ttype' : 1}]

t1_11 = createDataBase()
addNewTransaction(createTransaction(15,120,1),t1_11)
addNewTransaction(createTransaction(30,330,1),t1_11)

#t1_12 = [{'day': 22,'amount' : 2200,'ttype' : 0},{'day': 4, 'amount' : 1220, 'ttype' : 0}, {'day' : 26, 'amount' : 132, 'ttype' : 0}]

t1_12 = createDataBase()
addNewTransaction(createTransaction(22,2200,0),t1_12)
addNewTransaction(createTransaction(4,1220,0),t1_12)
addNewTransaction(createTransaction(26,132,0),t1_12)

#sorted

#ts1 = [{'day': 4, 'amount' : 1220, 'ttype' : 0},{'day': 22,'amount' : 2200,'ttype' : 0}, {'day' : 26, 'amount' : 132, 'ttype' : 0}]

ts1 = createDataBase()
addNewTransaction(createTransaction(4,1220,0),ts1)
addNewTransaction(createTransaction(22,2200,0),ts1)
addNewTransaction(createTransaction(26,132,0),ts1)

#ts2 = [{'day': 15,'amount' : 120,'ttype' : 1},{'day': 30,'amount' : 330,'ttype' : 1}]

ts2 = createDataBase()
addNewTransaction(createTransaction(15,120,1),ts2)
addNewTransaction(createTransaction(30,330,1),ts2)

#ts3 = [{'day': 1,'amount' : 33330,'ttype' : 0},{'day': 2,'amount' : 200,'ttype' : 0},{'day' : 3, 'amount' : 1332, 'ttype' : 0} ]

ts3 = createDataBase()
addNewTransaction(createTransaction(1,33330,0),ts3)
addNewTransaction(createTransaction(2,200,0),ts3)
addNewTransaction(createTransaction(3,1332,0),ts3)

#ts4 = [{'day': 14, 'amount' : 120, 'ttype' : 1},{'day': 22,'amount' : 123,'ttype' : 1},{'day': 25,'amount' : 12,'ttype' : 1}]

ts4 = createDataBase()
addNewTransaction(createTransaction(14,120,1),ts4)
addNewTransaction(createTransaction(22,123,1),ts4)
addNewTransaction(createTransaction(25,12,1),ts4)

#last

#ttt1 = [{'day': 22,'amount' : 2200,'ttype' : 0},
#      {'day': 4, 'amount' : 1220, 'ttype' : 0}, {'day': 30,'amount' : 330,'ttype' : 1},
#      {'day' : 26, 'amount' : 132, 'ttype' : 0}]

ttt1 = createDataBase()
addNewTransaction(createTransaction(22,2200,0),ttt1)
addNewTransaction(createTransaction(4,1220,0),ttt1)
addNewTransaction(createTransaction(30,330,1),ttt1)
addNewTransaction(createTransaction(26,132,0),ttt1)

#ttt2 = [{'day': 22,'amount' : 2200,'ttype' : 0},{'day': 30,'amount' : 330,'ttype' : 1}]

ttt2 = createDataBase()
addNewTransaction(createTransaction(22,2200,0),ttt2)
addNewTransaction(createTransaction(30,330,1),ttt2)

#ttt3 = [{'day': 22,'amount' : 2200,'ttype' : 0}]

ttt3 = createDataBase()
addNewTransaction(createTransaction(22,2200,0),ttt3)