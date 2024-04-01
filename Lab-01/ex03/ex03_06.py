def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
my_dric = {'a':1 ,'b':2, 'c':3, 'd':4}
key_to_delete = 'b'
result = xoa_phan_tu(my_dric, key_to_delete)
if result:
    print("Phan tu nay da duoc xoa tu dictionary:",my_dric)
else:
    print("Khong tim thay Phan tu can xoa trong dictionary:")  