'''
1.If you merge two arrays then the time complexiy becomes O(n+m). it will be accepted but you will not be able to learn anything.

2. You need to find the median of sorted merged array without merging it.

3. The hint is to find LEFT PART of merged array.

ex)
A = [{1, 2, 3}, 4, 5, 6, 7, 8]
B = [{1, 2, 3}, 4, 5]
     l             r
total = 13
num of left part = 13 // 2 -> 6

{} part is left part of merged array. 
it is because the number of element is 6 (13//2) and {}'s elements are small compared to any other element outside {}.

Now, you can manage {} part. If you use 2 pointer and binary search, then it's complexity will be O(log(min(n, m)))

'''
def findMedian(nums1, nums2)-> float:
	total = len(nums1) + len(nums2)
	half = total // 2 #number, not index!
	A, B = nums1, nums2
	if(len(B) < len(A)):
		A, B = B, A
	#index
	left = 0
	right = len(A) - 1
	while(True):# why this condition is correct? Think [1, 2], [3]
		mid = (left + right)//2#index
		last = half - mid - 2#number to index
		#exception handling
		# think A = [], B = [1, 2]
		A_left = A[mid] if(mid >=0) else float('-infinity')
		B_left = B[last] if (last >=0) else float('-infinity')
		A_right = A[mid + 1] if (mid + 1 < len(A)) else float('infinity')
		B_right = B[last + 1] if (last + 1 < len(B)) else float('infinity')
		
		if(A_left <= B_right and B_left <= A_right):
			if(total % 2 == 0):
				return (max(A[mid], B[last]) + min(A[mid + 1], B[last + 1]))/2
			else:
				return min(A[mid + 1], B[last + 1])
		elif(A_left > B_right):
			right = mid - 1
		else:
			left = mid + 1

# test

nums1 = [1, 2]
nums2 = [3]

print(findMedian(nums1, nums2))
	
