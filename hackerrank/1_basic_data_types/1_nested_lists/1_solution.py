if __name__ == '__main__':
    allList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        aStudent = [name, score]
        allList.append(aStudent)

allList.sort(key = lambda x: x[1])
secondList = []
highestScore = allList[0][1]
secondHighest = 0
i = 0
for student in allList:
    i = i + 1
    if student[1] != highestScore:
        secondHighest = student[1]
        break

# start from index i - 1
for student in allList[i - 1:]:
    if student[1] == secondHighest:
        secondList.append(student[0])
    else:
        break

secondList.sort()
print(*secondList, sep="\n")
