# Nhập hệ số a và b
a, b = map(float, input("Nhap a, b: ").split())

# Xét các trường hợp
if a == 0:
    if b == 0:
        # 0x + 0 = 0 → vô số nghiệm
        print("Phuong trinh vo so nghiem")
    else:
        # 0x + b = 0 (b ≠ 0) → vô nghiệm
        print("Phuong trinh vo nghiem")
else:
    # a ≠ 0 → có nghiệm duy nhất
    x = -b / a
    print("x =", x)
