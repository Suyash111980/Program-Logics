
food={
    "veg":
    {
        "masala papad":100,
        "abc":200,
        "xyz":300
    },

    "nonveg":
    {
        "n1":100,
        "n2":200

    }
}


for category,items in food.items():
    print(category)

    for item,price in items.items():
        print(item,"=",price)