aa = [x for x in range(0, 10) if x % 2 == 0]
print(aa)
bb = []
for x in range(0, 10):
    if x % 2 == 0:
        bb.append(x)

print(bb)

zz = lambda x: x * 2
print(zz(3))

vv = [lambda k=k: k * 2 for k in range(1,5)]
for vvv in vv:
    print(vvv())

# my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# new_list = list(filter(lambda x: (x % 2 == 0), my_list))
# print(new_list)
#
# tables = [lambda x = x: x*10 for x in range(1, 11)]
# for table in tables:
#     print(table())
#
# max_number = lambda a, b: a if a > b else b
# print(max_number(3, 5))