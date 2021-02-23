inp_data = str(input().rstrip())

print(inp_data)

#二次関数の時のみとする -x^2+3x-2のような形

def bunkai(shiki):
    a = []
    b = []
    c = ""

    flg = 0

    for iv,it in enumerate(inp_data):
        print(iv,it)

        if iv != 0 and (it == "+" or it == "-"):
            flg += 1

        if flg == 0:
            a.append(it)

        if flg == 1:
            b.append(it)

        if flg == 2:
            c += it

    print(a,b,c)

    return a,b,c

a,b,c = bunkai(inp_data)

a_kei = ""
for ai in a: #aの系数をとります
    if ai == "^":
        break
    a_kei += ai

print(a_kei)

b_kei = ""

for bi in b:

    if not bi.isdigit() and (not bi == "+" and not bi == "-" ) :
        break

    b_kei += bi

print(b_kei)

b_int = int(b_kei)

print(b_int)

b_int *= b_int

_,_,c = bunkai(sabun)