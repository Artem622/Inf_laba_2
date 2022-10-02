inverse = [3, 1, 5, 0, 4, 2, 6]

def checkMess(mess):
    mess = list(map(int, mess))
    r1 = mess[0]
    r2 = mess[1]
    r3 = mess[3]
    i1 = mess[2]
    i2 = mess[4]
    i3 = mess[5]
    i4 = mess[6]
    r1_check = (i1 + i2 + i4) % 2
    r2_check = (i1 + i3 + i4) % 2
    r3_check = (i2 + i3 + i4) % 2
    s1 = (r1_check + r1) % 2
    s2 = (r2_check + r2) % 2
    s3 = (r3_check + r3) % 2
    check = int(str(s1) + str(s2) + str(s3), 2)
    if (check != 0):
        print("Ошибка в ", inverse[check - 1] + 1, "бите")
        if (mess[inverse[check - 1]] == 0):
            mess[inverse[check - 1]] = 1
        else:
            mess[inverse[check - 1]] = 0
    else:
        print("Ошибок нет!")

    mess = list(map(str, mess))[2:]
    mess = ''.join(mess[0:1]) + ''.join(mess[2:])
    return mess

mess = str(input())
print("правильное сообщение: " ,checkMess(mess))
