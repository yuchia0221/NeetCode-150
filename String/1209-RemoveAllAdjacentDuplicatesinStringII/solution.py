from dataclasses import dataclass


@dataclass
class StackNode:
    char: str
    counter: int


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and stack[-1].char == char:
                stack[-1].counter += 1
            else:
                stack.append(StackNode(char, 1))

            if stack[-1].counter == k:
                stack.pop()

        output_string = ""
        for stack_node in stack:
            output_string += stack_node.char * stack_node.counter

        return output_string
