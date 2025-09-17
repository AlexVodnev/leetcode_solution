import test_case as tc

def productExceptSelf(nums):
    set_list = list(set(nums))
    dic = dict.fromkeys(set_list, 1)
    for k, v in dic.items():
        con = 1
        for i in range(len(nums)):
            if k == nums[i] and con == 1:
                con = 0
            else:
                dic[k] = dic[k] * nums[i]
    res = [0]*len(nums)
    for i in range(len(nums)):
        res[i] = dic[nums[i]]
    return res
        

test_cases = [[1,2,3,4], [-1,1,0,-3,3], [0,0]]
for nums in test_cases:
    print(productExceptSelf(nums))