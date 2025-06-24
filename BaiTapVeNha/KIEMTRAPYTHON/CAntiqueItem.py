import json
import random

class AntiqueItem:
    def __init__(self, tenDo, namSx, nguonGoc, gtriUT):
        self.tenDo = tenDo
        self.namSx = namSx
        self.nguonGoc = nguonGoc
        self.gtriUT = gtriUT

    def to_dict(self):
        return{"tenDo": self.tenDo, "namSx": self.namSx, "nguonGoc": self.nguonGoc, "gtriUT": self.gtriUT}

    @classmethod
    def from_dict(cls, data):
        return cls(data["tenDo"], data["namSx"], data["nguonGoc"], data["gtriUT"])




def load_data(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            antiques = [AntiqueItem.from_dict(item) for item in data]
    except FileNotFoundError:
        antiques = []
    return antiques

def save_data(antiques, file_name):
    data = [antique.to_dict() for antique in antiques]
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def create_antique(antiques):
    tenDo = input('Nhập tên đồ cổ: ')
    namSx = int(input('Nhập năm sản xuất: '))
    nguonGoc = input('Nhập nguồn gốc: ')
    gtriUT = float(input('Nhập giá trị ước tính: '))
    antique = AntiqueItem(tenDo, namSx, nguonGoc, gtriUT)
    antiques.append(antique)
    save_data(antiques, "AntiqueItem.json")
    print("Món đồ cổ mới đã được thêm thành công! ")

def read_antique(antiques):
    if not antiques:
        print("Không có món đồ cổ nào ")
    else:
        for i, antique in enumerate(antiques, 1):
            print(f"{i}. {antique.tenDo} - {antique.namSx} - {antique.nguonGoc} - {antique.gtriUT}")




