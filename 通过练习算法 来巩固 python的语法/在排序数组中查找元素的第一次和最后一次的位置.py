from typing import List


class Solution:
    """
    二分查找
    """

    def searchRange(self,nums:List[int],target:int) ->List[int]:
        """
        searchLeft:查找左边界
        searchRight:查找右边界
        :param nums:
        :param target:
        :return:
        """
        def searchLeft(nums:List[int],target:int) -> int:
            left,right = 0,len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if mid ==0 or nums[mid-1]<target:
                        return mid
                    right = mid-1
                elif nums[mid]<target:
                    left = mid + 1
                else:
                    right = mid -1

            return -1

        def searchRight(nums:List[int],target:int) -> int:
            left,right = 0,len(nums)-1
            while left <= right:
                mid = (left+right)//2

                if nums[mid]==target:
                    if mid ==len(nums)-1 or nums[mid+1]>target:
                        return mid
                    left = mid+1
                elif nums[mid]<target:
                    left = mid + 1
                else:
                    right = mid -1
            return -1

        return [searchLeft(nums,target),searchRight(nums,target)]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10],8)) #[3,4]
    print(s.searchRange([5,7,7,8,8,10],6)) #[-1,-1]



