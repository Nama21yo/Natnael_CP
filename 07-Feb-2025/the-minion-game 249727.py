# Problem: the-minion-game - https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

# from collections import defaultdict

def minion_game(string):
    # O(n^2) - generate all substring
    # word_score = defaultdict(int)
    # for i in range(len(string)):
    #     for j in range(0, len(string)):
    #         # check all substring
    #         word_score[s[i:j + 1]] += 1
    
    # Optimization
    set_vowel = set(["A","E","I","O","U"])
    kevin_score = 0
    stuart_score = 0
    n = len(string)
    for i,char in enumerate(string):
        if char in set_vowel:
            kevin_score += n - i
        else:
            stuart_score += n - i
    
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")
        

if __name__ == '__main__':
    s = input()
    minion_game(s)