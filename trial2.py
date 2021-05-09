list1 = [22, 4.5, -908, -556.897, "Karnan", ["Sulthan", "Teddy", "Nenjam Marapithillai"],
         {'a': "Master", 'b': "Eeswaran", 'c': ["Asuran", "Super Deluxe"],
          'd': {'1': "Dhanush", '2': "Vijay Sethupathi"}}]
print(list1[0])
print(list1[5][2])
print(list1[6]['a'])
print(list1[6]['d']['2'])
print(list1[-1]['c'][1])
list1.insert(2, "Mari Selvaraj")
print(list1)
list1[0]=25
del list1[1]
print(list1)
print(list1[2:4])
