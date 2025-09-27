str1 = input()
str2 = input()

lcs = [[''] * (len(str2) + 1) for _ in range((len(str1) + 1))]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + str1[i - 1]
        elif len(lcs[i - 1][j]) > len(lcs[i][j - 1]):
            lcs[i][j] = lcs[i - 1][j]
        else:
            lcs[i][j] = lcs[i][j - 1]

print(lcs[len(str1)][len(str2)])
