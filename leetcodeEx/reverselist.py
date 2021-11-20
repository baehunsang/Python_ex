class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None
	
	def push(self, val):
		runner = self
		while(runner.next):
			runner = runner.next
		runner.next = ListNode(val)
		
		
def toList(root: ListNode):
	runner = root.next
	list = []
	while(runner):
		list.append(runner.val)
		runner = runner.next
	return list	
	
root = ListNode(None)

for i in range(1, 10):
	root.push(i)

print(toList(root))

def reverse(head: ListNode) -> ListNode:
	prev = None
	node = head
	while(node):
		tmp = node.next
		node.next = prev
		prev = node
		node = tmp
	return prev


root.next = reverse(root.next)

	
print(toList(root))



