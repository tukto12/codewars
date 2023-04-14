def twoSum(nums: list[int], target: int) -> list[int]:
    hash_map = {}

    for i in range(len(nums)):
        if target - nums[i] in hash_map:
            return [hash_map[target - nums[i]], i]
        hash_map[nums[i]] = i


test = [1, 3, 5, 7]
target = 4

print(twoSum(test, target))
