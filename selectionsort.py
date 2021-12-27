list = list()
print("SELECTION SORT")
n = int(input("Masukkan jumlah angka pada List : "))
for i in range(n):
    list.append(int(input("Angka ke-"+str(i+1)+": ")))
print("\nList angka -> ",list)
for i in range(len(list)-1):
    min = i
    for j in range(i,len(list)):
        if list[min]>list[j]:
            min=j
    list[min], list[i] = list[i], list[min]
print("Hasil Selection Sort -> ",list)
