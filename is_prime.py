def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))

prime_numbers = find_primes(start_range, end_range)

print("Prime numbers between", start_range, "and", end_range, "are:")
for prime in prime_numbers:
    print(prime)
