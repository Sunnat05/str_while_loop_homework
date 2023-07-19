def main(s):
    ind=0
    ans=0
    while ind<len(s):
        if s[ind] in "qwertyuioplkjhgfdsazxcvbnm":
            ans+=1
        ind+=1 
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return ans
print(main("ffee3rdjad3333334333"))