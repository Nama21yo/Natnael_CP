import java.util.Scanner;

public class A_Catch_the_Coin {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        for (int i = 0; i < n; i++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();

            // Check if Monocarp can reach before the coin falls
            if (y < -1) {
                System.out.println("NO");
            } else {
                System.out.println("YES");
            }
        }

        scanner.close();
    }
}
