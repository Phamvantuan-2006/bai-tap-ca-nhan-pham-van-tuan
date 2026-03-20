# Nhập chuỗi nhị phân (chỉ gồm 0 và 1)
s = input("Nhap chuoi nhi phan: ")

# Khởi tạo kết quả
decimal = 0

# Duyệt từng ký tự trong chuỗi
for ch in s:
    # Chuyển ký tự '0' hoặc '1' sang số
    bit = int(ch)
    
    # Nhân kết quả hiện tại với 2 rồi cộng bit
    decimal = decimal * 2 + bit

# In kết quả thập phân
print("Tri thap phan:", decimal)
