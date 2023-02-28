## juseok
def add_func(n1, n2) :
    res = n1 + n2
    return res

def minus_func(n1, n2) :
    res = n1 - n2
    return res

def both_func(n1, n2, s) :
    if(s=="+"):
        return add_func(n1, n2)
    if(s=="-"):
        return minus_func(n1, n2)
    if(s=="/"):
        return (n1/n2)
    if(s=="*"):
        return (n1*n2)
    else :
        print(n1+n2+"nonono")


## static var

num1, num2, result = 100, 200, 0;

## main()

print(both_func(num1, num2, "+"))
print(both_func(num1, num2, "-"))
print(both_func(num1, num2, "*"))
print(both_func(num1, num2, "/"))
