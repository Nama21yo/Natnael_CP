
public class G_Nim_Game {
    // You will always start first don't forget that
    static boolean winGame(int n) {
        return n % 4 != 0;
    }
    public static void main(String[] args) {
        int stones = 57;
        System.out.println(winGame(stones)); //Ouput - True
    }
}

