def main(s):
    ans=0
    odd=0
    while odd<len(s):
        if s[odd] in "13579":
            ans+=1
        odd+=1
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return ans
print(main("123445"))