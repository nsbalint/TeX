start_range = 1
end_range = 10000

for num in range(start_range, end_range + 1):
    divisors_sum = sum(i for i in range(1, num) 
                       if num % i == 0)

    if divisors_sum == num:
        print(num)
