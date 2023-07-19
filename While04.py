def main(s):
    int=0
    ans=0
    while int<len(s):
        if s[int] in "QWERTYUIOPLKJHGFDSAZXCVBNM":
            ans+=1
        int+=1
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return ans
print(main("sadFD224f"))