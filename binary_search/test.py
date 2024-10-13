nums = [1,1,2,2,3,4,4,5,5,9,9]

def singleNonDuplicate2(nums):
    start = 0
    end  = len(nums) - 2

    while end >= start:
        mid = (start+end) // 2
        if nums[mid] == nums[mid ^ 1]:
            start = mid + 1
        else:
            end = mid - 1

    return nums[start]

print(singleNonDuplicate2(nums))