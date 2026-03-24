import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        //학급 인원 추가
        Map<Integer, List<String>> students = new HashMap<>();


        while (true) {
            st = new StringTokenizer(br.readLine());
            int classNum = Integer.parseInt(st.nextToken());
            String studentName = st.nextToken();

            if (classNum == 0) {
                break;
            }

            //학급 번호에 추가
            students.putIfAbsent(classNum, new ArrayList<>());
            List<String> studentList = students.get(classNum);
            if (studentList.size() < m) {
                studentList.add(studentName);
            }
        }

        for (Integer i : students.keySet()) {
            if (i % 2 != 0) {
                List<String> studentList = students.get(i);
                studentList.sort(Comparator.comparingInt(String::length).thenComparing(String::compareTo));
                for (String s : studentList) {
                    System.out.printf("%d %s\n", i, s);
                }
            }
        }

        for (Integer i : students.keySet()) {
            if (i % 2 == 0) {
                List<String> studentList = students.get(i);
                studentList.sort(Comparator.comparingInt(String::length).thenComparing(String::compareTo));
                for (String s : studentList) {
                    System.out.printf("%d %s\n", i, s);
                }
            }
        }
    }


}