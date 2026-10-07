class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isValid(x):
            count = 0

            for ch in x:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        level = {s}

        while level:
            valid = [x for x in level if isValid(x)]

            if valid:
                return valid

            next_level = set()

            for x in level:
                for i in range(len(x)):
                    if x[i] in '()':
                        next_level.add(x[:i] + x[i + 1:])

            level = next_level

        return [""]