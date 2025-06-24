import json
from datetime import datetime


class AntiqueItem:
    def __init__(self, name, year, origin, estimated_value, collection_name):
        self.name = name
        self.year = year
        self.origin = origin
        self.estimated_value = estimated_value
        self.collection_name = collection_name

    def to_dict(self):
        return {
            "name": self.name,
            "year": self.year,
            "origin": self.origin,
            "estimated_value": self.estimated_value,
            "collection_name": self.collection_name
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["year"],
            data["origin"],
            data["estimated_value"],
            data["collection_name"]
        )

    def display_info(self):
        print(f"Tên món đồ: {self.name}")
        print(f"Năm sản xuất: {self.year}")
        print(f"Nguồn gốc: {self.origin}")
        print(f"Giá trị ước tính: ${self.estimated_value:,.2f}")
        print(f"Danh mục: {self.collection_name}")
        print("-" * 40)