def fun(S):
    s = "@#" + "#".join(S) + "#$"
    counts = [0] * len(s)
    center = right = 0
    for i in range(1, len(s)-1):
        if i < right:
            # counts[i] = counts[2 * center - i] # abab
            counts[i] = min(right-i, counts[2*center-i])
        while s[i-counts[i]-1] == s[i+counts[i]+1]:
            counts[i] += 1
        if i + counts[i] > right:
            center, right = i, i + counts[i]
    return sum([(val+1)//2 for val in counts])


if __name__ == "__main__":
    S = 'abab'
    print(fun(S))
