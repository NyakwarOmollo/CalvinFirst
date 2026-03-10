def check_sign(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")


# Test cases
check_sign(10)     
check_sign(-5)     
check_sign(0)      
check_sign(3.7)    
check_sign(-0.1)   
check_sign(0.0)    