import random
print('PASSWORD GENERATOR')
print('Enter the length of the password')
a=int(input())
while (a<8):
    print('Weak length for a password enter a length greater than 8')
    a=int(input())
l=['!','@','#','$','%','^','&','*','(',')']
alpha1=list('abcdefghijklmnopqrstuvwxyz')
Alpha1=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
digi=list('0123456789')
r=[]
b=a*20//100
c=a*30//100
d=a*20//100
e=a-b-c-d

for i in range(b):
    r.append(random.choice(Alpha1))
for i in range(c):
    r.append(random.choice(digi))
for i in range(d):
    r.append(random.choice(l))
for i in range(e):
    r.append(random.choice(alpha1))
random.shuffle(r)
r1=''.join(r)
print(r1)

