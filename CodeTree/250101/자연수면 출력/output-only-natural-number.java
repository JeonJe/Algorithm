import java.util.*;


public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
  
        int a = sc.nextInt();
        int b = sc.nextInt();

        if(a <= 0) {
            System.out.print("0");
        } else {
            for(int i =0; i < b; i++) {
                System.out.printf("%d", a);
            }
        }



    }
}