
public class G_Coin_Change {
    static int coinChange(int[] coins, int amount){
        int[] memo = new int[amount + 1];
        memo[0] = 1; //for 0 amount you have 1 choice - not using any coin
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                memo[i] += memo[i - coin];
            }
        }        
        return memo[amount];
    }
    public static void main(String[] args) {
        int[] coins = {5, 15, 25, 30, 50, 55 ,75};
        System.out.println(coinChange(coins, 105));
       
    }
}

