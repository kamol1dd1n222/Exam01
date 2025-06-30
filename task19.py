litters = input("Litters: ")
unli_lst = ['a','e','i','o','u']
litters = litters.lower()
litters_list = list()
for i in range(len(litters)):
    litters_list.append(litters[i])
print(litters_list)
unlilar_soni = 0
for i in range(len(litters_list)):
    if litters_list[i] in unli_lst:
        unlilar_soni += 1
print("Unlilar soni ==> ",unlilar_soni)