def main(s):
    ans=0
    odd=0
    while odd<len(s):
        if s[odd] in "13579":
            ans+=int(s[odd])
        odd+=1
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return ans
print(main("12342"))
