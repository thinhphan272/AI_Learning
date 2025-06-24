import json
import os
import random
from antique_item import AntiqueItem
from collection import Collection
from kt2data import danh_muc_suu_tap, do_co_theo_danh_muc, nguon_goc


class AntiqueManager:
    def __init__(self):
        self.antique_items = []
        self.collections = []
        self.load_data()

    def load_data(self):
        # Kiểm tra và tạo file nếu không tồn tại
        if not os.path.exists("antique_items.json") or not os.path.exists("collections.json"):
            self.generate_sample_data()
        else:
            self.load_from_files()

    def generate_sample_data(self):
        # Chọn ngẫu nhiên 4 danh mục
        selected_collections = random.sample(danh_muc_suu_tap, 4)
        self.collections = [Collection(name) for name in selected_collections]

        # Tạo 12 món đồ cổ (3 mỗi danh mục)
        for collection in selected_collections:
            items_in_collection = do_co_theo_danh_muc.get(collection, [])
            selected_items = random.sample(items_in_collection, min(3, len(items_in_collection)))

            for item_name in selected_items:
                year = random.randint(1600, 1950)
                origin = random.choice(nguon_goc)
                estimated_value = round(random.randint(1000, 500000) / 100) * 100

                antique = AntiqueItem(
                    name=item_name,
                    year=year,
                    origin=origin,
                    estimated_value=estimated_value,
                    collection_name=collection
                )
                self.antique_items.append(antique)

        self.save_to_files()

    def save_to_files(self):
        with open("antique_items.json", "w", encoding="utf-8") as f:
            json.dump([item.to_dict() for item in self.antique_items], f, ensure_ascii=False, indent=2)

        with open("collections.json", "w", encoding="utf-8") as f:
            json.dump([col.to_dict() for col in self.collections], f, ensure_ascii=False, indent=2)

    def load_from_files(self):
        try:
            with open("antique_items.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.antique_items = [AntiqueItem.from_dict(item) for item in data]

            with open("collections.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.collections = [Collection.from_dict(col) for col in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.generate_sample_data()

    # Các phương thức quản lý đồ cổ
    def add_antique_item(self, item):
        # Kiểm tra danh mục có tồn tại không
        if not any(col.name == item.collection_name for col in self.collections):
            print("Danh mục không tồn tại! Không thể thêm đồ cổ.")
            return False

        self.antique_items.append(item)
        self.save_to_files()
        return True

    def update_antique_item(self, item_name, new_data):
        for item in self.antique_items:
            if item.name == item_name:
                # Kiểm tra danh mục mới có tồn tại không
                if "collection_name" in new_data and not any(
                        col.name == new_data["collection_name"] for col in self.collections):
                    print("Danh mục mới không tồn tại! Cập nhật thất bại.")
                    return False

                for key, value in new_data.items():
                    setattr(item, key, value)

                self.save_to_files()
                return True
        return False

    def delete_antique_item(self, item_name):
        for i, item in enumerate(self.antique_items):
            if item.name == item_name:
                del self.antique_items[i]
                self.save_to_files()
                return True
        return False

    # Các phương thức quản lý danh mục
    def add_collection(self, collection):
        if any(col.name == collection.name for col in self.collections):
            print("Danh mục đã tồn tại!")
            return False

        self.collections.append(collection)
        self.save_to_files()
        return True

    def update_collection_name(self, old_name, new_name):
        # Kiểm tra tên mới có trùng không
        if any(col.name == new_name for col in self.collections):
            print("Tên danh mục mới đã tồn tại!")
            return False

        for col in self.collections:
            if col.name == old_name:
                col.name = new_name
                # Cập nhật tất cả đồ cổ thuộc danh mục này
                for item in self.antique_items:
                    if item.collection_name == old_name:
                        item.collection_name = new_name
                self.save_to_files()
                return True
        return False

    def delete_collection(self, collection_name, new_collection=None):
        # Kiểm tra xem danh mục có tồn tại không
        collection_exists = any(col.name == collection_name for col in self.collections)
        if not collection_exists:
            print("Danh mục không tồn tại!")
            return False

        # Kiểm tra xem danh mục có đồ cổ không
        items_in_collection = [item for item in self.antique_items if item.collection_name == collection_name]

        if items_in_collection:
            if new_collection is None:
                print("Danh mục không thể xóa vì có đồ cổ bên trong. Vui lòng chọn danh mục khác để chuyển đồ cổ.")
                return False

            # Kiểm tra danh mục mới có tồn tại không
            if not any(col.name == new_collection for col in self.collections):
                print("Danh mục mới không tồn tại!")
                return False

            # Chuyển tất cả đồ cổ sang danh mục mới
            for item in items_in_collection:
                item.collection_name = new_collection

        # Xóa danh mục
        self.collections = [col for col in self.collections if col.name != collection_name]
        self.save_to_files()
        return True

    # Các phương thức hiển thị và tìm kiếm
    def display_collections(self):
        print("\nDANH SÁCH DANH MỤC SƯU TẬP")
        print("=" * 40)
        for col in self.collections:
            col.display_info()

    def display_antiques_in_collection(self, collection_name):
        items = [item for item in self.antique_items if item.collection_name == collection_name]
        if not items:
            print(f"Không có đồ cổ nào trong danh mục '{collection_name}'")
            return

        print(f"\nDANH SÁCH ĐỒ CỔ TRONG DANH MỤC '{collection_name}'")
        print("=" * 60)
        for item in items:
            item.display_info()

    def display_all_antiques(self):
        print("\nDANH SÁCH TẤT CẢ ĐỒ CỔ")
        print("=" * 60)
        for item in self.antique_items:
            item.display_info()

    def search_antiques_by_name(self, keyword):
        results = [item for item in self.antique_items if keyword.lower() in item.name.lower()]
        if not results:
            print(f"Không tìm thấy đồ cổ nào chứa từ khóa '{keyword}'")
            return

        print(f"\nKẾT QUẢ TÌM KIẾM CHO TỪ KHÓA '{keyword}'")
        print("=" * 60)
        for item in results:
            item.display_info()

    def sort_antiques(self, by='name', ascending=True):
        if by == 'name':
            sorted_items = sorted(self.antique_items, key=lambda x: x.name, reverse=not ascending)
        elif by == 'year':
            sorted_items = sorted(self.antique_items, key=lambda x: x.year, reverse=not ascending)
        else:
            print("Tiêu chí sắp xếp không hợp lệ!")
            return

        order = "tăng dần" if ascending else "giảm dần"
        print(f"\nDANH SÁCH ĐỒ CỔ SẮP XẾP THEO {by.upper()} ({order})")
        print("=" * 60)
        for item in sorted_items:
            item.display_info()

    def get_stats(self):
        stats = {}
        for col in self.collections:
            count = sum(1 for item in self.antique_items if item.collection_name == col.name)
            stats[col.name] = count

        print("\nTHỐNG KÊ SỐ LƯỢNG ĐỒ CỔ THEO DANH MỤC")
        print("=" * 50)
        for col_name, count in stats.items():
            print(f"{col_name}: {count} món đồ")
        print("-" * 50)
        print(f"Tổng cộng: {len(self.antique_items)} món đồ")