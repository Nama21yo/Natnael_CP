import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A_Zhan_s_Blender {
    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        try {
            int t = Integer.parseInt(reader.readLine()); // Number of test cases
            StringBuilder result = new StringBuilder();

            for (int i = 0; i < t; i++) {
                long n = Long.parseLong(reader.readLine()); // Number of fruits
                String[] inputs = reader.readLine().split(" ");
                long x = Long.parseLong(inputs[0]); // Blender capacity
                long y = Long.parseLong(inputs[1]); // Input rate

                // If there are no fruits, print 0
                if (n == 0) {
                    result.append(0).append("\n");
                    continue;
                }

                // Calculate minimum time needed
                long minTime = (n + y - 1) / y; // Time to fill the blender
                long blendedTime = (n + x - 1) / x; // Time to blend all fruits

                // Append the maximum of the two times to the result
                result.append(Math.max(minTime, blendedTime)).append("\n");
            }

            // Output all results
            System.out.print(result);
        } catch (IOException e) {
            e.printStackTrace(); // Handle IO exceptions
        }
    }
}
