class Solution:
    def decodeString(self, s):
        num_stack = []
        str_stack = []

        current = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                num_stack.append(num)
                str_stack.append(current)
                num = 0
                current = ""

            elif ch == ']':
                repeat = num_stack.pop()
                previous = str_stack.pop()
                current = previous + current * repeat

            else:
                current += ch

        return current