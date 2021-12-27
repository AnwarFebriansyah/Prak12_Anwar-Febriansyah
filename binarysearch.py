def binary_search(list, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if list[mid] == x:
            return mid
        elif list[mid] > x:
            return binary_search(list, l, mid-1, x)
        else:
            return binary_search(list, mid + 1, r, x)
    else:
        return -1
list = list()
print("BINARY SEARCH")
n = int(input("Masukkan jumlah angka pada List : "))
for i in range(n):
    list.append(int(input("Angka ke-"+str(i+1)+": ")))
print("\nList angka -> ",list)
key = int(input("Masukkan angka yang dicari : "))
idx = binary_search(list, 0, len(list)-1, key)
print("Hasil Linear Search -> "+("Tidak Ditemukan" if idx == -1 else "Ditemukan ( di index "+str(idx)+" )"))
