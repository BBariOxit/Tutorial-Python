import math
import os
import Functions

def XuatMenu():
    print("============================FUNCTIONS===============================")
    print("0. Thoát chương trìnhtrình")
    print("1. Tính (a+b), a/b, a^b")
    print("2. Tính diện tích hình tròntròn khi biết bán kính")
    print("3. Xuất tất cả các số nguyên tố trong 1 khoảng")
    print("4. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không")
    print("5. Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)")
    print("6. Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)")
    print("7. Tính tổng căn bậc 2 của n số nguyên đầu tiên")
    print("8. Giải phương trình bậc 2: ax2 + bx + c=0")
    print("9. Tính n!")
    print("10. In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)")
    print("""11. Đổi giờ - phút – giây: thời gian đầu vào là giây được đổi thành giờ, phút, giây.
    Xuất kết quả ra màn hình dưới dạng: giờ:phút:giây. Ví dụ: soGiay = 3770 thì xuất
    ra màn hình 1:2:50.""")
    print("12.Cho một mảng số nguyên: (nên viết 2-3 cách)")
    print("===============================END=================================")

def XuatMenu2():
    print("============================FUNCTIONS===============================")
    print("1. Xuât tất cả các số lẻ không chia hết cho 5")
    print("2. Xuất tất cả các số Fibonacci")
    print("3. Tìm số nguyên tố lớn nhất")
    print("4. Tìm số Fibonacci bé nhất")
    print("5. Tính trung bình các số lẻ")
    print("6. Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng")
    print("7. Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ")
    print("8. Đảo ngược trật tự các phần tử của danh sách")
    print("9. Xuất tất cả các số lớn thứ nhì của danh sách")
    print("10. Tính tổng các chữ số của tất cả các số trong danh sách")
    print("11. Đếm số lần xuất hiện của một số trong danh sách")
    print("12. Xuất các số xuất hiện n lần trong danh sách")
    print("13. Xuất các số xuất hiện nhiều lần nhất trong danh sách")
    print("===============================END=================================")

def ChonMenu(menu):
    while True:
        n = int(input("nhập chức năng:"))
        if(0 <= n <= menu):
            return n
        else:
            os.system('cls')
            XuatMenu()
            print(f"vui lòng nhập chức năng trong khoảng 0-{menu}:")

def Extra(DsNumbs):
    txt =str(input("ban co muon tiep tuc cac chuc nang khac voi day so nguyen vua nhap(y/n):"))
    if(len(txt) > 1):
        Extra()
    elif(txt == "y"):
        XuLyCNExtra(DsNumbs)
    else:
        print("===========================thoat=============================")

def XuLyCNMenu2():
    DsNumbs = Functions.NhapMangSoNguyen()
    XuatMenu2()
    print(f"mang ban vua nhap la:{DsNumbs}")
    choice = ChonMenu(13)
    XuLyMenu2(choice,DsNumbs)

def XuLyCNExtra(DsNumbs):
    XuatMenu2()
    print(f"mang ban vua nhap la:{DsNumbs}")
    choice = ChonMenu(13)
    XuLyMenu2(choice,DsNumbs)

def XuLyMenu2(choice,DsNumbs):
    match(choice):
        case 1:
            print("1. Xuât tất cả các số lẻ không chia hết cho 5")
            print(Functions.XuatSoLeKhongChiaHetCho5(DsNumbs))
            Extra(DsNumbs)
            XuLyCNMenu2()
        case 2:
            print("2. Xuất tất cả các số Fibonacci")
            print(f"Danh sach cac so fibonacci la:", Functions.XuatAllFibonacci(DsNumbs))
            Extra(DsNumbs)
            XuLyCNMenu2()
        case 3:
            print("3. Tìm số nguyên tố lớn nhất")
            print(f"Danh sach cac so la so nguyen to la:", Functions.XuatAllSoNguyenTo(DsNumbs))
            Extra(DsNumbs)
            XuLyCNMenu2()
        case 4:
            print("4. Tìm số Fibonacci bé nhất")
            print("day so fibonacci la:",Functions.XuatAllFibonacci(DsNumbs))
            print("so fibonacci nho nhat trong day la:",min(Functions.XuatAllFibonacci(DsNumbs)))
            Extra(DsNumbs)
            XuLyCNMenu2()
        case 5:
            print("5. Tính trung bình các số lẻ")
            print("Trung binh cac so le la:", Functions.TinhTBSoLe(DsNumbs))
            Extra(DsNumbs)
            XuLyCNMenu2()
        case 6:
            print("6. Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng")
            print("Tich so le khong chi het cho 3 la:", Functions.TinhTichSoLeKoChiaHetCho3(DsNumbs))
            Extra(DsNumbs)
            XuLyCNMenu2()
        case 7:
            print("7. Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ")
            a = int(input("nhap vi tri cua so thu 1:"))
            b = int(input("nhap vi tri cua so thu 2:"))
            print(f"Danh sach sau khi da hoan vi 2 vi tri {a} va {b} la:", Functions.HoanVi2ViTri(a,b,DsNumbs))
            Extra(DsNumbs)
            XuLyCNMenu2()
        case 8:
            print("8. Đảo ngược trật tự các phần tử của danh sách")
            print("danh sach sau khi dao la:",Functions.DaoDS(DsNumbs))
            Extra(DsNumbs)
            XuLyCNMenu2()
        case 9:
            print("9. Xuất tất cả các số lớn thứ nhì của danh sách")
            print("Tat ca cac so lon nhi la:", Functions.LaySoLonThu2(DsNumbs))
            Extra(DsNumbs)
            XuLyCNMenu2()
        case 10:
            print("10. Tính tổng các chữ số của tất cả các số trong danh sách")
            print("Tong tat ca cac chu so la:",Functions.TongAllCacChuSo(DsNumbs))
            Extra(DsNumbs)
            XuLyCNMenu2()
        case 11:
            print("11. Đếm số lần xuất hiện của một số trong danh sách")
            n = int(input("nhap so ma ban muon biet so lan xuat hien trong ds:"))
            print(f"so lan xuat hien cua so {n} trong ds la", Functions.DemSoLanXH(DsNumbs,n))
            Extra(DsNumbs)
            XuLyCNMenu2()
        case 12:
            print("12. Xuất các số xuất hiện n lần trong danh sách")
            n = int(input("nhap so lan xuat hien:"))
            print(f"danh sach cac so xh {n} lan la:", Functions.TimCacSoXHNLan(DsNumbs,n))
            Extra(DsNumbs)
            XuLyCNMenu2()
        case 13:
            print("13. Xuất các số xuất hiện nhiều lần nhất trong danh sách")
            print("cac so xuat hien nhieu lan nhat la:",Functions.TimCacSoXHNhieuLanNhat(DsNumbs))
            Extra(DsNumbs)
            XuLyCNMenu2()
            
def XuLyMenu(choice):
    match(choice):
        case 0:
            print("0. Thoát chương trình")
            exit()
        case 1:
            print("1. Tính (a+b), a/b, a^b")
            a = int(input("nhap so nguyen a: "))
            b = int(input("nhap so nguyen b: "))
            Functions.TinhToanCoBan(a,b)
        case 2:
            print("2. Tính diện tích hình tròn khi biết bán kính")
            n = int(input("nhap ban kinh hinh tron:"))
            print("dien tich hinh tron la:", Functions.TinhSHinhTron(n))
        case 3:
            print("3. Xuất tất cả các số nguyên tố trong 1 khoảng")
            a = int(input("nhap so bat dau: "))
            b = int(input("nhap so ket thuc: "))
            print(f"danh sach cac so nguyen to trong khoang {a}-{b} la: ",Functions.TimDaySoNguyenTo(a,b))
        case 4:
            print("4. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không")
            a = int(input("nhap so ma ban muon kiem tra:"))
            if(Functions.CheckFibonacci(a)):
                print(f"so {a} la so fibonacci")
            else:
                print(f"so {a} ko la so fibonacci")
            txt = str(input("ban co muon nhap so khac de ktra ko?(y/n):"))
            while True:
                if txt == "n":
                    break
                else:
                    a = int(input("nhap so ma ban muon kiem tra:"))
                    if(Functions.KtraSoFibonacci(a)):
                        print(f"so {a} la so fibonacci")
                    else:
                        print(f"so {a} ko la so fibonacci")
        case 5:
            print("5. Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)")
            n = int(input("nhap so fibonacci thu n ma ban muon tim:"))
            print(f"so fibonacci thu {n} dung de quy la:",Functions.FindFibonacciRescusive(n))
            print(f"so fibonacci thu {n} khong dung de quy la:",Functions.FindFibonacciNonRecursive(n))
        case 6:
            print("6. Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)")
            n = int(input("nhap so fibonacci thu n (tinh tong cua day n fibonacci):"))
            print(f"tong cua {n} so fibonacci dung de quy la la:",Functions.SumOfFibonacciRescusive(n))
            print(f"tong cua {n} so fibonacci khong dung de quy la la:",Functions.SumOfNFibonacciNonRescusive(n))
        case 7:
            print("7. Tính tổng căn bậc 2 của n số nguyên đầu tiên")
            n = int(input("nhap so nguyen thu n:"))
            print("tổng căn bậc 2 của {n} số nguyên đầu tiên la:", Functions.TongSQRTCuaNSoNguyen(n))
        case 8:
            print("8. Giải phương trình bậc 2: ax2 + bx + c=0")
            a = float(input("nhap he so a:"))
            b = float(input("nhap he so b:"))
            c = float(input("nhap he so c:"))
            result = Functions.GiaiPTBac2(a,b,c)
            print(f"PT {a}x^2 + {b}x +{c} = 0 {result}")
        case 9:
            print("9. Tính n!")
            n = int(input("nhap so n:"))
            print(f"{n}! = ", Functions.TinhNGiaiThua(n))
        case 10:
            print("10. In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)")
            n = int(input("nhap kich thuoc tam giac:"))
            print(Functions.inTamGiac(n))
        case 11:
            print("""11. Đổi giờ - phút – giây: thời gian đầu vào là giây được đổi thành giờ, phút, giây.
    Xuất kết quả ra màn hình dưới dạng: giờ:phút:giây. Ví dụ: soGiay = 3770 thì xuất
    ra màn hình 1:2:50.""")
            n = int(input("nhap so giay ma ban muon doi:"))
            print("{n}s = ", Functions.DoiGioPhutGiay(n))
        case 12:
            print("12.Cho một mảng số nguyên: (nên viết 2-3 cách)")
            XuLyCNMenu2()
            
            
            

            


