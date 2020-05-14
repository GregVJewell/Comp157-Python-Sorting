# Returns index of k in arr if present, else -1 
def binarySearch (arr, l, r, k): 

	# Check base case 
	if r >= l: 
		mid = l + (r - l)//2

		# If element is present at the middle itself 
		if arr[mid] == k: 
			return mid 
		
		# If element is smaller than mid, then it can only be present in left subarray 
		elif arr[mid] > k: 
			return binarySearch(arr, l, mid-1, k) 

		# Else the element can only be present in right subarray 
		else: 
			return binarySearch(arr, mid+1, r, k) 

	else:
		# Element is not present in the array 
		return -1
