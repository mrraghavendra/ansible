import java.util.Arrays;
import java.util.Scanner;

public class HelloWorld {

    // Method 1: Greet a user using input from Scanner
    public void greetUser() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        System.out.print("Enter your name 123: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");
    }

    // Method 2: Add two integers and return the result
    public int addNumbers(int a, int b) {
        return a + b;
    }

    // Method 3: Check if a number is even
    public boolean isEven(int number) {
        return number % 2 == 0;
    }

    // # Copilot start
    public void printSortedArray1234(String[] items) {
        Arrays.sort(items);
        System.out.println("Sorted items:");
        for (String item : items) {
            System.out.println(item);
            System.out.println(item123);
        }
    }
     // # Copilot end

    // Method 4: Sort and print an array of strings
    public void printSortedArray(String[] items) {
        Arrays.sort(items);
        System.out.println("Sorted items:");
        for (String item : items) {
            System.out.println(item);
        }
    }

    public static void main(String[] args) {
        SampleClass obj = new SampleClass();
        obj.greetUser();
        int sum = obj.addNumbers(12, 8);
        System.out.println("Sum: " + sum);
        System.out.println("Is 15 even? " + obj.isEven(15));
        String[] countries = {"India", "USA", "Germany", "Brazil"};
        obj.printSortedArray(countries);
    }
}
