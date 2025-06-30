#chipta narxi 7 yoshgacha 50% chegirma, 8 - 15 yoshgacha 30 % chegirma
# undan kattalarga esa 15% chegirma bor
chipta_price =  100_000
age = int(input("Yoshingiz:  "))
if 0 < age <= 7:
    chipta_price = chipta_price - ((chipta_price / 100)) * 50
    print(f"Yakuniy narx: {chipta_price} (50% chegirma qo'llanildi)") 
elif 8 < age <= 15:
    chipta_price = chipta_price - ((chipta_price / 100)) * 30
    print(f"Yakuniy narx: {chipta_price} (30% chegirma qo'llanildi)")
elif age >= 16:
    chipta_price = chipta_price - ((chipta_price / 100)) * 15
    print(f"Yakuniy narx: {chipta_price} (15% chegirma qo'llanildi)")
else: 
    print("Siz noto'g'ri yosh kiritdingiz!")