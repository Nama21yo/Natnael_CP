def main():
    t = int(input()) 
    for _ in range(t):
        words = input().split(" ")
        new1 = words[1][0] + words[0][1:]
        new2 = words[0][0] + words[1][1:]
        print(new1 + " " + new2)

main()