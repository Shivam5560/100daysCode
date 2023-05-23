class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev = None
        for x in range(len(numbers)):
            if numbers[x] != prev:
                prev = numbers[x]
            else:
                continue
            for y in range(x+1,len(numbers)):
                val = numbers[x]+numbers[y]
                if  val == target:
                    return [x+1,y+1]
                elif val>target:
                    break
                else:
                    pass
                
