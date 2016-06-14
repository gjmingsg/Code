class ListNode {
	int val;
	ListNode next;
	ListNode(int x) { val = x; }
    }

public class RemoveLinkedListElements {
 
    /**
     * @param head a ListNode
     * @param val an integer
     * @return a ListNode
     */
    public ListNode removeElements(ListNode head, int val) {
	ListNode t = head,pre=t;
	ListNode fh = new ListNode(0);
	fh.next=head;
	pre=fh;
	while(t!=null){
	    if(t.val == val){
		pre.next=t.next;
	    }
	    else{
		pre = t;
	    }
	    t = t.next;
	}
	return fh.next;
    }

    public void print(ListNode head){
	ListNode t = head;
	while(t!=null){
	    System.out.println(t.val);
	    t = t.next;
	}
	
    }
    public static void main(String[] args){
	RemoveLinkedListElements test = new RemoveLinkedListElements();
	ListNode node = new ListNode(1);
	node.next= new ListNode(2);
	node.next.next = new ListNode(3);
	ListNode head = test.removeElements(node,3);
	test.print(head);
	
    }
}
