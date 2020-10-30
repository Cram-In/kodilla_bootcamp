def palindrome(txt):
    #case sensivity
    txt = txt.lower()
    # remove all spaces from the string. (in case if string have spaces)
    txt = txt.replace(" ", "")
    # remove special characters
    txt = "".join(l for l in txt if l.isalnum())
    # checking if string is a palindrome through slicing
    return txt == txt[::-1]

palindrome("kajak")
palindrome("kajak")
palindrome("abba")
palindrome("Are we not drawn onward, we few, drawn onward to new era?")
#knock knock
palindrome("tattarrattat")
