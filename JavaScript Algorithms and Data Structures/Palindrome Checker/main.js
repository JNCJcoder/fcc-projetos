function palindrome(str)
{
    const stringArray = str.match(/[a-z0-9]/ig);

    const string = stringArray.join("").toLowerCase();

    const reversedString = stringArray.reverse().join("").toLowerCase();

    if(string === reversedString)
    {
        return true;
    }

    return false;
}

palindrome("eye");