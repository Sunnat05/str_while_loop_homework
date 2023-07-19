def main(s):
    ans=0
    int=0
    while int<len(s):
        if s[int] in "qwertyuioplkjhgfdsazxcvbnmQWRTYPLKJHGFDSZXCVBNM":
            ans+=1
        int+=1
    
        """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return ans
print(main("dfdasd13e"))