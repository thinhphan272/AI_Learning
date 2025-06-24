import json

from colorama import Fore, Back, init

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_dict(self):
        return{"name": self.name, "price": self.price}

    @classmethod
    def form_dict(cls, data):
        return cls(data['name'], data['price'])


def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            products = [Product.form_dict(item) for item in data]
    except FileNotFoundError:
        products = []
    return products

def save_data(products, file_name):
    data = [product.to_dict() for product in products]
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def create_products(products):
    name = input('Nhập tên sản phẩm: ')
    price = int(input('Nhập giá sản phẩm: '))
    product = Product(name, price)
    products.append(product)
    save_data(products, "products.json")
    print(Fore.BLUE + Back.BLACK+'Sản phẩm được thêm thành công')
def read_products(products):
    if not products:
        print(Fore.RED + Back.BLACK + 'Không có sản phẩm nào')
    else:
        for i, product in enumerate(products, 1):
            print(f'{i}. {product.name} - {product.price}')
def main():

    init(autoreset=False)
    products = load_data("products.json")
    while True:
        print(Fore.YELLOW + Back.BLACK + '\n----------Quản lý sản phẩm----------')
        print('1. Hiển thị danh sách sản phẩm')
        print('2. Thêm sản phẩm mới')
        print('3. Cập nhật sản phẩm')
        print('4. Xóa một sản phẩm')
        print('0. Thoát chương trình')
        print(Fore.GREEN + Back.BLACK + '')
        choice = input('Chọn chức năng: ')

        if choice == '1':
            read_products(products)
        elif choice == '2':
            create_products(products)

        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '0':
            print(Fore.BLUE + Back.BLACK + 'Kết thúc chương trình !!')
            break
        else:
            print(Fore.RED + Back.BLACK + 'Lựa chọn không hợp lệ. Vui lòng nhập lại')

if __name__ == '__main__':
    main()