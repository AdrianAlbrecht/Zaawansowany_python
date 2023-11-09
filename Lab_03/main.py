from lab_03 import Pizza, Slice

#pizza1 = Pizza(['ser','szynka'], 19.0)
#print("Działam dalej")
pizza2 = Pizza(['ser','szynka'], 20.0)
print(pizza2.price)
pizza2.diameter = 23.0
#pizza2.__price = 0.0
print(pizza2.price)
pizza2.add_topping('pieczarki')
print(pizza2.price, pizza2.toppings)
pizza2.add_topping('brokuły','fasolka')
print(pizza2.price, pizza2.toppings)
print(pizza2)
pizza3 = Pizza([],60.0)
print(pizza3)
print(pizza2 + pizza3)

# slice_p_7 = Slice(['ser','szynka'], 25.0, 7)
# print("Działam dalej")
# slice_u_4 = Slice(['ser','szynka'], 25.0, 2)
# print("Działam dalej")
# slice_h_12 = Slice(['ser','szynka'], 25.0, 14)
# print("Działam dalej")
slice_12 = Slice(['ser','szynka'], 25.0, 12)
slice_12.how_many_slices = 10
print(slice_12.how_many_slices)
print(slice_12.price,slice_12.part_price(5))
print(slice_12)
slice_12_without_toppings = Slice([], 60.0, 10)
print(slice_12_without_toppings)
