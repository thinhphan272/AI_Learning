import json


class Collection:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"name": self.name}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"])

    def display_info(self):
        print(f"Danh mục: {self.name}")
        print("-" * 40)