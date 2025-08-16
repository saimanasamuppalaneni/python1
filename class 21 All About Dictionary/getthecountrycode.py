# get the country code 
code = {
    "India":'0091',
    "Pakistan":'0092',
    "USA":'0001'
}
print("the country code for India ")
print(code.get("India","not found"))
print("the country code for Japan ")
print(code.get("Japan","not found"))