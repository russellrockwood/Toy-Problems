// Input: integer over 9
// Output: single digit

function persistence(num) {
    num = num.toString().split('')
    var digitArray = num.map(Number);
  
    if (digitArray.length === 1) {
      return digitArray[0];
    } else {
      return persistence(digitArray.reduce((a, b) => a*b, 1));
    }
  }
  
  persistence(4)
  
   //persistence(39) === 3 // because 3*9 = 27, 2*7 = 14, 1*4=4
                          // and 4 has only one digit