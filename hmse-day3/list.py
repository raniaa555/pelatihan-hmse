#Contoh sederhana pembuatan list pada bahasa pemrograman python
list1 = ['kimia', 'fisika', 1993, 2017]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list = [[1, 2, 3], ['satu', 'dua', [4,6,['lima']], 'tiga']]

print(list1[2])
print(list[-1][-1][-1][0])

list1 = ['kimia', 'fisika', 1993, 2017]
list2 = [2,4,6,8,3,2,4,5,1,7,9,8,6,0] 

list1[2] = 2000
list1.append("budi")
list1.insert(2, "tess")
list1.remove("tess")
del list1[2]
print(list1)
list2.sort()
print(list2)
