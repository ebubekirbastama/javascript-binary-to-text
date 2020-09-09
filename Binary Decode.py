let EBSbinary = `01000101 01000010 01010011 00100000 01010011 01100101 01101100 01100001 01101101 01101100 01100001 01110010 00100000 `;

let outputStr = EBSbinary.split(' ') 
   .map(bin => String.fromCharCode(parseInt(bin, 2))) 
   .join(''); 

alert(outputStr);
