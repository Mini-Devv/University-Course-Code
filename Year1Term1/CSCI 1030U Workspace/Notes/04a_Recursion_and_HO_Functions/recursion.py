#Decimal: digits can be 0-9, e.g. 206, 000206
#Binary: digits can be 0 or 1, e.g 1101 = 13 (decimal), 00001101

def to_binary(n, num_digits):
    result = ''
    digit_num = 0
    
    while (digit_num < num_digits):
        result = str(n % 2) + result
        n = n // 2

        digit_num += 1    

    return result

#print(to_binary(13, 8))

def print_n_times(n, message):
    #base case - otherwise we'd never exit
    if n < 1:
        return

    print(f'{message} {n}')
    print_n_times(n - 1, message)

print_n_times(3, 'hello')

def fib(n):
    #base case
    if n <= 1:
        return n

    
    #recursive case
    #TODO: Write the code (1 line)

def fib_efficient(n):
    if n <= 1:
        return n
    
    last_fib = 1
    prev_fib = 0
    current_index = 1

    while current_index < n:
        current_fib = last_fib + prev_fib
        prev_fib = last_fib
        last_fib = current_fib
        current_index += 1 
    return last_fib

#print(fib_efficient(100))
