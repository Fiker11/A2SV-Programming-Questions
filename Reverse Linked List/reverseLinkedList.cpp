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
class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        ListNode *reverseHead = nullptr;
        // ListNode *nodeptr = head;

        while (head != nullptr)
        {
            ListNode *newnode = new ListNode;
            newnode->val = head->val;

            // if(reverseHead == nullptr){
            //     reverseHead = newnode;
            // }
            // else{
            newnode->next = reverseHead;
            reverseHead = newnode;
            // }
            ListNode *temp = head;
            head = head->next;
            delete temp;
        }
        return reverseHead;
    }
};