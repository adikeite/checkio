def safe_pawns(pawns):
    pawns_indexes = set()  # vytvoř prázdnou množinu
    count = 0

    for p in pawns:
        row = int(p[1]) - 1  # "a3" -> 3 převeď na číslo
        col = ord(p[0]) - 97  # ord vraci ordinalni ASCII hodnotu, pro “a” to je 97
        pawns_indexes.add((row, col))  # do mnoziny pridej nactenou hodnotu “a3” jako (0, 2)

    for row, col in pawns_indexes:
        is_safe = any(((row - 1, col - 1) in pawns_indexes, (row - 1, col + 1) in pawns_indexes))
        if is_safe:
            count += 1

    return (count)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

#1 vytvořím prázdnou množinu
#2 vytvořím prázdný count (celkový počet safe pawns)
#3 získám indexové souřadnice (převedu rows i columns na čísla) figurek
#4 vytvořím si funkci is_safe, kde stanovím pravidlo, že safe je, pokud row - 1 a zároveň col - 1 nebo col + 1
#5 pokud je is_safe true, přičítám 1 do count
#6 vracím count