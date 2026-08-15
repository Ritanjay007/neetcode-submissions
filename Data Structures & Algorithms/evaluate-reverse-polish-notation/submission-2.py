class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack=[]
        o_list =['+','-','*','/']
        for char in tokens:
            if char not in o_list:
                self.stack.append(char)
            else:
                sec_val = int(self.stack.pop())
                first_val = int(self.stack.pop())
                if char == "+":
                    new_val = first_val + sec_val
                elif char == "-":
                    new_val = first_val - sec_val
                elif char == "*":
                    new_val = first_val * sec_val
                else:
                    new_val = int(first_val / sec_val)  # handles truncating towards zero
                self.stack.append(new_val)

        return int(self.stack[0])
