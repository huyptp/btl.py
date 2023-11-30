# Khai báo các thư viện cần thiết
import random
import datetime
import math

# Khai báo các hằng số
M = 10 
N = 10 
PHI_30_DAU = 50000 
PHI_30_TIEP = 30000 
bai_xe = [[0 for j in range(N)] for i in range(M)] # Mảng 2 chiều lưu trạng thái của bãi xe, 0 là chỗ trống, 1 là chỗ có xe
danh_sach_xe = []
#tạo biển số xe có 8 phần tư gồm 7 số và 1 chữ cái 
def tao_bien_so():
    bien_so = ""
    for i in range(2):
        bien_so += str(random.randint(0,9)) 
    bien_so += "-"
    bien_so += chr(random.randint(65,90)) 
    for i in range(5):
        bien_so += str(random.randint(0,9)) 
    return bien_so
# Hàm tìm một chỗ trống trong bãi xe
def tim_cho_trong():
    for i in range(M):
        for j in range(N):
            if bai_xe[i][j] == 0: 
                return (i,j) 
    return 0
# Hàm nhập một xe vào bãi xe
def nhap_xe():
    cho_trong = tim_cho_trong() 
    if cho_trong == None: 
        print("Không còn chỗ trống trong bãi xe!")
    else: 
        bien_so = tao_bien_so()
        thoi_gian_vao = datetime.datetime.now() 
        bai_xe[cho_trong[0]][cho_trong[1]] = (bien_so, thoi_gian_vao) 
        print("Xe có biển số {} đã vào bãi xe vào lúc {}".format(bien_so, thoi_gian_vao))

# Hàm tính phí giữ xe
def tinh_phi(thoi_gian_vao, thoi_gian_ra):
    thoi_gian_giu = thoi_gian_ra - thoi_gian_vao 
    so_phut = math.ceil(thoi_gian_giu.total_seconds() / 60) 
    if so_phut <= 30: 
        return PHI_30_DAU 
    else: 
        so_phut_con_lai = so_phut - 30
        so_khoang_30_phut = math.ceil(so_phut_con_lai / 30)
        return PHI_30_DAU + so_khoang_30_phut * PHI_30_TIEP 

# Hàm xuất một xe ra khỏi bãi xe
def xuat_xe():
    bien_so = input("Nhập biển số xe: ") 
    tim_thay = False
    for i in range(M):
        for j in range(N):
            if bai_xe[i][j] != 0 and bai_xe[i][j][0] == bien_so: 
                tim_thay = True 
                thoi_gian_vao = bai_xe[i][j][1] 
                thoi_gian_ra = datetime.datetime.now() 
                phi = tinh_phi(thoi_gian_vao, thoi_gian_ra) 
                bai_xe[i][j] = 0 
                print("Xe có biển số {} đã ra khỏi bãi xe vào lúc {}".format(bien_so, thoi_gian_ra))
                print("Phí giữ xe là: {} đồng".format(phi))
                danh_sach_xe.append((bien_so, thoi_gian_vao, thoi_gian_ra, phi))
                break
        if tim_thay: 
            break 
    if not tim_thay: 
        print("Không tìm thấy xe có biển số {} trong bãi xe!".format(bien_so))

# Hàm xuất ra danh sách các xe đã ra khỏi bãi xe
def bao_cao():
    print("Danh sách các xe đã ra khỏi bãi xe:")
    print("Biển số\t\tThời gian vào\t\tThời gian ra\t\tPhí giữ xe")
    for xe in danh_sach_xe: # Duyệt qua từng xe trong danh sách
        print("{}\t{}\t{}\t{} đồng".format(xe[0], xe[1], xe[2], xe[3])) 

# Hàm tìm vị trí của một xe trong bãi xe
def tim_vi_tri():
    bien_so = input("Nhập biển số xe: ")
    tim_thay = False 
    for i in range(M):
        for j in range(N):
            if bai_xe[i][j] != 0 and bai_xe[i][j][0] == bien_so: 
                tim_thay = True 
                print("Xe có biển số {} đang ở hàng {}, cột {} của bãi xe".format(bien_so, i+1, j+1)) # In ra vị trí của xe
                break # Thoát khỏi vòng lặp



def thucthi():
    print("*---------------------------------------------------------*")
    print("|   Cac option lua chon                                  |")
    print("|Option 1 : tao  xe, dua xe vao khu, lua thoi gian xe vao|")
    print("|Option 2 :cho xe ra , lua danh sach , tinh tien         |")
    print("|Option 3 :mo danh sach xe da vao                        |")
    print("|Option 4 :tra cua xe                                    |")
    print("*---------------------------------------------------------*")
    a=int(input("moi ban chon option "))
    if a==1:
       print(nhap_xe())
    if a==2:
       print(xuat_xe())
    if a==3:
       print(bao_cao())
    if a==4:
       print(tim_cho_trong())
while(1>0):
    print(thucthi())
    print("ban co muon tiep tuc dua xe vao hay khong(1/0)")
    luachon=int(input())  
    if luachon== 1:
       print(thucthi())
    else :
       print("ket thuc")
       break 



