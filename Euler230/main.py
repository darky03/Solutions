
def fibonacci(a,b,n):
    tA = a
    tB = b
    for i in range(2,n):
        tempStr = tA + tB
        tA = tB
        tB = tempStr
        if len(tempStr) >= n:
            print(tempStr[n-1])
            break

if __name__ == "__main__":
    total = int(input())
    if total >= 1 and total <= 100:
        for i in range(0,total):
            inputString = input()
            inputSplits = inputString.split(" ")
            partA = inputSplits[0]
            partB = inputSplits[1]
            k = int(inputSplits[2])
            if len(partA) >= 1 and len(partA) <= 100:
               if len(partB) >= 1  and len(partB) <= 100:
                   if k >= 1 and k <= 2**100:
                        fibonacci(partA,partB,k)
                        pass
            

