package tema1variables;

import java.util.Scanner;

public class EjercicioCondicional {
	public static void main(String[]args) {
		Scanner sc = new Scanner(System.in);
		int edad;
		
		System.out.println("Dime tu Edad");
		edad= sc.nextInt();
		
		if (edad < 18) {
			System.out.println("menor de eadad");
		} else if (edad>=67) {
			System.out.println("Trabajador activo");	
		}
		else {
			System.out.println("Puede trabajar si quiere");
		}
	sc.close();
	}
	

}
