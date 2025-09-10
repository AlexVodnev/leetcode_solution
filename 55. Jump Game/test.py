def canJump(nums):
    i = 0
    while i < len(nums):
        print("Step", i)
        r = i + nums[i]
        print("r =", r)
        if r < len(nums) - 1 and r != i:
            max_pos = r + nums[r]
            print("max_pos =", max_pos)
            n = r
            print("n =", n)
            for j in range(r, i, -1):
                print("j =", j)
                if (nums[j] != 0):
                    if j + nums[j] > max_pos:
                        max_pos = j + nums[j]
                        n = j
        elif r < len(nums) - 1 and r == i:
            return False
        else:
            return True
        if max_pos >= r + nums[r]:
            print("max_pos =", max_pos)
            print("nums[n] =", nums[n])
            print("n =", n)
            i = n - 1
        i += 1
        


nums = [2,3,1,1,4]
print(canJump(nums))