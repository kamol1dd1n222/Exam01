fayl_name = input("Fayl name: ")
oxiri = fayl_name[-4:]
if oxiri == '.pdf':
    print("Fayl turi: pdf")
elif oxiri == '.docx':
    print("Fayl turi:  docx")
elif oxiri == 'txt':
    print("Fayl turi: txt")
else:
    print("Fayl turi: boshqa")