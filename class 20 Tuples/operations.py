# operations on tuple
m_tuples = (23,34,46,"red",False)
print("mixed tuples \n",m_tuples)
i_tuples = (23,45,56,78,99,76,53)
print("integer tuples \n",i_tuples)

# adding elements to tuples
i_tuples = i_tuples +(9,)
print("element added \n",i_tuples)
print("the occurance of 23 in tuple",i_tuples.count(23))
# slicing
print(i_tuples[1:4])
print(i_tuples[:4])