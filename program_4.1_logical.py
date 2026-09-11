# operasi logika atau boolean 

# not, or, and, xor 
print('===NOT===') 
a = True
b = not a
print('data a =', a)
print( '------------ NOT')
print('data b =', b)

# OR (jika salah satu true, maka hasilnya adalah true) print(‘===OR===’) 
print('===OR===')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)

# AND (jika dua buah nilai true, maka hasil true) print(‘===AND===’) 

a = false
b = false  
c = a and b
print(a, 'AND', b, '=', c)
a = false
b = true
c = a and b
print(a, 'AND', b, '=', c)
a = true
b = false
c = a and b
print(a, 'AND', b, '=', c)
a = true
b = true
c = a and b
print(a, 'AND', b, '=', c)

# XOR (akan true jika salah satu true, sisanya false) print(‘===XOR===’) 

a = false
b = false
c = a ^ b
print(a, 'XOR', b, '=', c)
a = false
b = true
c = a ^ b
print(a, 'XOR', b, '=', c)
a = true
b = false
c = a ^ b
print(a, 'XOR', b, '=', c)
a = true
b = true
c = a ^ b
print(a, 'XOR', b, '=', c)
