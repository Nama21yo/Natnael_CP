def missing_number(logs):
    n = len(logs)
    min_op = 0
    for file in logs:
        if file == "../":
            min_op -= 1
        elif file == "./":
            pass
        else:
            min_op += 1
    return min_op

def main():
    logs = [ "d1/", "d2/", "../", "d21/", "./", "d22/", "../", "../", "../","d1/", "d3/", "d4/", "./", "../", "d5/", "./", "../", "d6/","../", "../", "d7/", "d8/", "d9/", "d10/", "../", "../", "d11/","./", "d12/", "d13/", "d14/", "../", "../", "d15/", "../", "d16/","../", "d17/", "d18/", "../", "d19/", "d20/", "./", "../", "../","d21/", "d22/", "d23/", "../", "d24/", "../", "../", "../", "../","d25/", "d26/", "../", "../", "../"]
    print(missing_number(logs))

main()