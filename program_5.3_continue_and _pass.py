# CONTINUE,PASS,BREAK

#pass → dia berfungsi sebagai dummy, tidak akan dieksekusi 

angka = 0 

while angka < 5:
    angka = angka + 1
    print(f'angka sekarang → {angka}') # aksi 1

    if(angka == 3): 
        print ('nice')
        continue  # akan membuat loop meloncat ke step selanjutnya 
    print ('whassup') # aksi 2

print ('finish')




for i in range(1, 6):
    if i == 3:
        continue
    print(i)