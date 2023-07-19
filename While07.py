def main(s):
    int=0
    ans=0
    while int<len(s):
        if s[int] in "24680":
            ans+=1
        int+=1
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return ans
print(main("12345345676545"))