import java.util.*;

public class Repetitions {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println(countRepetition(str));
        sc.close();
    }

    private static int countRepetition(String str) {
        int n = str.length();
        int maxCount = 0;
        int r;

        for (int l = 0; l < n; l = r) {
            r = l;

            while (r < n && str.charAt(l) == str.charAt(r)) {
                r++;
            }
            maxCount = Math.max(maxCount, r - l);
        }

        return maxCount;
    }
}
