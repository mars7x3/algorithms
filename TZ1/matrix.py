import math


def search_word(xy: list, a: list, ):
    x = 1
    for n in xy[x:]:
        if len(n) == 1:
        
            if (n[0][0] == a[x-1][0][0] and (abs(n[0][1] - a[x-1][0][1]) == 1)) or (abs(n[0][0] - a[x-1][0][0]) == 1 and (n[0][1] == a[x-1][0][1])):
                a.append(n)
        if n == xy[-1]:
            for k in n:
                if (k[0] == a[-1][0][0] and (abs(k[1] - a[-1][0][1]) == 1)) or (abs(k[0] - a[-1][0][0]) == 1 and (k[1] == a[-1][0][1])):
                    a.append([k])

        elif len(n) > 1:
            for k in n:
                if (k[0] == a[x-1][0][0] and (abs(k[1] - a[x-1][0][1]) == 1)) or (abs(k[0] - a[x-1][0][0]) == 1 and (k[1] == a[x-1][0][1])):
                    if (k[0] == xy[x+1][0][0] and (abs(k[1] - xy[x+1][0][1]) == 1)) or (abs(k[0] - xy[x+1][0][0]) == 1 and (k[1] == xy[x+1][0][1])):
                        a.append([k])
        x += 1


def before_search_word(xy, a):
        x = 1
        for i in xy[0]:
            if (i[0] == xy[x][0][0] and (abs(i[1] - xy[x][0][1]) == 1)) or (abs(i[0] - xy[x][0][0]) == 1 and (i[1] == xy[x][0][1])):
                a.append([i])
            x += 1


def create_matrix(input1, input2):
    number = len(input1) ** 0.5
    list_index = []
    for i in input2:
        list_index.append([k for k,val in enumerate(input1) if val==i])

    x = []
    for i in list_index:
        x.append([math.trunc(n/number) for n in i])

    y = []
    for i in list_index:
        y.append([math.trunc(n%number) for n in i])

    xy = []
    for i, (x1, y1) in enumerate(zip(x, y)):
        xy.append([(x2, y2) for k, (x2, y2) in enumerate(zip(x1, y1))])

    a = []

    if len(xy[0]) == 1:
        a.append(xy[0])    
        search_word(xy, a)
    
    elif len(xy[0]) > 1:
        before_search_word(xy, a)
        search_word(xy, a)

    print(a)


create_matrix(input1=input("Введите первую строку: "), input2=input("Введите вторую строку: "))


