def getInt(text):
    '''
    Primeste input de la utilizator pana cand valoarea este un numar intreg
    text - string care se afiseaza la input
    return - prima valoare intreaga
    '''
    while True:
        try:
            command = int(input(text))
            return command
        except ValueError: #Exceptia este aruncata daca inputul nu este numar intreg
            print("Valoarea introdusa nu este un numar intreg")


def getYear(text):
    '''
    Primeste input de la utilizator pana cand valoarea este un an calendaristic valid
    text - string care se afiseaza la input
    return - primul an valid
    '''
    while True:
        year = getInt(text)
        if year > 1900 and year < 2018:
            return year
        print("Anul introdus nu este valid")


def getMonth(text):
    '''
    Primeste input de la utilizator pana cand valoarea este o luna calendaristica valida
    text - string care se afiseaza la input
    return - prima luna valida
    '''
    while True:
        month = getInt(text)
        if month > 0 and month < 13:
            return month
        print("Luna introdusa nu este valida")


def getDay(text, month, year):
    '''
    Primeste input de la utilizator pana cand valoarea este o zi calendaristica valida
    text - string care se afiseaza la input
    month, year - anul si luna (valori valide, numere intregi) in functie de care
    se verifica daca o zi este valida
    return - prima zi valida
    '''
    months_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    while True:
        day = getInt(text)
        if months_list[month] >= day and day > 0:
            return day
        elif month == 2 and year % 4 == 0 and day == 29:
            return day
        print("Ziua introdusa nu este valida")


def getDate(*text):
    '''
    Primeste input de la utilizator un an calendaristic valid.
    *text -  primeste o lista de stringuri care se afiseaza inaintea citirii
    return - data, touple (an,zi,luna)
    '''
    if len(text) > 0:
        for output_text in text:
            print(output_text)

    year = getYear("Introduceti anul")
    month = getMonth("Introduceti luna")
    day = getDay("Introduceti ziua", month, year)

    return (day,month,year)


def getAmount(text):
    '''
    Primeste input de la utilizator pana cand valoarea este o suma strict pozitiva
    text - string care se afiseaza la input
    return - prima suma pozitiva
    '''
    while True:
        amount = getInt(text)
        if amount > 0:
            return amount
        print("Nu puteti introduce o suma negativa sau nula")


def getType(text):
    '''
    Primeste input de la utilizator pana cand valoarea este un tip valid (0/1)
    text - string care se afiseaza la input
    return - primul tip valid
    '''
    while True:
        type = getInt(text)
        if type == 0 or type == 1:
            return type
        print("Nu puteti introduce alt tip de tranzactie inafara de 0 sau 1")


def getTransaction(text):
    '''
    Primeste input de la utilizator o tranzactie valida
    text - string care se afiseaza la input
    return - o tranzactie (touple de forma (data,suma,tip)
    iar data este un touple de forma (zi,luna,an))
    '''
    print(text)
    date = getDate()
    amount = getAmount("Introduceti suma de bani transferata")
    type = getType("Introduceti tipul de tranzactie (0 - Adaugare/1 - Retragere)")

    return (date,amount,type)


def printTransactions(trans_list):
    '''
    Afiseaza tranzactiile dintr-o lista
    trans_list - lista de tranzactii (o tranzactie este un touple de
    forma (data,suma,tip) iar data este un touple de forma (zi,luna,an))
    return - nimic
    '''
    if len(trans_list) == 0:
        print("Nu s-au gasit tranzactii dupa criteriile indicate")
        return

    for transaction in trans_list:
        print("Suma: %d" % (transaction[1]))
        print("Data: %d.%d.%d" % (transaction[0][0], transaction[0][1], transaction[0][2]))
        if transaction[2] == 0:
            print("Tip: adaugare bani\n")
        else:
            print("Tip: retragere bani\n")
