n = int(input().strip())
arr = list(map(int, input().split()))
max_dif = 0
for i in range(n//2):
    #print(arr)
    max_id = arr.index(max(arr))
    #print(max_id)
    if max_id==0:
        id_min_neighbour = 1
        max_dif += abs(arr[max_id]-arr[id_min_neighbour])
        arr.pop(0)
        arr.pop(0)
        #print('+')
    elif max_id==(len(arr)-1):
        id_min_neighbour = -2
        max_dif += abs(arr[max_id] - arr[id_min_neighbour])
        arr.pop(-1)
        arr.pop(-1)
    else:
        id_min_neighbour = arr.index(min(arr[max_id+1], arr[max_id-1]))
        max_dif += abs(arr[max_id] - arr[id_min_neighbour])
        temp_id = min(max_id, id_min_neighbour)
        arr.pop(temp_id)
        arr.pop(temp_id)
    #print(arr)
print(max_dif)