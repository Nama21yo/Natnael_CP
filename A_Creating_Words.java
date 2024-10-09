import java.util.Scanner;

public class A_Creating_Words {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt(); // Number of test cases
        scanner.nextLine(); // Move to the next line after reading integer
        for (int i = 0; i < t; i++) {
            String line = scanner.nextLine(); // Read the whole line
            String[] parts = line.split(" "); // Split the line into two strings a and b
            String a = parts[0];
            String b = parts[1];
            // Swap the first characters of a and b
            String newA = b.charAt(0) + a.substring(1);
            String newB = a.charAt(0) + b.substring(1);

            // Output the result
            System.out.println(newA + " " + newB);
        }
        scanner.close(); // Close the scanner
    }
}