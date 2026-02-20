import java.util.*;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    Person[] persons = new Person[n];
    for (int i = 0; i < n; i++) {
      String name = sc.next();
      int korean = sc.nextInt();
      int english = sc.nextInt();
      int math = sc.nextInt();

      persons[i] = new Person(name, korean, english, math);
    }

    Arrays.sort(persons);

    for (Person p : persons) {
      System.out.printf("%s %d %d %d\n", p.name, p.korean, p.english, p.math);
    }
  }

  public static class Person implements Comparable<Person> {

    String name;
    int korean;
    int english;
    int math;

    public Person(String name, int korean, int height, int weight) {
      this.name = name;
      this.korean = korean;
      this.english = height;
      this.math = weight;
    }

    @Override
    public int compareTo(Person o) {
      if (this.korean == o.korean) {
        if (this.english == o.english) {
          return o.math - this.math;
        }
        return o.english - this.english;
      }
      return o.korean - this.korean;

    }
  }
}
