def checkio(number):
    string = str(number)

    result = 1

    for i in string:
        if int(i) != 0:
            result = result * int(i)

    return result

#1 převedu si int na string
#2 vytvořím result s počáteční hodnotou 1
#3 pro každé i ve stringu, pokud je toto i různé od nuly, result vynásobím tím i
#4 vracím result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1