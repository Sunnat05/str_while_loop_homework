def main(s):
    int=0
    ans=0
    while int<len(s):
        if s[int] in "qwrtyplkjhgfdszxcvbnm":
           ans+=1
        int+=1
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