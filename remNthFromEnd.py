def remnthFromEnd(head, n):
	iterNode1 = iterNode2 = head
    for i in range(n):
        iterNode1 = iterNode1.next
    if not iterNode1:
        return head.next
    while(iterNode1.next):
        iterNode1 = iterNode1.next
        iterNode2 = iterNode2.next
    iterNode2.next = iterNode2.next.next
    return head
	