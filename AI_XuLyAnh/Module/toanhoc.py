def tamgiacvuong(a, b, c):
    check_triagle = False
    if a > b and a > c:
        if (b * b) + (c * c) == a * a:
            check_triagle = True
        else:
            check_triagle = False
    elif b > c and b > a:
        if (a * a) + (c * c) == b * b:
            check_triagle = True
        else:
            check_triagle = False
    else:
        if (a * a) + (b * b) == c * c:
            check_triagle = True
        else:
            check_triagle = False
            
    return check_triagle