class Solution
{
public:
    int evalRPN(vector<string> &tokens)
    {
        stack<int> stk;
        for (string i : tokens)
        {
            if (i == "+")
            {
                int a = stk.top();
                stk.pop();
                int b = stk.top();
                stk.pop();
                stk.push(b + a);
            }
            else if (i == "*")
            {
                int a = stk.top();
                stk.pop();
                int b = stk.top();
                stk.pop();
                stk.push(b * a);
            }
            else if (i == "/")
            {
                int a = stk.top();
                stk.pop();
                int b = stk.top();
                stk.pop();
                stk.push(b / a);
            }
            else if (i == "-")
            {
                int a = stk.top();
                stk.pop();
                int b = stk.top();
                stk.pop();
                stk.push(b - a);
            }
            else
                stk.push(stoi(i));
        }
        return stk.top();
    }
};