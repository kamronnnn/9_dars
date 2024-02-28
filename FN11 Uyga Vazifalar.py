# 1 - Masala

import csv

users = [
    {'user_name': 'tony', 'followers': 987, 'online': 'True'},
    {'user_name': 'jimmy', 'followers': 1000, 'online': 'False'},
    {'user_name': 'tommy', 'followers': 1285, 'online': 'True'},
    {'user_name': 'mikky', 'followers': 822, 'online': 'True'}
]

with open('users_info.csv', mode='w') as csv_file:

    header = ['user_name', 'followers', 'online']
    writer = csv.DictWriter(csv_file, header)
    writer.writeheader()
    writer.writerows(users)

#=================================================================================

# 2 - Masala

# import csv
#
# with open('users_info.csv', mode='r', encoding='utf-8') as csv_file:
#     reader = csv.reader(csv_file)
#
#     for i in reader:
#         for j in i:
#             print(j, end=" ")
#         print()

#=================================================================================

# 3 - Masala

# file = open('users_info.csv', mode='r', encoding='utf-8')
# copy_file = file.read()
#
# txt_copy = open('txt_copy.txt', mode='w', encoding='utf-8')
# txt_copy.write(copy_file)
#
# file.close()
# txt_copy.close()

#=================================================================================

# 4 - Masala

# def qabul_qiluvchi_raqam(raqam):
#     try:
#         natija = raqam + 2
#         print(f"Natija: \x1b[31m{natija}\x1b[0m")
#     except TypeError:
#         print("Xatolik: Qabul qilingan raqam - raqam emas")
#
# raqam = input("Istalgan raqamni kiriting: ")
# qabul_qiluvchi_raqam(int(raqam))

#=================================================================================

# 5 - Masala

# def sonlar_kopaytmasi(son1, son2):
#     try:
#         natija = son1 * son2
#         print(f"Natija: \x1b[32m{natija}\x1b[0m")
#     except TypeError:
#         natija = str(son1) + str(son2)
#         print(f"Natija: \x1b[32m{natija}\x1b[0m")
#
# son1 = input("Birinchi sonni kiriting: ")
# son2 = input("Ikkinchi sonni kiriting: ")
#
# sonlar_kopaytmasi(float(son1), float(son2))

