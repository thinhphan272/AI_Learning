from antique_manager import AntiqueManager
from antique_item import AntiqueItem

def display_menu():
    print("\n" + "=" * 40)
    print("QUẢN LÝ BỘ SƯU TẬP ĐỒ CỔ".center(40))
    print("=" * 40)
    print("1. Quản lý Đồ Cổ")
    print("2. Quản lý Danh Mục Sưu Tập")
    print("3. Chức năng bổ sung")
    print("4. Thoát chương trình")
    print("=" * 40)


def display_antique_menu():
    print("\n" + "=" * 40)
    print("QUẢN LÝ ĐỒ CỔ".center(40))
    print("=" * 40)
    print("1. Thêm đồ cổ mới")
    print("2. Cập nhật thông tin đồ cổ")
    print("3. Xóa đồ cổ")
    print("4. Hiển thị tất cả đồ cổ")
    print("5. Quay lại menu chính")
    print("=" * 40)


def display_collection_menu():
    print("\n" + "=" * 40)
    print("QUẢN LÝ DANH MỤC SƯU TẬP".center(40))
    print("=" * 40)
    print("1. Thêm danh mục mới")
    print("2. Cập nhật tên danh mục")
    print("3. Xóa danh mục")
    print("4. Hiển thị tất cả danh mục")
    print("5. Quay lại menu chính")
    print("=" * 40)


def display_extra_menu():
    print("\n" + "=" * 40)
    print("CHỨC NĂNG BỔ SUNG".center(40))
    print("=" * 40)
    print("1. Hiển thị đồ cổ theo danh mục")
    print("2. Tìm kiếm đồ cổ theo tên")
    print("3. Sắp xếp đồ cổ")
    print("4. Thống kê số lượng đồ cổ")
    print("5. Quay lại menu chính")
    print("=" * 40)


def get_input(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if required and not value:
            print("Giá trị này là bắt buộc. Vui lòng nhập lại!")
        else:
            return value


def main():
    manager = AntiqueManager()

    while True:
        display_menu()
        choice = get_input("Chọn chức năng (1-4): ")

        if choice == "1":  # Quản lý đồ cổ
            while True:
                display_antique_menu()
                sub_choice = get_input("Chọn chức năng (1-5): ")

                if sub_choice == "1":  # Thêm đồ cổ mới
                    print("\nTHÊM ĐỒ CỔ MỚI")
                    print("-" * 30)
                    manager.display_collections()

                    name = get_input("Tên món đồ: ")
                    year = int(get_input("Năm sản xuất: "))
                    origin = get_input("Nguồn gốc: ")
                    estimated_value = float(get_input("Giá trị ước tính (USD): "))
                    collection_name = get_input("Tên danh mục: ")

                    new_item = AntiqueItem(name, year, origin, estimated_value, collection_name)
                    if manager.add_antique_item(new_item):
                        print("Thêm đồ cổ thành công!")

                elif sub_choice == "2":  # Cập nhật đồ cổ
                    print("\nCẬP NHẬT THÔNG TIN ĐỒ CỔ")
                    print("-" * 30)
                    manager.display_all_antiques()

                    item_name = get_input("Nhập tên đồ cổ cần cập nhật: ")
                    print("\nNhập thông tin mới (bỏ trống nếu không thay đổi):")

                    new_data = {}
                    name = get_input("Tên món đồ: ", required=False)
                    if name: new_data["name"] = name

                    year = get_input("Năm sản xuất: ", required=False)
                    if year: new_data["year"] = int(year)

                    origin = get_input("Nguồn gốc: ", required=False)
                    if origin: new_data["origin"] = origin

                    value = get_input("Giá trị ước tính (USD): ", required=False)
                    if value: new_data["estimated_value"] = float(value)

                    collection = get_input("Tên danh mục: ", required=False)
                    if collection: new_data["collection_name"] = collection

                    if manager.update_antique_item(item_name, new_data):
                        print("Cập nhật thành công!")
                    else:
                        print("Cập nhật thất bại! Kiểm tra lại thông tin.")

                elif sub_choice == "3":  # Xóa đồ cổ
                    print("\nXÓA ĐỒ CỔ")
                    print("-" * 30)
                    manager.display_all_antiques()

                    item_name = get_input("Nhập tên đồ cổ cần xóa: ")
                    if manager.delete_antique_item(item_name):
                        print("Xóa đồ cổ thành công!")
                    else:
                        print("Không tìm thấy đồ cổ để xóa!")

                elif sub_choice == "4":  # Hiển thị tất cả đồ cổ
                    manager.display_all_antiques()

                elif sub_choice == "5":  # Quay lại
                    break

                else:
                    print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

        elif choice == "2":  # Quản lý danh mục
            while True:
                display_collection_menu()
                sub_choice = get_input("Chọn chức năng (1-5): ")

                if sub_choice == "1":  # Thêm danh mục mới
                    print("\nTHÊM DANH MỤC MỚI")
                    print("-" * 30)
                    name = get_input("Tên danh mục: ")

                    new_collection = Collection(name)
                    if manager.add_collection(new_collection):
                        print("Thêm danh mục thành công!")

                elif sub_choice == "2":  # Cập nhật tên danh mục
                    print("\nCẬP NHẬT TÊN DANH MỤC")
                    print("-" * 30)
                    manager.display_collections()

                    old_name = get_input("Nhập tên danh mục cần đổi: ")
                    new_name = get_input("Nhập tên mới: ")

                    if manager.update_collection_name(old_name, new_name):
                        print("Đổi tên danh mục thành công!")
                    else:
                        print("Đổi tên thất bại! Kiểm tra lại thông tin.")

                elif sub_choice == "3":  # Xóa danh mục
                    print("\nXÓA DANH MỤC")
                    print("-" * 30)
                    manager.display_collections()

                    col_name = get_input("Nhập tên danh mục cần xóa: ")

                    # Kiểm tra xem danh mục có đồ cổ không
                    items_in_collection = [item for item in manager.antique_items if item.collection_name == col_name]

                    if items_in_collection:
                        print(f"Danh mục '{col_name}' có {len(items_in_collection)} món đồ.")
                        manager.display_collections()
                        new_col = get_input("Nhập tên danh mục mới để chuyển đồ cổ (bỏ trống để hủy): ", required=False)
                        if new_col:
                            if manager.delete_collection(col_name, new_col):
                                print("Xóa danh mục thành công!")
                            else:
                                print("Xóa danh mục thất bại!")
                        else:
                            print("Đã hủy thao tác xóa danh mục.")
                    else:
                        if manager.delete_collection(col_name):
                            print("Xóa danh mục thành công!")
                        else:
                            print("Xóa danh mục thất bại!")

                elif sub_choice == "4":  # Hiển thị tất cả danh mục
                    manager.display_collections()

                elif sub_choice == "5":  # Quay lại
                    break

                else:
                    print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

        elif choice == "3":  # Chức năng bổ sung
            while True:
                display_extra_menu()
                sub_choice = get_input("Chọn chức năng (1-5): ")

                if sub_choice == "1":  # Hiển thị theo danh mục
                    print("\nHIỂN THỊ ĐỒ CỔ THEO DANH MỤC")
                    print("-" * 30)
                    manager.display_collections()

                    col_name = get_input("Nhập tên danh mục để xem đồ cổ: ")
                    manager.display_antiques_in_collection(col_name)

                elif sub_choice == "2":  # Tìm kiếm đồ cổ
                    print("\nTÌM KIẾM ĐỒ CỔ")
                    print("-" * 30)
                    keyword = get_input("Nhập từ khóa tìm kiếm: ")
                    manager.search_antiques_by_name(keyword)

                elif sub_choice == "3":  # Sắp xếp đồ cổ
                    print("\nSẮP XẾP ĐỒ CỔ")
                    print("-" * 30)
                    print("1. Theo tên (A-Z)")
                    print("2. Theo tên (Z-A)")
                    print("3. Theo năm sản xuất (cũ nhất)")
                    print("4. Theo năm sản xuất (mới nhất)")

                    sort_choice = get_input("Chọn cách sắp xếp (1-4): ")

                    if sort_choice == "1":
                        manager.sort_antiques(by='name', ascending=True)
                    elif sort_choice == "2":
                        manager.sort_antiques(by='name', ascending=False)
                    elif sort_choice == "3":
                        manager.sort_antiques(by='year', ascending=True)
                    elif sort_choice == "4":
                        manager.sort_antiques(by='year', ascending=False)
                    else:
                        print("Lựa chọn không hợp lệ!")

                elif sub_choice == "4":  # Thống kê
                    manager.get_stats()

                elif sub_choice == "5":  # Quay lại
                    break

                else:
                    print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

        elif choice == "4":  # Thoát
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")


if __name__ == "__main__":
    main()