import java.util.Scanner;

public class C {
    static class Node {
        int val;
        Node next;

        Node(int val) {
            this.val = val;
            this.next = null;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String S = sc.next();
        sc.close();

        // Начинаем с списка: 0
        Node head = new Node(0);

        // Для удобства будем хранить ссылки на узлы по значению i
        // чтобы быстро находить i-1
        Node[] nodes = new Node[N + 1];
        nodes[0] = head;

        for (int i = 1; i <= N; i++) {
            char c = S.charAt(i - 1);
            Node prevNode = nodes[i - 1];
            Node newNode = new Node(i);
            nodes[i] = newNode;

            // Вставляем newNode слева или справа от prevNode
            // Но в односвязном списке нет ссылки на предыдущий элемент,
            // поэтому вставка слева от prevNode - это вставка перед prevNode,
            // а справа - вставка после prevNode.

            if (c == 'R') {
                // Вставка справа от prevNode - проще: newNode.next = prevNode.next; prevNode.next = newNode;
                newNode.next = prevNode.next;
                prevNode.next = newNode;
            } else { // c == 'L'
                // Вставка слева от prevNode - нужно найти узел, который указывает на prevNode, и вставить newNode между ним и prevNode
                // Если prevNode == head, то вставляем newNode в голову
                if (prevNode == head) {
                    newNode.next = head;
                    head = newNode;
                } else {
                    // Найдем узел, у которого next == prevNode
                    Node cur = head;
                    while (cur != null && cur.next != prevNode) {
                        cur = cur.next;
                    }
                    // cur не может быть null, так как prevNode есть в списке
                    if (cur != null) {
                        cur.next = newNode;
                        newNode.next = prevNode;
                    }
                }
            }
        }

        // Выводим список
        StringBuilder sb = new StringBuilder();
        Node cur = head;
        while (cur != null) {
            sb.append(cur.val);
            cur = cur.next;
            if (cur != null) sb.append(" ");
        }
        System.out.println(sb.toString());
    }
}
