public class G_Decipher {
    public static String decipher(String encoded) {
        String[] enc = encoded.trim().split(" ");
        StringBuilder decipheredText = new StringBuilder();
        
        for (String binaryString : enc) {
            int decimalValue = Integer.parseInt(binaryString, 2);
            decipheredText.append((char) decimalValue);
        }
        
        return decipheredText.toString();
    }

    public static void main(String[] args) {       
        String encoded = " 01001011 01101110 01101111 01110111 01101100 01100101 01100100 01100111 01100101 00100000 01101001 01110011 00100000 01110011 01110101 01110010 01110110 01101001 01110110 01100001 01101100 00101110 00100000 01001010 01101111 01101001 01101110 00100000 01000111 01000100 01000111 ";
        System.out.println(decipher(encoded)); // Output: Knowledge is survival. Join GDG
    }
}
