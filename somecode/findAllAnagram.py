from collections import Counter


def findAnagrams(s: str, p: str):
    if len(s) < len(p) or not s or not p:
        return []
    counter0 = Counter(p)
    counter = {}
    ans = []
    n = len(s)
    l = 0
    r = -1
    while r < len(p) - 1:
        r += 1
        if s[r] in counter:
            counter[s[r]] += 1
        else:
            counter[s[r]] = 1
    if counter == counter0:
        ans.append(l)

    while r < n - 1:
        counter[s[l]] -= 1
        if counter[s[l]] == 0:
            del counter[s[l]]
        l += 1
        r += 1
        if s[r] in counter:
            counter[s[r]] += 1
        else:
            counter[s[r]] = 1

        if counter == counter0:
            ans.append(l)
    return ans

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))