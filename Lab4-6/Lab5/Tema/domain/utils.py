def createDataBase():
    return {'transactions' : [], 'undo_list' : [], 'operations' : 0}


def createTransaction(day ,amount, ttype):
    return {'day': day, 'amount': amount, 'ttype': ttype}


def getTransactions(data):
    return data['transactions']


def getUndo(data):
    return data['undo_list']


def getOperations(data):
    return data['operations']


def setOperations(data, value):
    data['operations'] = value


def getUndoType(undoObj):
    return undoObj[0]


def getUndoNr(undoObj):
    return undoObj[1]


def getUndoTransaction(undoObj):
    return undoObj[2]


def getDay(transaction):
    return transaction['day']


def getAmount(transaction):
    return transaction['amount']


def getType(transaction):
    return transaction['ttype']


def setDay(transaction, day):
    transaction['day'] = day


def setAmount(transaction, amount):
    transaction['amount'] = amount


def setType(transaction, ttype):
    transaction['ttype'] = ttype


def addTransaction(data, new_transaction):
    '''
        Adauga o tranzactie noua 'new_transaction' in baza de data 'data'
    '''
    transactions = getTransactions(data)
    undo_list = getUndo(data)
    transactions.append(new_transaction)
    setOperations(data,getOperations(data)+1)
    undo_list.append((0, getOperations(data), new_transaction))


def swapTransaction(data, old_transaction, new_transaction):
    '''
        Modifica o tranzactie 'old_transaction' din baza de date 'data' cu o
        tranzactie noua 'new_transaction'
    '''
    transactions = getTransactions(data)
    undo_list = getUndo(data)
    transactions.remove(old_transaction)
    transactions.append(new_transaction)
    setOperations(data, getOperations(data) + 1)
    undo_list.append((1, getOperations(data), old_transaction))
    undo_list.append((0, getOperations(data), new_transaction))


def transExists(data, trans):
    return trans in getTransactions(data)


def deleteTransactions(data, delete_list):
    '''
        Sterge tranzactiile date prin 'delete_list' din baza de data 'data'
    '''
    transactions = getTransactions(data)
    undo_list = getUndo(data)

    setOperations(data,getOperations(data)+1)
    for trans in delete_list:
        if trans in transactions:
            transactions.remove(trans)
            undo_list.append((1, getOperations(data), trans))

