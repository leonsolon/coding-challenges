#90'

#PERSONAL NOTE: I could not find a solution using recursion. Instead, I devised a iterative
#approach based on the generalization of the algorithm described below, which is hardcoded
#to the case where k = 3 (which requires 3 loops).

#LESSON LEARNED: find all possible combinations!

#Link: https://leetcode.com/problems/combinations/

#DESCRIPTION:
    # Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
    # You may return the answer in any order.


""" Lets say your array of letters looks like this: "ABCDEFGH". You have three indices (i, j, k) indicating which letters you are going to use for the current word, You start with:

A B C D E F G H
^ ^ ^
i j k
First you vary k, so the next step looks like that:

A B C D E F G H
^ ^   ^
i j   k
If you reached the end you go on and vary j and then k again.

A B C D E F G H
^   ^ ^
i   j k

A B C D E F G H
^   ^   ^
i   j   k
Once you j reached G you start also to vary i.

A B C D E F G H
  ^ ^ ^
  i j k

A B C D E F G H
  ^ ^   ^
  i j   k
...
Written in code this look something like that

void print_combinations(const char *string)
{
    int i, j, k;
    int len = strlen(string);

    for (i = 0; i < len - 2; i++)
    {
        for (j = i + 1; j < len - 1; j++)
        {
            for (k = j + 1; k < len; k++)
                printf("%c%c%c\n", string[i], string[j], string[k]);
        }
    }
} """


from typing import List

# Runtime: 124 ms, faster than 90.03% of Python3 online submissions for Combinations.
# Memory Usage: 15.9 MB, less than 52.30% of Python3 online submissions for Combinations.
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = [1]
        res = []
        while stack:
            if len(stack) == k:
                res.append(list(stack))
                
                while stack and (x := stack.pop()) == n - (k - len(stack) - 1): 
                    pass
                
                #if d is empty and x >= n - (k - len(d) -1) means we must stop. Therefore, do not append!
                if stack or x < n - (k - len(stack) - 1):
                    stack.append(x + 1)    
            else:
                stack.append(stack[-1] + 1)
        return res
