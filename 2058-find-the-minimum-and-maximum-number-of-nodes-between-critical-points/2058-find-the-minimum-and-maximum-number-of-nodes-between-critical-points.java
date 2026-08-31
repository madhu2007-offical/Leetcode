class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {

        int minDistance = Integer.MAX_VALUE;
        int first = -1;
        int prevCritical = -1;

        ListNode prev = head;
        ListNode curr = head.next;

        int index = 1;

        while (curr.next != null) {

            ListNode next = curr.next;

            // Check if current node is a critical point
            boolean isCritical =
                    (curr.val > prev.val && curr.val > next.val) ||
                    (curr.val < prev.val && curr.val < next.val);

            if (isCritical) {

                // First critical point
                if (first == -1) {
                    first = index;
                }

                // We already have a previous critical point
                if (prevCritical != -1) {
                    minDistance = Math.min(
                        minDistance,
                        index - prevCritical
                    );
                }

                prevCritical = index;
            }

            prev = curr;
            curr = next;
            index++;
        }

        // Fewer than two critical points
        if (first == -1 || first == prevCritical) {
            return new int[]{-1, -1};
        }

        // Maximum distance = last critical - first critical
        int maxDistance = prevCritical - first;

        return new int[]{minDistance, maxDistance};
    }
}