def main():
    antiques = load_data("AntiqueItem.json")
    while True:
        print('\n---------------Quản lý Đồ Cổ---------------')
        print('1. Hiển thị danh sách Đồ Cổ')
        print('2. Thêm Đồ Cổ mới')
        print('3. Cập nhật Đồ Cổ')
        print('4. Xóa Đồ Cổ')
        print('0. Thoát chương trình')

        choice = input('Chọn chức năng: ')

        if choice == '1':
           read_antique(antiques)
        elif choice == '2':
            create_antique(antiques)
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '0':
            print("Kết thúc chương trình!!")
            break
        else:
            print('Lựa chọn không hợp lệ. Vui lòng nhập lại!')

if __name__ == '__main__':
    main()