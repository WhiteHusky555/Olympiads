import java.util.*;

public class E {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int q = scanner.nextInt();

        // Инициализация графа
        List<Integer>[] graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        // Построение графа на основе фактов
        for (int i = 0; i < q; i++) {
            int l = scanner.nextInt();
            int r = scanner.nextInt();
            int u = l - 1;
            int v = r;
            graph[u].add(v);
            graph[v].add(u);
        }

        // BFS для поиска кратчайшего пути
        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);
        Queue<Integer> queue = new LinkedList<>();
        dist[0] = 0;
        queue.add(0);

        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v : graph[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    queue.add(v);
                }
            }
        }

        // Проверка достижимости вершины N
        if (dist[n] == -1) {
            System.out.println("No");
        } else {
            System.out.println("Yes");
            System.out.println(dist[n]);
        }
    }
}