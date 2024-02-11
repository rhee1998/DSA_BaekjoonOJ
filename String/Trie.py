# ================== #
# Trie = Prefix Tree #
# ================== #

import sys
from collections import deque

def StringToDeque(x):
    # ==================================================
    # Input(s)
    # - x : string object
    #
    # Output(s)
    # - deque of characters from string
    # ==================================================
    return deque([ch for ch in x])

def GenerateTrie(x):
    # ==================================================
    # Input(s)
    # - x : deque object. If string, should be converted with StringToDeque(x)
    #
    # Output(s)
    # - returns initialized trie object
    # - ex) 'hello' -> {'h':{'e':{'l':{'l':{'o':{}}}}}}
    # ==================================================
    if len(x) == 0: return {}
    return {x.popleft(): GenerateTrie(x)}

def AddElement(trie, x):
    # ==================================================
    # Input(s)
    # - trie : base trie object
    # - x    : deque object which is added to given trie
    #
    # Output(s)
    # - trie : modified trie object
    # ==================================================
    if len(x) == 0: return trie
    
    ch = x.popleft()
    try: trie[ch] = AddElement(trie[ch], x)
    except: trie[ch] = GenerateTrie(x)

    return trie
