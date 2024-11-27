
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {

    static List<Integer> deque = new ArrayList<>();
    static int result = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine());

        int n = Integer.parseInt(st.nextToken());
        for (int i = 1; i < n + 1; i++) {
            deque.add(i);
        }

        int m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(reader.readLine());

        for (int i = 0; i < m; i++) {
            int targetNum = Integer.parseInt(st.nextToken());
            findMinimumDistance(targetNum);
        }

        System.out.println(result);

    }

    private static void findMinimumDistance(int targetNum) {
        int targetNumIndex = deque.indexOf(targetNum);
        int rolateLeft = targetNumIndex;
        int roateRight = deque.size() - targetNumIndex;

        if (rolateLeft <= roateRight) {
            while (rolateLeft > 0) {
                Integer front = deque.remove(0);
                deque.add(front);
                rolateLeft--;
                result++;
            }
            deque.remove(0);
            return;
        }
        while (roateRight > 0) {
            Integer back = deque.remove(deque.size() - 1);
            deque.add(0, back);
            roateRight--;
            result++;
        }
        deque.remove(0);
    }
}