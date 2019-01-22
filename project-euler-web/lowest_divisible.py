# Returns True if the given number is prime and False otherwise.
def is_prime(number):
    if number == 2:
        return True
    for i in range(3, int(number ** 0.5) + 1, + 2):
        if number % i == 0:
            return False
    return True


# Returns a list of all the prime numbers that construct the given number.
def prime_factors(number):
    prime_list = {}
    for i in range(2, int(number ** 0.5) + 1):
        counter = 0
        while number % i == 0:
            counter += 1
            prime_list[str(i)] = counter
            number //= i
    if not number == 1:
        prime_list[str(number)] = 1
    return prime_list


# Returns the smallest number that is divisible by all of the integers in the range from 1 until a given top value
def smallest_divisible(top_number):
    num_to_return = 1
    list_to_multiply = {}
    for i in range(2, int(top_number) + 1):
        current_prime_factors = prime_factors(i)
        for prime_factor in current_prime_factors.keys():
            if prime_factor in list_to_multiply.keys():
                if list_to_multiply[prime_factor] < current_prime_factors[prime_factor]:
                    list_to_multiply[prime_factor] = current_prime_factors[prime_factor]
            else:
                list_to_multiply[prime_factor] = current_prime_factors[prime_factor]
    for num_to_multiply in list_to_multiply.items():
        num_to_return *= (int(num_to_multiply[0]) ** num_to_multiply[1])
    return num_to_return