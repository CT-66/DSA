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
    // dummy pointer
    /*
    ListNode *removeElements(ListNode *head, int val) {
        ListNode *ans = new ListNode(0, head);
        ListNode *dummy = ans;

        while (dummy != nullptr) {
            while (dummy->next != nullptr && dummy->next->val == val) {
                dummy->next = dummy->next->next;
            }
            dummy = dummy->next;
        }

        ListNode *result = ans->next;
        delete ans;

        return result;
    }
    */

    // without dummy pointer
    ListNode *removeElements(ListNode *head, int val) {
        while (head != nullptr && head->val == val) {
            head = head->next;
        }

        ListNode *curr = head;

        while (curr != nullptr && curr->next != nullptr) {
            if (curr->next->val == val) {
                curr->next = curr->next->next;
            } else {
                curr = curr->next;
            }
        }

        return head;
    }
};
