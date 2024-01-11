import java.util.Scanner;

public class HanoiTower {

    public static void hanoi(int n, int source, int auxiliary, int target) {
        if (n > 0) {
            hanoi(n - 1, source, target, auxiliary);
            System.out.println("Move disk " + n + " from " + source + " to " + target);
            hanoi(n - 1, auxiliary, source, target);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите количество дисков: ");
        int disks = scanner.nextInt();

        hanoi(disks, 1, 2, 3);

        scanner.close();
    }
}
