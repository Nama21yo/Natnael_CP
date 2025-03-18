# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    ans_list = []
    while N > 0:
        rule = list(map(str, input().split()))
        if rule[0] == "append":
            ans_list.append(int(rule[1]))
        elif rule[0] == "print":
            print(ans_list)
        elif rule[0] == "insert":
            pos = int(rule[1])
            ele = int(rule[2])
            ans_list.insert(pos, ele)
        elif rule[0] == "remove":
            ans_list.remove(int(rule[1]))
        elif  rule[0] == "sort":
            ans_list.sort()
        elif rule[0] == "pop":
            ans_list.pop()
        elif rule[0] == "reverse":
            ans_list.reverse()  
        N -= 1
            
        