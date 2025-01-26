import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String c = sc.next();
        String p = sc.next();
        int t = sc.nextInt();
        C myC = new C(c,p,t);

        System.out.printf("secret code : %s\n", myC.secretCode);
        System.out.printf("meeting point : %s\n", myC.place);
        System.out.printf("time : %d\n", myC.time);
    }

    public static class C  {
        String secretCode;
        String place;
        int time;

        C (String secretCode, String place, int time) {
            this.secretCode = secretCode;
            this.place = place;
            this.time = time;
        }
    }
}