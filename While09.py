def main(s):
    ans=0
    num=0
    while num<len(s):
        if s[num] in "0987654321":
            ans+=int(s[num])
        num+=1
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return ans
print(main("334"))