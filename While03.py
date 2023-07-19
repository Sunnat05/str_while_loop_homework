def main(s):
    ind=0
    ans=0
    while ind<len(s):
        if not s[ind] in "1234567890poiuytrewqasdfghjklmnbvcxz":
            ans+=1
        ind+=1
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return ans
print(main("++trt!@#$"))