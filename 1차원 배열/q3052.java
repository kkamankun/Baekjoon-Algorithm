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

# 다른 풀이
import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<Integer> count = new HashSet<Integer>();

        for(int i = 0; i < 10; i++){
           count.add(Integer.parseInt(br.readLine()) % 42);
        }
        System.out.println(count.size());
    }
}
