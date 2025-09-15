class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_v = -1
        citations = sorted(citations)
        for i in range(len(citations)):
            v = 0
            if citations[i] == 0:
                pass
            else:
                for j in range(i, len(citations)):
                    if citations[j] >= citations[i]:
                        v += 1
                    if  v == citations[i]:
                        break
            h_v = max(h_v, v)
        return h_v