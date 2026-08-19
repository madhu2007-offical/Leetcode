/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (!head || !head->next) return head; // empty or single node

        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even; // to attach at the end of odd list

        while (even && even->next) {
            odd->next = even->next;   // link next odd node
            odd = odd->next;          // move odd pointer
            even->next = odd->next;   // link next even node
            even = even->next;        // move even pointer
        }

        odd->next = evenHead; // attach even list after odd
        return head;
    }
};