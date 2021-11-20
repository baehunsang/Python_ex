import collections
str = "ebcbcacdb"
#eacdb

def removeDup(s: str) ->str:
	list = []
	counter = collections.Counter(s)
	
	for char in s:
		counter[char] -= 1
		if(char in list):
			continue
		while(list and char < list[-1] and counter[list[-1]] > 0):
			list.pop()
		list.append(char)
	return ''.join(list)

print(removeDup(str))	 
