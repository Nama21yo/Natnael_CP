# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # c = Counter(a=3, b=1)
        # d = Counter(a=1, b=2)
        # c + d                       # add two counters together:  c[x] + d[x]
        # Counter({'a': 4, 'b': 3})
        # c - d                       # subtract (keeping only positive counts)
        # Counter({'a': 2})
        # c & d                       # intersection:  min(c[x], d[x])
        # Counter({'a': 1, 'b': 1})
        # c | d                       # union:  max(c[x], d[x])
        # Counter({'a': 3, 'b': 2})
        # c == d                      # equality:  c[x] == d[x]
        # False
        # c <= d                      # inclusion:  c[x] <= d[x]
        # False

        # c = Counter(a=4, b=2, c=0, d=-2)
        # sorted(c.elements())
        # ['a', 'a', 'a', 'a', 'b', 'b']

        # Counter('abracadabra').most_common(3)
        # [('a', 5), ('b', 2), ('r', 2)]

        # c = Counter(a=4, b=2, c=0, d=-2)
        # d = Counter(a=1, b=2, c=3, d=4)
        # c.subtract(d)
        # c
        # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

        # c = Counter(a=10, b=5, c=0)
        # c.total()
        # 15

        # c = Counter(a=2, b=-4)
        # +c
        # Counter({'a': 2})
        # -c
        # Counter({'b': 4})
        min_freq = Counter(words[0])
        for word in words:
            min_freq &= Counter(word)
        return list(min_freq.elements())