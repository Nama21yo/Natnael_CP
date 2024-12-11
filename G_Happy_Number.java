class Solution {
    static int findSum(int n) {
        int sum = 0;
        while(n > 0) {
            sum += (n % 10) * (n % 10);
            n = n /  10;
        }
        return sum;
    }
    static boolean isHappy(int n) {
        //! Floyd's tortoise and hare algorithm 
        int slow = n;
        int fast = findSum(n);
        while(fast != 1 && slow != fast) {
            slow = findSum(slow);
            fast = findSum(findSum(fast));
        }
        return fast == 1;
    }
    public static void main(String[] args) {
        int happy = 1337;
        System.out.println(isHappy(happy)); // Output- True [Happy Number]
    }
}