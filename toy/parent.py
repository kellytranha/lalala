import sys

def main():
    contents = sys.stdin.read().split()
            
    y = contents[0]
    p = contents[1]

    if y[-1] == "e":
        result = y + "x" + p
    elif y[-1] in "aiou":
        result = y[:-1] + "ex" + p
    elif y[-2:] == "ex":
        result = y + p
    else:
        result = y + "ex" + p

    print(result)
    
if __name__ == "__main__":
    main()
    
