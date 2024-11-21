def getMinNumber(text, search, wholeWord, start):
    # Write your code here


T = int(input())
for _ in range(T):
    text = input()
    search = input()
    wholeWord = input()
    start = int(input())

    out_ = getMinNumber(text, search, wholeWord, start)
    print (out_)
