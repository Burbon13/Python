from domain.utils import getAmount
from domain.utils import getDay
from domain.utils import getType
from domain.utils import setAmount
from domain.utils import setDay
from domain.utils import setType


def validateDay(day):
    '''
        Valideaza o zi
        day (string) - ziua
        Arunca eroare daca nu e valida
    '''
    errors = ''

    try:
        day = int(day)
        if day < 1 or day > 31:
            errors += 'Ziua nu este valida\n'
    except ValueError:
        errors += 'Ziua nu este valida.\n'

    if len(errors) > 0:
        raise ValueError(errors)


def validateType(ttype):
    '''
        Valideaza un tip
        ttype (string) - tip
        Arunca eroare daca nu e valid
    '''
    errors = ''

    try:
        ttype = int(ttype)
        if ttype != 0 and ttype != 1:
            errors += 'Tipul nu este valid\n'
    except ValueError:
        errors += 'Tipul nu este valid.\n'

    if len(errors) > 0:
        raise ValueError(errors)


def validateAmount(amount):
    '''
        Valideaza o suma
        amount (string) - suma
        Arunca eroare daca nu e valida
    '''
    errors = ''

    try:
        amount = int(amount)
        if amount < 1:
            errors += 'Suma nu este valida\n'
    except ValueError:
        errors += 'Suma nu este valida.\n'

    if len(errors) > 0:
        raise ValueError(errors)

def validateTransaction(transaction):
    '''
        Verifica daca o tranzactie e valida
        transaction - tranzactia
        Arunca eroare daca nu e valida
    '''

    validateDay(getDay(transaction))
    #transaction['day'] = int(getDay(transaction))
    setDay(transaction,int(getDay(transaction)))

    validateAmount(getAmount(transaction))
    #transaction['amount'] = int(getAmount(transaction))
    setAmount(transaction,int(getAmount(transaction)))

    validateType(getType(transaction))
    #transaction['ttype'] = int(getType(transaction))
    setType(transaction, int(getType(transaction)))