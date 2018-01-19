def remnthFromEnd(head, n):
	temp = []
	iterNode = head
	while (iterNode.next != None):
		temp.append(iterNode) 
		iterNode = iterNode.next
	temp.append(iterNode)
	i = len(temp) - n
	temp[i - 1].next = temp[i-1].next.next
	return head
