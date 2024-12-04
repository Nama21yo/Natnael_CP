

public class G_Grid_paths {
    static int distinctPaths(int m, int n) {  
        // Combination of row +  col - 2 with row - 1, where is the minimum
        int row = Math.min(m, n);  
        int col = Math.max(m, n);  
        
        long res = factorial(row + col - 2);  
        long den = factorial(row - 1);  
        long r = factorial(col - 1);  
        
        long combination = res / (den * r);  
        
        return (int) combination; 
    }  
    
    static long factorial(int num) {  
        long answer = 1;  
        for (int i = 1; i <= num; i++) {  
            answer = answer * i; 
        }  
        return answer;  
    }  
    public static void main(String[] args) {
        int row = 10;
        int col = 10;
        System.out.println(distinctPaths(row, col));  // Output: 48620       
    }
}
