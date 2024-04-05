def filter_price(price):
  if price > 350:
    return True
  else:
    return False

item_price = [230, 400, 450, 350, 370]

filtered_price = filter(filter_price, item_price)
print(list(filtered_price))

# trucks list
#makes = ["Chevy", "Ford", "Toyota", "Ram", "Rivian"]
#print(makes.sort)



#for i in range(0, 4, 2):
  #print(makes[i])

#for make in makes:
  #print(make)