def check_validity(input_val): 
    stack = [] 
 
    for expr in input_val: 
        if expr in ["(", "{", "["]: 
  
            stack.append(expr) 
        else:  
            if not stack: 
                return False
            current_expr = stack.pop() 
            if current_expr == '(': 
                if expr != ")": 
                    return False
            if current_expr == '{': 
                if expr != "}": 
                    return False
            if current_expr == '[': 
                if expr != "]": 
                    return False
  
    if stack: 
        return False
    return True
  
  
if __name__ == "__main__": 
    expression = input()
  
    print(check_validity(expression))
