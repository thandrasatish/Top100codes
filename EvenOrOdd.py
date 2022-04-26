def number(n):
    if(n%2==0):
        return even(n)
    else:
        return odd(n)
def even(n):
    return True
def odd(n):
    return False
n=int(input())
if(number(n)==True):
    print("even")
else:
    print("odd")
