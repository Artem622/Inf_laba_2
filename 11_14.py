inverse = [7, 3, 11, 1, 9, 5, 13, 0, 8, 4, 12, 2, 10, 6, 14]

def checkMess(mess):
    mess = list(map(int, mess))
    r1 = mess[0]
    r2 = mess[1]
    r3 = mess[3]
    r4 = mess[7]
    i1 = mess[2]
    i2 = mess[4]
    i3 = mess[5]
    i4 = mess[6]
    i5 = mess[8]
    i6 = mess[9]
    i7 = mess[10]
    i8 = mess[11]
    i9 = mess[12]
    i10 = mess[13]
    i11 = mess[14]
    r1_check = (i1 + i2 + i4 + i5 + i7 + i9 + i11)%2
    r2_check = (i1 + i3 + i4 + i6 + i7 + i10 + i11)%2
    r3_check = (i2 + i3 + i4 + i8 + i9 + i10 + i11)%2
    r4_check = (i5 + i6 + i7 + i8 + i9 + i10 +i11)%2
    s1 = (r1_check + r1) % 2
    s2 = (r2_check + r2) % 2
    s3 = (r3_check + r3) % 2
    s4 = (r4_check + r4) % 2
    check = int(str(s1) + str(s2) + str(s3) +str(s4), 2)

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
    mess = ''.join(mess[0:4]) + ''.join(mess[5:])
    return mess

mess = str(input())
print("правильное сообщение: " ,checkMess(mess))