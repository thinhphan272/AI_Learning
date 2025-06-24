def ptBac1(a, b):
    if a != 0:
        x = -b / a
        print(f"Phương trình có nghiệm duy nhất x = -b / a\nx = {x}")
    elif a == 0 and b != 0:
        print("Phương trình vô nghiệm")
    else:
        print("Phương trình nghiệm đúng với mọi x ")


if __name__ == "__main__":
    print("Trường hợp a và b khác 0")
    ptBac1(2, 1)
    print("Trường hợp a và b bằng 0")
    ptBac1(0, 0)
    print("Trường hợp a = 0; b != 0")
    ptBac1(0, 1)
