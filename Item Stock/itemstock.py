item_number=[101,102,103,104]
item_name=['Milk','Cheese','Ghee','Bread']
item_price=[42,50,500,40]
item_stock=[10,20,15,16]
itemnum=int(input())
item_quantity=int(input())
try:
    index=item_number.index(itemnum)
except ValueError:
   print("Invalid input")
   exit()

if item_quantity<=item_stock[index]:
    price=float(item_price[index]*item_quantity)
    item_stock[index]-=item_quantity
    print(price,"INR")
    print(ist[index],"LEFT")
else:
    if item_stock[index]<item_quantity:
        print("NO STOCK")
        print(item_stock[index],"LEFT")