# Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

def distinct(seq):
    nums = set()
    for num in seq:
        if num not in nums:
            nums.add(num)

    return False if len(seq) != len(nums) else True

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6]
    numbers2 = [1,2,3,4,5,5]
    print(distinct(numbers))
    print(distinct(numbers2))

