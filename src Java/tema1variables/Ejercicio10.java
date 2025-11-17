package tema1variables;

import java.util.Scanner;

public class Ejercicio10 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.print("Que personaje de Lord of the rings te gusta ");
		String personaje=sc.nextLine();
		System.out.print("El mago malo se llamaba ");
		String malo=sc.nextLine();
		System.out.print("Que edad ten�a Frodo... ");
		byte edad= Byte.parseByte(sc.nextLine());
		System.out.print("Cuantos orcos formaba el ejercicio de Sauron");
		int orcos= Integer.parseInt(sc.nextLine());
	}

}
