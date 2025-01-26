import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String id = sc.next();
        int level = sc.nextInt();
        User user1 = new User("codetree", 10);
        User user2 = new User();
        user2.id = id;
        user2.level = level;

        System.out.printf("user %s lv %d\n", user1.id, user1.level);
        System.out.printf("user %s lv %d", user2.id, user2.level);
    }

    public static class User {
        String id;
        int level;

        User() {

        }

        User(String id, int level) {
            this.id = id;
            this.level = level;
        }
    }
}