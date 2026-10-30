#PROGRAM 9.1 LIST
##  -- LIST ---

# KUMPULAN DATA NUMBERS
data_angka = {1,5,2,3}
print (data_angka)

#KUMPULAN DATA STRING
data_string = ["Heathcliff,Rodion,Ishmael"]
print (data_string)

# KUMPULAN DATA BOOLEAN
data_boolean = [True,False,True,True]
print (data_boolean)

# KUMPULAN CAMPURAN
data_campuran = [1,"Yi Sang",2,"Faust",True,"Don Quixote",False]
print (data_campuran)

# CARA ALTERNATIF MEMBUAT LIST
data_range = range (0,10,2) # range (start,stop,step)
print (data_range)
data_list = list (data_range)
print (data_list)

# MEMBUAT LIST DENGAN FOR LOP,LIST COMPREHENSION
list_for_if = [i for i in range(0,10) if i !%2 == 0]
print(list_for_if) 

list_for_if = [i for i in range(0,10) if i !%2 == 0]
print(list_for_if) 

list_for_if = [i for i in range(0,10) if i !%2 != 0]
print(list_for_if) 
