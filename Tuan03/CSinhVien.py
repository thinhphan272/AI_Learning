# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 13:31:13 2025

@author: Administrator
"""

class SinhVien:
    def  __init__(self, mssv, tenSV):
        self.mssv = mssv
        self.tenSV = tenSV
        
    def getmssv(self):
        return self.mssv
    
    def gettenSV(self):
        return self.tenSV
    
    def getName(self):
        return f'{self.mssv} - {self.tenSV}'
        
    def get(self):
        self.mssv = input("Nhập mã số sinh viên: ")
        self.tenSV = input("Nhập họ và tên sinh viên: ")
        
    def put(self):
        print(f'{self.mssv} - {self.tenSV}')