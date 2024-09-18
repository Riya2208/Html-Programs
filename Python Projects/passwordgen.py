# import random 
# chars = "dbsgfkyghdf275381273#^%$^&^%$%^&(**&^%$#^$%^&**(GJFGJFYTGHVAGSDTW8YE"
# length = int(input("Enter length:"))
# password=" "

# for a in range(length):
#    password += random.choice(chars)
#    print(password)
import random
chars = "jgjsfsnms$##@#$fdx^&56157256729SbvjfjrngmhnbFVfdvchgbugvf"
length = int(input("Enter length:"))
password = " "

for a in range(length):
  password += random.choice(chars)
print(password)  