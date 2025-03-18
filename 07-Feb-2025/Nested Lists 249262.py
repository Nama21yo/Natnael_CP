# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    t = int(input())
    students = [[input(), float(input())] for _ in range(t)]
    second_high = sorted(set([score for name,score in students]))[1]
    
    for name, score in sorted(students):
        if score == second_high:
            print(name)
