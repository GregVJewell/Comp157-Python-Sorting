# Super straight-forward linear search
def search(arr, k): 
    for index in range(len(arr)): 
        if arr[index] == k: 
            return index
  
    return -1