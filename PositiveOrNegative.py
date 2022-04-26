def number(n):
    if(n>0):
        return  positive(n)
    elif(n<0):
        return  negative(n)
    else:
        return neitherNegativeNorPositive(n)
def positive(n):
    return "positive"
def negative(n):
    return "negative"
def neitherNegativeNorPositive(n):
    return "neither negative nor positive"
n=int(input())
print(number(n))
