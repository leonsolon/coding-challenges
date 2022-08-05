# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H=[]):
    blocks = []
    cutted_blocks = 0
    for i,h in enumerate(H):
        if len(blocks)==0 or (len(blocks)>0 and h>blocks[-1]):
            blocks.append(h)
        elif len(blocks)>0 and h < blocks[-1]:
            while len(blocks)>0 and h < blocks[-1]:
                cutted_blocks += 1
                blocks.pop()
            if len(blocks)==0 or h != blocks[-1]:
                blocks.append(h)

    cutted_blocks += len(blocks)
    return cutted_blocks