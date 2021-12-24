def linear_search(key, list):
    for i in list:
        if i == key:
            return 1
    return 0
list = list()
print("LINEAR SEARCH")
n = int(input("Masukkan jumlah angka pada List : "))
for i in range(n):
    list.append(int(input("Angka ke-"+str(i+1)+": ")))
print("\nList angka -> ",list)
key = int(input("Masukkan angka yang dicari : "))
print("Hasil Linear Search -> "+("Ditemukan" if linear_search(key,list) == 1 else "Tidak Ditemukan"))

