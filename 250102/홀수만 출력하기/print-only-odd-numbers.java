import java.util.*; 

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for(int i = 0; i < n; i++) {
            int target = sc.nextInt();
            if(target % 2 != 0 && target % 3 == 0) {
                System.out.println(target);
            }
        }
    }       
}