def getDuplicate(sequence) -> int:

    ok_sum = sumNumber(len(sequence) - 1)
    current_sum = 0

    for n in sequence:
        current_sum += n

    return current_sum - ok_sum




def sumNumber(nums):
    return_number = 0
    for i in range(nums):
        return_number += i + 1

    return return_number

print(getDuplicate([1, 6, 3, 2, 5, 4, 6]))