def prime(number):
    prime_c = 1 # create prime counter that starts at one for the number 2
    for current_num in range(3,number+1,2): # for loop that goes from 3-number by increments of 2
        prime_tracker = True  # variable to keep track if number is prime/ reset tracker for new numbers
        for num in range(3,current_num): # for loop that tracks the current number in iteration
            if current_num % num == 0: # determines if the current number is composite
                prime_tracker = False
                break
            elif num > (current_num**.5): # exits loop if no multiple found by sq root
                break
        if prime_tracker == True: # if tracker doesnt switch during iteration add 1 to prime counter
            prime_c +=1
    return prime_c
