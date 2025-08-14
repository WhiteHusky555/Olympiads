import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.close();

        if (n >= 8) {
            // Если n >= 8, просто вычитаем 7
            System.out.println(n - 7);
            return;
        }

        // Проверяем длину месяца, чтобы определить результат
        int monthLen = 28;
        if (!daysOnMonth(n, m, 28)) {
            if (daysOnMonth(n, m, 29)) {
                monthLen = 29;
            } else if (daysOnMonth(n, m, 30)) {
                monthLen = 30;
            } else {
                monthLen = 31;
            }
        }

        System.out.println(n - 7 + monthLen);
    }

    private static boolean daysOnMonth(int n, int m, int days) {
        if (m > days) {
            return false;
        }
        return (n + days - m) == 14;
    }
}

