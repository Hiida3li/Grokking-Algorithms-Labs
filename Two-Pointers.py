from sympy import false


def twoSum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True

        if current_sum < target:
            left += 1

        else:
            right -= 1


    return False

print(twoSum([2, 7, 11, 15], 19))





