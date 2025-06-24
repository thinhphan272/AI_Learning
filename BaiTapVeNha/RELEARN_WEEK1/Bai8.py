celsius = float(input('Enter temperature in Celsius: '))

if celsius < -273.15:
    print('Nhiệt độ không hợp lệ vì nó dưới độ không tuyệt đối!')
elif celsius == -273.15:
    print('Nhiệt độ tuyệt đối bằng 0!')
elif celsius > -273.15 and celsius < 0:
    print('Nhiệt độ dưới điểm đóng băng!')
elif celsius == 0:
    print('Nhiệt đô đang ở điểm đóng băng!')
elif celsius > 0 and celsius < 100:
    print('Nhiệt độ ở mức bình thường!')
elif celsius == 100:
    print('Nhiệt độ đang ở điểm sôi!')
else:
    print('Nhiệt độ cao hơn điểm sôi!')