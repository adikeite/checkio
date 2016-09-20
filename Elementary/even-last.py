def checkio(array):
    if len(array) == 0:
        return 0
    else:
        return sum(array[::2]) * array[-1]

#1 Pokud je řada čísel prázdná, vracím 0
#2 Jinak vracím sumu sudých čísel vynásobenou posledním číslem v seznamu

#l[::2] - vrací každé sudé číslo v seznamu
#l[1::2] - vrací každé liché číslo v senzamu

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"