# restaurant ordering system
# user chooses an item, and it gets added to cart
# calculate the total bill also add remove item from cart feature before checking out!
# add a bonus if bill greater than 1k

items = {
    "daal chawal": 150,
    "daal roti": 120,
    "biryani": 250,
    "chicken pulao": 220,
    "dosa": 180,
    "paratha roll": 200,
    "shawarma": 250,
    "burger": 300,
    "pizza slice": 350,
    "fries": 100,
    "cold drink": 80,
    "chai": 50
}

def displaymenu():
    print("\n|-----------------------------------Menu----------------------------------------|\n")
    count = 0
    for item, price in items.items():
        count += 1
        print(f"Item: {item}, Price: {price}$ ".center(40), end=" ")
        if count % 2 == 0:
            print()
    print("\n|-----------------------------------Menu----------------------------------------|\n")

def showcart(numbercount):
    print("\n-------Your Cart-------")

    if numbercount == {}:
        print("Cart Empty!".center(23))

    else:
        for food, qty in numbercount.items():
            print(f"{food.center(20)} x{qty}")
    print("\n----------------------")



def main():
    total = 0
    cart = []
    numbercount = {}
    is_ordering = True
    displaymenu()
    while is_ordering:
        print()
        print("\033[1mR to remove an item, Checkout To checkout, Cart to see Your cart, M for Menu!\033[0m")
        buyfood = input("What do you want to buy?: ").lower()
        if buyfood == "checkout":
            if total >= 1000:
                discount = total * 0.25
                total -= discount
                print(f"Price after discount {total}$")
                print(f"Your total was {total}$!")
                showcart(numbercount)
                is_ordering = False
            else:
                print("No discount applied total was under 1,000$!")
                print(f"Your total was {total}$!")
                showcart(numbercount)
                is_ordering = False

        if buyfood == "r" or buyfood == "remove":
            removeitem = input("Which item do you want to remove?!: ").lower()
            if removeitem in cart:
                total -= items[removeitem]
                cart.remove(removeitem)
                if numbercount[removeitem] - 1 == 0:
                    del numbercount[removeitem]
                else:
                    numbercount[removeitem] -= 1
                print(f"{removeitem} Removed from Cart!")
            else:
                print("Not Valid!")


        if not buyfood or buyfood.isdigit():
            print("Invalid input!")
            continue


        if buyfood in ["cart"]:
            showcart(numbercount)
            continue

        if buyfood in ["m", "menu"]:
            displaymenu()
            continue

        if buyfood in items:
            cart.append(buyfood)
            numbercount[buyfood] = numbercount.get(buyfood, 0) + 1
            total += items[buyfood]
            print(f"{buyfood} added to cart!, Your Total is {total}$")

        elif buyfood in ["r","remove","checkout","cart","m","menu"]:
            continue

        else:
            print(f"{buyfood} Is not available!")




if __name__ == "__main__":
    main()
