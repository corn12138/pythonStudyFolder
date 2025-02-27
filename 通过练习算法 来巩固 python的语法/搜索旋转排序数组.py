#搜索旋转排序数组
from typing import List


def search(nums:List[int],target:int) -> int:
    left,right = 0,len(nums) - 1

    while left <=right:
        mid = (left + right) // 2 # // 代表整除
        if nums[mid] == target:
            return mid

        # 左半部分有序
        if nums[left]<=nums[mid]:
            if nums[left] <= target< nums[mid]:
                right = mid -1
            else:
                left = mid + 1

        # 右半部分有序
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1 #没有找到

print(search([3,1],1))