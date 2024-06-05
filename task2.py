print('enter first number')
a=int(input())
print('enter second number')
b=int(input())
print('enter the operator')
c=input()
d=0
if c=='+':
    d=a+b
elif c=='-':
    d=a-b
elif c=='*':
    d=a*b
elif c=='/':
    d=a/b
print(a,c,b,'=',d)
