Cities = {"Delhi","Haryana","Bangal","Bangalore","Gujrat","Mumbai"}
North_India = {"Delhi","Haryana","Punjab"}
South_India = {"Bangal","Bangalore","Mumbai"}

# print(North_India.union(South_India))
# print(North_India)
#North_India.update(South_India)
# print(North_India.intersection(Cities))
# print(North_India)
#print(North_India.intersection(South_India))#print north india
#North_India.intersection_update(Cities)
#print(North_India)
#print(North_India.symmetric_difference(Cities))
print(Cities.difference(North_India))
print(North_India.difference(Cities))
