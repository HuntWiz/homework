n = input()
paper = []
has = True

def printmas():
    for i in paper:
        for j in range(len(i)):
            print(i[j], end='')


for i in range(1, int(n)):
    for j in range(2, int(n)):
        if int(n) % (i + j) == 0:
            for k in paper:
                if [j, i] == k or j == k[1] or j == i:
                    has = False
            if has:
                paper.append([i, j])

        has = True



printmas()
