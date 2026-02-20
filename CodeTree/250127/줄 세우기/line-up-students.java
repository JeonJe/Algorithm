import java.util.*;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    Person[] persons = new Person[n];
    for (int i = 0; i < n; i++) {
      int height = sc.nextInt();
      int weight = sc.nextInt();

      persons[i] = new Person(i + 1, height, weight);
    }

    Arrays.sort(persons);

    for (Person p : persons) {
      System.out.printf("%d %d %d \n", p.height, p.weight, p.num);
    }
  }

  public static class Person implements Comparable<Person> {

    int num;
    int height;
    int weight;

    public Person(int num, int height, int weight) {
      this.num = num;
      this.height = height;
      this.weight = weight;
    }

    @Override
    public int compareTo(Person o) {
      if (this.height == o.height) {
        if (this.weight == o.weight) {
          return this.num - o.num;
        }
        return o.weight - this.weight;
      }
      return o.height - this.height;
    }

  }
}
