def num_within(num_check, num_start, num_finish):
    return (num_check >= num_start and num_check <= num_finish)


print(num_within(3, 1, 3))
print(num_within(10, 2, 5))