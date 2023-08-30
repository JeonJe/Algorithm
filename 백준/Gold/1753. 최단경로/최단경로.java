import java.util.*;
import java.io.*;

class Node {
  int weight;
  int to;

  public Node(int weight, int to) {
    this.weight = weight;
    this.to = to;
  }
}

public class Main {
  static int V, E, START;
  static ArrayList<ArrayList<Node>> list;
  static int[] distance;
  public static void main(String[] args) throws Exception {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(reader.readLine());
    V = Integer.parseInt(st.nextToken());
    E = Integer.parseInt(st.nextToken());
    START = Integer.parseInt(reader.readLine());
    list = new ArrayList<>();
    

    for (int i = 0; i < V+1; i++){
      ArrayList<Node> row = new ArrayList<>();
      list.add(row);
    }
    for (int i = 0; i < E; i++){
      st = new StringTokenizer(reader.readLine());
      int fr = Integer.parseInt(st.nextToken());
      int to = Integer.parseInt(st.nextToken());
      int weight = Integer.parseInt(st.nextToken());
      list.get(fr).add(new Node(weight,to));
    }

    distance = new int[V+1];
    Arrays.fill(distance,Integer.MAX_VALUE);
    
    dijk();

    for (int i = 1; i < distance.length; i++) {
      System.out.println(distance[i] != Integer.MAX_VALUE ? distance[i] : "INF");
    }
  }

  static void dijk() {
    distance[START] = 0;
    PriorityQueue<Node> pq = new PriorityQueue<>( (o1, o2) -> o1.weight - o2.weight);
    pq.offer(new Node(0,START ));

    while (!pq.isEmpty()) {
      Node current = pq.poll();

      if ( distance[current.to] < current.weight ){
        continue;
      }

      for (Node adj : list.get(current.to)) {
        int newDist = current.weight + adj.weight;

        if (newDist < distance[adj.to]) {
          distance[adj.to] = newDist;
          pq.offer(new Node(newDist, adj.to));
        }

      }

    }
  }
}
