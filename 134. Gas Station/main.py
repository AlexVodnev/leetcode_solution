class MySolution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        r = [a - b for a, b in zip(gas, cost)]
        if sum(r) >= 0:
            pass
        else:
            return -1
        max_value = max(r)
        i = r.index(max_value)
        while True:
            t = 0
            if r[(i)%len(r)] < 0:
                i += 1
            else:
                for j in range(len(r)):
                    t += r[(i + j)%len(r)]
                    if t < 0:
                        i += 1
                        break
                    elif j == len(r) - 1:
                        return i%len(r)

class CommunitySolution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
                
        curernt_gas = 0
        start = 0
        for i in range(len(gas)):
            curernt_gas += gas[i] - cost[i]
            if curernt_gas < 0:
                curernt_gas = 0
                start = i + 1

        return start
