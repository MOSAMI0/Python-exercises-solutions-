# برنامجًا لحساب مضروب عدد معين n باستخدام حلقة while.
o = int(input('Enter any number: '))
F = 1
s = o
while o > 0:
    F *= o
    o -= 1
print('مضروب العدد', s, 'هو', F)
