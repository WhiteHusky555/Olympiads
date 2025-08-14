class Track:
    def __init__(self, rate, number):
        self.rate: int = rate
        self.number: int = number

tracks, coms = map(int, str(input()).split())
arr=[Track(x, x) for x in range(1, tracks+1)]
for _ in coms:
    com = list(map(int, str(input()).split()))
    if com[0] == 1:
        print(arr[com[1]].rate)
        for i in range(len(arr)):
            if arr[i].number == com[1]:
                arr[i].number = com[2]
    elif com[0] == 2:
        sv = arr[com[1]].rate
        print(arr[com[1]].rate)
        for i in range(len(arr)):
            if arr[i].number == com[1]:
                arr[i].rate = 1
            else:
                if arr[i].rate < arr[com[1]].rate:
                    arr[i].rate += 1
    elif com[0] == 3:


    elif com[0] == 4:
