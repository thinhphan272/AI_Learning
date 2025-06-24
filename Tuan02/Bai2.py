

def nhap_day():
    L = input("Nhập vào từng phần từ (cách nhau bởi khoảng trắng): ")
    L = list(map(int, L.split()))
    print('Các phần tử của dãy: ', L)
    return L

def tron_chuoi():
    a = nhap_day()
    b = nhap_day() 
    
    d = min(len(a), len(b))
    
    c = a if len(a)>len(b) else b
    
    for i in range(d):
        c[i] = a[i] + b[i]
        
    print('Chuỗi đã trộn: ',c)
    
    
tron_chuoi()




