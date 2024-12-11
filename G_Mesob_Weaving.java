
public class G_Mesob_Weaving {
    static int weave(int n) {
        return n % 7;
    }
    public static void main(String[] args) {
        int  strings = 126;
        System.out.println(weave(strings)); //Output - 0
    }
}

