def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0 and price > 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)           
        elif price < 0:
            print('Error. Please enter a valid positive price')
        else:
            moreItems = False
    if total == 0:
        print('You can not compute an average without data')
    else:          
        average = total / count
        print('Total items:', count)
        print('Total $', total)
        print('Average price per item: $', average)
    
checkout()
