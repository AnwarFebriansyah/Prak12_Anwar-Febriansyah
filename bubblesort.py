list = list()
print("BUBBLE SORT")
n = int(input("Masukkan jumlah angka pada List : "))
for i in range(n):
    list.append(int(input("Angka ke-"+str(i+1)+": ")))
print("\nList angka -> ",list)
for i in range(len(list)):
    for j in range((len(list)-i-1)):
        if list[j]>list[j+1]:
             list[j], list[j+1] = list[j+1], list[j]
print("Hasil Selection Sort -> ",list)
