function rot13(str)
{
    const stringArray = str.toUpperCase().split("");
  
    const result = stringArray.map(item => {
        let charNumber = item.charCodeAt(0);
  
        if(charNumber > 77 && charNumber < 91)
        {
            charNumber -= 13;
        }
        else if(charNumber > 64 && charNumber < 78) 
        {
            charNumber += 13;
        }
        else
        {
            return item;
        }
  
        return String.fromCharCode(charNumber);
    }).join("");
  
    return result;
}
  
rot13("SERR PBQR PNZC");