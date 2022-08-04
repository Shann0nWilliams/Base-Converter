#Shannon_Williams_35855916

def dec_to_hex(n):
    if n < 10:
        return str(n)
    elif n == 10:
        return "A"
    elif n == 11:
        return "B"
    elif n == 12:
        return "C"
    elif n == 13:
        return "D"
    elif n == 14:
        return "E"
    elif n == 15:
        return "F"


def dec_to_bin(val):
    if val <= 0:
        return ""
    else:
        return dec_to_bin(val//2) + str(val % 2)


def dec_to_oct(val):
    if val <= 0:
        return ""
    else:
        return dec_to_oct(val//8) + str(val % 8)


dec_num = int(input("Enter decimal number to convert to base: "))
base_num = int(input("Enter base for conversion: "))

while base_num == 2:
    print("    ___")
    print(base_num, "|",dec_num)
    print("Base",base_num,"value of ",dec_num," = ",(dec_to_bin(dec_num)))
    break
while base_num == 8:
    print("    ___")
    print(base_num, "|",dec_num)
    print("Base", base_num, "value of ",dec_num, " = ",(dec_to_oct(dec_num)))
    break
while base_num == 16:
    print("    ___")
    print(base_num,"|",dec_num)
    print("Base", base_num,"value of", dec_num, "= " + str(dec_num//16) + str(dec_to_hex(dec_num%16)))

    break
