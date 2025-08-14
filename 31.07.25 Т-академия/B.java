import java.util.Scanner;

public class B {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        sc.close();

        int n = s.length();

        // prefixA[i] = количество 'a' в s[0..i-1]
        int[] prefixA = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefixA[i + 1] = prefixA[i] + (s.charAt(i) == 'a' ? 1 : 0);
        }

        // suffixC[i] = количество 'c' в s[i..n-1]
        int[] suffixC = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            suffixC[i] = suffixC[i + 1] + (s.charAt(i) == 'c' ? 1 : 0);
        }

        long result = 0;
        for (int j = 0; j < n; j++) {
            if (s.charAt(j) == 'b') {
                // количество 'a' слева от j = prefixA[j]
                // количество 'c' справа от j = suffixC[j + 1]
                result += (long) prefixA[j] * suffixC[j + 1];
            }
        }

        System.out.println(result);
    }
}
