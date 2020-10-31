import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    List<Object> Array = new ArrayList<Object>();

    int[] arr = new int[10];

    for (int i = 0; i < arr.length; i++) {
      arr[i] = sc.nextInt() % 42;
    }

    for (int i = 0; i < arr.length; i++) {
      for (int j = i + 1; j < arr.length; j++) {
        if (arr[i] == arr[j]) {
          Array.add(arr[i]);
          break;
        }
      }
    }

    System.out.println(10 - Array.size());
    sc.close();
  }
}
