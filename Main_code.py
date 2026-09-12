Username = input("Enter your name : ")
print ("What you want to buy ")
item1 = input("Product Name : ")
qty1 = int(input("Product quantity in KG: "))
price1 = 400
item2 = input("Product Name : ")
qty2 = int(input("Product quantity in KG : "))
price2 = 800

Total_price1 = price1*qty1
GST = int(18/100)
Total_price2 = price2*qty2    

final_price1 = Total_price1 + GST*Total_price1 
final_price2 = Total_price2 + GST*Total_price2

# last output format

for i in range(0,31):
    print('--', end = "")

print(" \n                      TI Supermarket London UK ")

for i in range(0,31):
    print('--', end = "")

print("\n ||        Name          || ",Username)
for i in range(0,31):
    print('--', end = "")

print("\n ||     Product Name     || ",item1)
for i in range(0,31):
    print('--', end = "")
print("\n ||         Qty          || ",qty1)
for i in range(0,31):
    print('--', end = "")
print("\n ||  Product price + GST || ",final_price1)
for i in range(0,31):
     print('--', end = "")



print("\n ||     Product Name     || ",item2)
for i in range(0,31):
    print('--', end = "")
print("\n ||         Qty          || ",qty2)
for i in range(0,31):
    print('--', end = "")
print("\n ||  Product price + GST || ",final_price2)
for i in range(0,31):
     print('--', end = "")     
Bill = final_price1 + final_price2
print("\n ||          Bill        || ",Bill)
for i in range(0,31):
     print('--', end = "")    