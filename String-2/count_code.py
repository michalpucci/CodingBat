#
# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
#
#
# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(strw):
    strw = list(strw)
    for i in range(len(strw) - 2):
        if strw[i] == "o" and strw[i + 2] == "e":
            strw[i + 1] = "d"
    strw = "".join(strw)
    return strw.count("code")

