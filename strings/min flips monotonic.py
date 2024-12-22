class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        '''
        1s = 2
        flipped = 0

        00110
            ^
        if we pass 1 and see a 0, should we flip it?
        

        as we go through we can recursively ask ourselves:
        assuming everything prior is monotonic, i'm at a mismatch, I need to do a flip to either
        the current character or the character before me. Either way that's 1 flip
        let's have a bias to flip the ones we encounter
        '''
        ones = 0
        flipped = 0
        

        for c in s:
            if c == '1':
                ones += 1
            else:
                #it's a 0
                if ones > 0:
                    flipped += 1
                    ones -= 1
        return flipped
