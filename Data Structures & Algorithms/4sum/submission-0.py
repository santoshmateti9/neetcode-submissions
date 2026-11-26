class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = set()
        final = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    diff = target - (nums[i] + nums[j] + nums[k])
                    
                    if diff in final:
                        final_list = [diff,nums[i],nums[j],nums[k]]
                        final_list.sort()
                        final_tuple = tuple(final_list)
                        output.add(final_tuple)

            final.add(nums[i])
        return [list(o) for o in output]