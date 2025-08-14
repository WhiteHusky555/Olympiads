import java.util.*;

public class D {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int k = scanner.nextInt();

        int[] a = new int[n + 1]; // 1-indexed
        for (int i = 1; i <= n; i++) {
            a[i] = scanner.nextInt();
        }

        // dp[i][j] = максимальное настроение на i-й ступеньке, используя j абстракций
        long[][] dp = new long[n + 1][k + 1];

        // Инициализация
        for (int i = 0; i <= n; i++) {
            Arrays.fill(dp[i], Long.MIN_VALUE / 2);
        }

        // Начальное состояние
        Arrays.fill(dp[0], 0);

        // Для оптимизации абстракций - храним максимум для каждого количества использованных абстракций
        long[] maxPrev = new long[k + 1];

        for (int i = 1; i <= n; i++) {
            // Обновляем максимумы с предыдущих позиций
            for (int j = 0; j <= k; j++) {
                maxPrev[j] = Math.max(maxPrev[j], dp[i-1][j]);
            }

            for (int j = 0; j <= k; j++) {
                // Обычный шаг
                if (dp[i-1][j] != Long.MIN_VALUE / 2) {
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j] + a[i]);
                }

                // Прыжок через ступеньку
                if (i >= 2 && dp[i-2][j] != Long.MIN_VALUE / 2) {
                    dp[i][j] = Math.max(dp[i][j], dp[i-2][j] + a[i]);
                }

                // Абстракция
                if (j > 0 && maxPrev[j-1] != Long.MIN_VALUE / 2) {
                    dp[i][j] = Math.max(dp[i][j], maxPrev[j-1] + a[i]);
                }
            }
        }

        // Результат
        long result = Long.MIN_VALUE;
        for (int j = 0; j <= k; j++) {
            result = Math.max(result, dp[n][j]);
        }

        System.out.println(result);
        scanner.close();
    }
}
