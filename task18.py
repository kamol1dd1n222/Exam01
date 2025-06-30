sonlar = [45, 12, 78, 34, 89, 23]
max_son = sonlar[0]
min_son = sonlar[0]
for i in range(2,len(sonlar)):
    if sonlar[i] > max_son:
        max_son = sonlar[i]
    elif sonlar[i] < min_son:
        min_son = sonlar[i]
print(f"Eng katta son: {max_son}, Eng kichik son: {min_son}")    
