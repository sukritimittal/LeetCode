class Solution {
    public ListNode reverseList(ListNode head) {
       if(head == null){
           return head;
       }
        Stack<Integer> stack = new Stack<Integer>();
        ListNode result = new ListNode(0);
         ListNode dummy = new ListNode(0);
        dummy.next = result;
        while(head!=null){
            stack.push(head.val);
            head = head.next;
        }
        while(!stack.empty()){
            result.val = stack.pop();
            if(!stack.empty())
            result.next = new ListNode(0);
            else
                result.next = null;
            result = result.next;
        }
        
        return dummy.next;
    }
}
