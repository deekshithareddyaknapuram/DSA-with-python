def subarray_with_k_different_integers(nums, k):
    if k > len(set(nums)):
        return 0

    left = 0
    right = 0
    count = {}
    unique = 0
    max_length = 0

    while right < len(nums):
        if nums[right] not in count:
            unique += 1
        count[nums[right]] = count.get(nums[right], 0) + 1

        while unique > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                unique -= 1
            left += 1

        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length
