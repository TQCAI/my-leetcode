package structure;

public class ListNode {
    public int val;
    public ListNode next;

    public ListNode() {
    }

    public ListNode(int val) {
        this.val = val;
    }

    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    public static ListNode fromArray(int[] list) {
        ListNode head = null;
        ListNode tail = null;
        for (int item : list) {
            ListNode node = new ListNode(item);
            if (head == null) {
                head = node;
                tail = node;
            } else {
                tail.next = node;
                tail = node;
            }
        }
        return head;
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
        ListNode p = this;
        while (p != null) {
            res.append(p.val).append(" -> ");
            p = p.next;
        }
        res.append("O");
        return res.toString();
    }
}