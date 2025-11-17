package tema1variables;
import java.util.Scanner;
public class Ejercicio9 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner=new Scanner(System.in);
		System.out.print("Que pelicula de star war te gusta ");
		String peli= scanner.nextLine();
		System.out.print("Cuantas peliculas has visto ");
		byte cuantas= Byte.parseByte(scanner.nextLine());
		System.out.print("Te gustaria ver alguna mas ");
		boolean gustar=Boolean.parseBoolean(scanner.nextLine());
		System.out.print("tus respuestas "+peli+" "+cuantas+" "+gustar);
		
		
	}

}
