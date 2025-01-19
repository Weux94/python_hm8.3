def find_unique_value(list):
  unique_list = []
  for item in list:
      if item in unique_list:
        continue
      else:
        unique_list.append(item)
  return unique_list[0]

print(find_unique_value([1,2,3,4,5,5,2]))
