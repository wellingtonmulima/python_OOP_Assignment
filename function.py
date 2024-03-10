def calculate_discount(original_price,discount_percent):
    if discount_percent>=20:
        discount_amount=original_price*(discount_percent/100)
        final_price=original_price-discount_amount
        return final_price
    else:
        return original_price
    
original_price=float(input('Enter original price:'))
discount_percent=float(input('Enter the discount:'))
    
final_price=calculate_discount(original_price,discount_percent)
    
if final_price != original_price:
    
    print(final_price)
    
else:
    print(original_price)
    

      

    
    

    
    