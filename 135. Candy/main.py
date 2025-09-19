class Solution:
    def candy(self, ratings: list[int]) -> int:
        candys = [1]*len(ratings)
        if len(ratings) == 1:
            return 1
        elif len(ratings) == 2:
            if ratings[0] == ratings[1]:
                return 2
            else:
                return 3
        else:
            for i in range(len(ratings) - 1):
                if ratings[i] < ratings[i + 1]:
                    candys[i+1] = candys[i] + 1
            for i in range(len(ratings) - 1, 0, -1):
                if ratings[i] < ratings[i - 1]:
                    if candys[i - 1] <= candys[i]:
                        candys[i - 1] = candys[i] + 1
            return sum(candys) 

s = Solution()
list_ratings = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 1], [0, 1, 2, 2], [0, 1, 2, 1], [0, 1, 2, 2, 1], [3,2,1,0,1,2,3]]
for ratings in list_ratings:
    print("For", ratings, "candys sum =", s.candy(ratings))