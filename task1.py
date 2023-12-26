import time

def collatz_sequence_length(n, lengths):
    if n == 1:
        return 1
    if n < len(lengths) and lengths[n] != 0:
        return lengths[n]

    original_n = n
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1

        if n < len(lengths) and lengths[n] != 0:
            lengths[original_n] = length + lengths[n]
            return lengths[original_n]

    lengths[original_n] = length
    return length

def find_longest_collatz_sequence(limit):
    max_length = 0
    starting_number = 0
    lengths = [0] * (limit + 1)

    for i in range(1, limit):
        current_length = collatz_sequence_length(i, lengths)
        if current_length > max_length:
            max_length = current_length
            starting_number = i

    return starting_number, max_length

start_time = time.time()
result = find_longest_collatz_sequence(1000000)
end_time = time.time()

print(f"Starting Number: {result[0]}")
print(f"Sequence Length: {result[1]}")
print(f"Execution Time: {end_time - start_time} seconds")
