array = [1, 3, 1, 3, 1, 3, 1]
prefix = [0] * (len(array) + 1)

for i in range(len(array)):
    prefix[i + 1] = prefix[i] + array[i]

print(prefix[4 + 1] - prefix[2])

"""
A[] = [1, 3, 1, 3, 1, 3, 1]
PREF[] = [0, 1, 4, ...]

PREF[K + 1] = PREF[K] + A[K]

Sum from L to R
=> PREF[R + 1] - PREF[L]
"""
