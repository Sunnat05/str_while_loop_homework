def main(s):
    ind=0
    ans=0
    while ind<len(s):
        if s[ind] in "1234567890":
            ans+=1
        ind+=1        
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return ans
print(main('rtrddxbe3434466ydd'))