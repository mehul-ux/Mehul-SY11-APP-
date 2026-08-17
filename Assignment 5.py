def find_lcs(str1, str2):
    rows = len(str1)
    cols = len(str2)

    table = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

    for x in range(1, rows + 1):
        for y in range(1, cols + 1):
            if str1[x - 1] == str2[y - 1]:
                table[x][y] = table[x - 1][y - 1] + 1
            else:
                table[x][y] = max(table[x - 1][y], table[x][y - 1])

    x = rows
    y = cols
    result = []

    while x > 0 and y > 0:
        if str1[x - 1] == str2[y - 1]:
            result.append(str1[x - 1])
            x -= 1
            y -= 1
        elif table[x - 1][y] >= table[x][y - 1]:
            x -= 1
        else:
            y -= 1

    result = result[::-1]

    return table[rows][cols], result


first = "Mehul"
second = "Adani"

lcs_length, lcs_result = find_lcs(first, second)

print("LCS:", "".join(lcs_result))
print("Length:", lcs_length)
