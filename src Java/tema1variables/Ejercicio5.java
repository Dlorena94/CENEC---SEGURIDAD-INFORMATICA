package tema1variables;

import java.util.Scanner;

public class Ejercicio5 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Introduce el primer número: ");
        int numero1 = sc.nextInt();
        
        System.out.print("Introduce el segundo número: ");
        int numero2 = sc.nextInt();
        
        int suma = numero1 + numero2;
        int resta = numero1 - numero2;
        int multiplicacion = numero1 * numero2;
       // double divi=numero1/numero2;
        double division = (double) numero1 / numero2;//castear, permite convertir una variable en otra
        
        System.out.println("La suma es: " + suma);
        System.out.println("La resta es: " + resta);
        System.out.println("La multiplicación es: " + multiplicacion);
        System.out.printf("La división es: %.2f%n", division);
       // System.out.printf("La división es: %.2f%n", divi);
        sc.close();
    }
}
