#include <stack>
#include <string>

bool brace_matching(std::string string) {
    std::stack<char> bracket_stack;
    for(auto it = string.begin(); it != string.end(); ++it) {
        char const& c = *it;
        switch (c)
        {
        case '(':
        case '[':
        case '{':
            bracket_stack.push(c);
            break;
        case '\'':
        case '"':
            if(it == string.begin() || *(it - 1) != '\\') {
                if(c == bracket_stack.top()) {
                    bracket_stack.pop();
                } else {
                    bracket_stack.push(c);
                }
            }
            break;
        case ')':
        case ']':
        case '}':
            if(c != bracket_stack.top()) {
                return false;
            } else {
                bracket_stack.pop();
            }
            break;
        }
    }
    return bracket_stack.empty();
}