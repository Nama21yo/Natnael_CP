import java.util.Scanner;

public class Weird_Algorithm {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        // Continue looping until n becomes 1
        while (n > 1) {
            System.out.printf("%d ", n); // Print the current value of n

            // Apply the weird algorithm rules
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = (n * 3) + 1;
            }
        }

        // Print the last value, which will be 1
        System.out.printf("%d", n);

        scanner.close();
    }
}
