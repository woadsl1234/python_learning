def change(c,i):
    c = c.lower()
    num = ord(c)
    if num >= 97 and num <= 122:
        num = 97 + ((num - 97) + i) % 26
    return chr(num)


def kaisa_jiami(string,i):
    string_new = ''
    for s in string:
        string_new += change(s,i)
    print(string_new)
    return string_new

def kaisa_jiemi(string):
    for i in range(25):
        print('\n', i, '\n')
        i += 1
        kaisa_jiami(string,i)
str='hgame{The_qu8ck_br7wn_1x_jUmps_ovEr_a_La9y_dOg}'
str1='vuoas{Hvs_ei8qy_pf7kb_1l_xIadg_cjSf_o_Zo9m_rCu}'
kaisa_jiemi(str1)