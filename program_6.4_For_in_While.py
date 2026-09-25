## --- For in While --- 

# for_in_while.py
sesi = 1

while sesi <= 2:  #Outer while: mengontrol nomor seszi
    print(f"Sesi ke-{sesi}:")

    # Inner for: mencetak nomor antrean pada sesi tersebut 
    for antrean in range(1, 4): 
        print(f"  Melayani pasien nomor: {antrean}")

    sesi += 1
    print("===")
        


