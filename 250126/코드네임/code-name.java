import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        Person[] persons = new Person[5];
        for(int i = 0; i < 5; i++) {
            String codeName = sc.next();
            int score = sc.nextInt();
            persons[i] = new Person(codeName, score);
        }

        Arrays.sort(persons, new Comparator<Person>() {
            public int compare(Person a, Person b) {
                return Integer.compare(a.score, b.score);
            }
        });
                System.out.printf("%s %d", persons[0].codeName, persons[0].score);


    }

    public static class Person {
        int score;
        String codeName;

        Person() {

        }

        Person(String codeName, int score) {
            this.codeName = codeName;
            this.score = score;
        }
    }
}