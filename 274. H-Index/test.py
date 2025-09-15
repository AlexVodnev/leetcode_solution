def hIndex(citations):
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

citations = [[3,0,6,1,5], [1,1,3], [1], [8,2,8,9,2]]
for i in citations:
    print(hIndex(i))