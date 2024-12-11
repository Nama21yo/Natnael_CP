public class G_To_Main_Foldetr {
    static int min_operations(String[] logs) {
        int min_operations = 0;
        for (String file : logs) {
            if(file == "../") min_operations--;
            else if (file == "./") continue;
            else min_operations++;
        }
        return min_operations;
    }
    public static void main(String[] args) {
        String[] logs = {"d1/", "d2/", "../", "d21/", "./", "d22/", "../", "../", "../","d1/", "d3/", "d4/", "./", "../", "d5/", "./", "../", "d6/","../", "../", "d7/", "d8/", "d9/", "d10/", "../", "../", "d11/","./", "d12/", "d13/", "d14/", "../", "../", "d15/", "../", "d16/","../", "d17/", "d18/", "../", "d19/", "d20/", "./", "../", "../","d21/", "d22/", "d23/", "../", "d24/", "../", "../", "../", "../","d25/", "d26/", "../", "../", "../"};
        System.out.println(min_operations(logs)); //Output - 4
    }
}
