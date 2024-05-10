class MyLinkedList
{
private:
    int size;

    struct ListNode
    {
        int val;
        ListNode *next;

        // ListNode(int v, ListNode* ptr = nullptr){
        //     val = v;
        //     next = ptr;
        // }
    };
    ListNode *head;

public:
    MyLinkedList()
    {
        head = nullptr;
        size = 0;
    }

    int get(int index)
    {
        if (index >= size || head == nullptr) // invalid index;
            return -1;

        // index is valid.
        int i = 0;
        int val;
        ListNode *nodeptr = head;
        while (nodeptr)
        {
            if (i == index)
            {
                val = nodeptr->val;
                break;
            }
            i++;
            nodeptr = nodeptr->next;
        }
        return val;
    }

    void addAtHead(int val)
    {
        addAtIndex(0, val);
    }

    void addAtTail(int val)
    {
        addAtIndex(size, val);
    }

    void addAtIndex(int index, int val)
    {
        if (index > size) // check validity of index.
            return;

        // create the new node for the value to be added.
        ListNode *newNode = new ListNode;
        newNode->val = val;
        newNode->next = nullptr;

        if (index == 0)
        { // if i want to add to head.
            newNode->next = head;
            head = newNode;
        }
        else
        { // adding at any index other than 0.
            ListNode *nodeptr = head;
            for (int i = 0; i < index - 1; i++)
                nodeptr = nodeptr->next;

            newNode->next = nodeptr->next;
            nodeptr->next = newNode;
        }
        size++;
    }

    void deleteAtIndex(int index)
    {
        if (index >= size)
            return;
        else if (index == 0)
        {
            ListNode *temp = head;
            head = head->next;
            delete temp;
        }
        else
        {
            ListNode *prevNode = nullptr;
            ListNode *nodeptr = head;

            for (int i = 0; i < index; i++)
            {
                prevNode = nodeptr;
                nodeptr = nodeptr->next;
            }

            ListNode *temp = nodeptr;
            prevNode->next = nodeptr->next;
            delete temp;
        }
        size--;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */