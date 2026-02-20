import java.util.*;

public class Main {
  public static void main(String[] args) {
    // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    Person[] persons = new Person[n];
    for(int i = 0; i < n; i++ ){
      String name = sc.next();
      int height = sc.nextInt();
      int weight = sc.nextInt();

      persons[i] = new Person(name, height, weight);
    }

    Arrays.sort(persons, (a, b) -> a.height - b.height);

    for(Person p : persons) {
      System.out.printf("%s %d %d\n", p.name, p.height, p.weight);
    }
  }

  public static class Person {
    String name;
    int height;
    int weight;

    public Person (String name, int height, int weight){
      this.name = name;
      this.height = height;
      this.weight = weight;
    }
  }
}
