inverse = [3, 1, 5, 0, 4, 2, 6]

def checkMsg(msg):
    msg = list(map(int, msg))
    r1 = msg[0]
    r2 = msg[1]
    r3 = msg[3]
    i1 = msg[2]
    i2 = msg[4]
    i3 = msg[5]
    i4 = msg[6]
    r1_check = (i1 + i2 + i4) % 2
    r2_check = (i1 + i3 + i4) % 2
    r3_check = (i2 + i3 + i4) % 2
    s1 = (r1_check + r1) % 2
    s2 = (r2_check + r2) % 2
    s3 = (r3_check + r3) % 2
    check = int(str(s1) + str(s2) + str(s3), 2)
    if (check != 0):
        print("Ошибка: ", inverse[check - 1] + 1, "бит")
        if (msg[inverse[check - 1]] == 0):
            msg[inverse[check - 1]] = 1
        else:
            msg[inverse[check - 1]] = 0
    else:
        print("Ошибок нет!")

    msg = list(map(str, msg))[2:]
    msg = ''.join(msg[0:1]) + ''.join(msg[2:])
    return msg

msg = str(input())
print(checkMsg(msg))