## --- OPERASI LIST --- 

# index 0(-3) 1(-2) 2(-1) 
data 1 = ["Binah","Carmen,"Ayin”] 
data 2 = ["Roland","Angelica,"Vergillius"]
data 3 = ["Callisto","Matthias,"Rien"] 

# mengambil data dari list 
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}") 

data_terakhir = data [-1]
print (f"data terakhir adalah = {data_terakhir}")

# mengambil info jumlah data dalam list
panjang_data = len (data)
print (f"panjang data = {panjang_data}")

# manipulasi data list 

# menambahkan item pada list sesuai posisi 
print (f"data sebelum ditambah =\n{data}")

#data.insert(posisi,item) 
data.insert (1,"Asep")
print (f"data ditambah lagi = \n {data}")

# menambah di akhir list 
data.apend ("Ririn")
print (f"data ditambah lagi = \n {data}")

# menambahkan list dengan list 
data_baru = ["Dante","Meursault","Gregor"]
data.extend (data_baru)
print (f"data gabungan  = \n{data}")

# menghapus data
data.remove ("Catherine")
print (f"data hapus = \n {data}")

# menghapus data palimhbelakang
data.pop ()
print (f"data akhir = \n {data}")
