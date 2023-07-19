def main(s):
    con=0
    ans=0
    while con<len(s):
        if s[con] in "qwrtyplkjhgfdszxcvbnmQWRTYPLKJHGFDSZXCVBNM":
           ans+=1
        con+=1
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    return ans
print(main("gghg34fgfae"))