def find_unique_value(list):
  for num in list:
    if list.count(num) == 1:
      return num

print(find_unique_value([8, 8,1,1,2,2,3,3,4,5,5,2]))
