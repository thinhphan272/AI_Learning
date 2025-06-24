import json

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_dict(self):
        return{"name": self.name, "price": self.price}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"])


def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            products = [Product.from_dict(item) for item in data]
    except FileNotFoundError:
        products = []
    return products


def save_data(products, file_name):
    data = [product.to_dict() for product in products]
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


def create_product(products):
    name = input('Nhập tên sản phẩm: ')
    price = int(input('Nhập giá sản phẩm: '))
    product = Product(name, price)
    products.append(product)
    save_data(products, "sanPham.json")
    print('Sản phẩm được thêm thành công')

def read_product(products):
    if not products:
        print('Không có sản phẩm nào !!')
    else:
        for i, product in enumerate(products, 1):
            print(f'{i}. {product.name} - {product.price}')

def main():

    products = load_data("sanPham.json")
    while True:
        print('\n---------------Quản lý sản phẩm---------------')
        print('1. Hiển thị danh sách sản phẩm')
        print('2. Thêm sản phẩm mới')
        print('3. Cập nhật sản phẩm!')
        print('4. Xóa sản phẩm ')
        print('0. Thoát chương trình')

        choice = input('Chọn chức năng: ')

        if choice == '1':
            read_product(products)
        elif choice == '2':
            create_product(products)
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

