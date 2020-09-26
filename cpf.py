"""
CPF = 168.995.350-09 - Example
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digit 1 = 0          #   Digit 2 = 9
"""

# Loop
while True:
    cpf = input("Type the CPF you want to check(without - or .):  ")
    new_cpf = cpf[:-2]
    reverse = 10
    total = 0

    for i in range(19):
        if i > 8:
            i -= 9

        total += int(new_cpf[i]) * reverse

        reverse -= 1
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            new_cpf += str(d)

    if cpf == new_cpf:
        print(f"{new_cpf} its valid")
    else:
        print(f"{new_cpf} its invalid")
