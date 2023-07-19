def main(s):
    let=0
    ans=0
    while let<len(s):
        if s[let] in "qwrtyplkjhgfdszxcvbnm":
            ans+=1
        let+=1
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