import java.util.*;

public class Main {
    static ArrayList<Integer> list = new ArrayList<>();
    static int k;
    static int n;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        k = scanner.nextInt();
        n = scanner.nextInt();

        choose(0 );
    }

    public static void choose( int currentNum) {
        if(currentNum == n) {
            printArr();
            return;
        }

        for(int i = 1; i <= k; i++) {
            list.add(i);
            choose(currentNum + 1);
            list.remove(list.size()-1);
        }

    }

    private static void printArr() {
        for (Integer integer : list) {
            System.out.print(integer + " ");
        }
        System.out.println();
    }
}