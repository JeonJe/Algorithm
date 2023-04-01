import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        br.readLine();
        int sum = 0;

        String nums = br.readLine();
        char[] charArray = nums.toCharArray();
        for (char c : charArray) {
            sum += Character.getNumericValue(c);
        }
        System.out.println(sum);

    }

}
