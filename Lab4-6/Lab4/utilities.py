def compareDates(date1, date2):
    '''
    Compara doua date calendaristice.
    date1 - data, touple de forma (zi,luna,an) - zi,luna,an numere intregi
    date2 - data, touple de forma (zi,luna,an) - zi,luna,an numere intregi
    return - -1 <=> date1 < date2
              0 <=> date1 = date2
              1 <=> date1 > date2
    '''
    if date1[2] < date2[2]:
        return -1
    elif date1[2] > date2[2]:
        return 1
    elif date1[1] < date2[1]:
        return -1
    elif date1[1] > date2[1]:
        return 1
    elif date1[0] < date2[0]:
        return -1
    elif date1[0] > date2[0]:
        return 1
    else:
        return 0
