def custom_range(num1, num2=None, iter=1):
    iter_counter = 0
    counter = 0
    ending_num = num1

    if num2:
        counter = num1
        ending_num = num2

    num_list = []
    while counter < ending_num:
        if iter_counter % iter == 0:
            num_list.append(counter)
        counter += 1
        iter_counter += 1

    return num_list
    
for x in range(10):
    print(x)
    
print('\n')

for x in custom_range(10):
    print(x)

print('------------------------------------------------------------------------------------------')

for x in range(10, 20, 2):
    print(x)
    
print('\n')

for x in custom_range(10, 20, 2):
    print(x)
