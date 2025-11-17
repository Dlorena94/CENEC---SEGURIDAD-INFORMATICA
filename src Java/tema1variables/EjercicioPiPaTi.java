
package tema1variables;
import java.util.Scanner;
import java.util.Random;

public class EjercicioPiPaTi {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Random random = new Random();
		int opcion;

		System.out.println("!Bienvenido al juego!");
		
		while (true) {
			System.out.println("\nIndica la opción: 1. Jugar, 2. Salir");
			
			opcion = sc.nextInt();
			
			if (opcion == 2) {
	        		System.out.println("Has elegido salir");
	        		break; 
	        	} else if (opcion == 1){
	        		System.out.println("Has elegido jugar");
	        		
	        		int jugadaMaquina = random.nextInt(3) + 1;
	        		
	     System.out.println("\nElige tu opcion de juego: ");
	     System.out.println("1. Piedra");
	     System.out.println("2. Papel");
	     System.out.println("3. Tijera");
	     System.out.print("Tu eleccion (1, 2, o 3): ");
	     
	     int jugadaUsuario = sc.nextInt();
	     
	     if (jugadaUsuario < 1 || jugadaUsuario > 3) {
	    	 continue; 
	     }

	     String[] opciones = {"Piedra", "Papel", "Tijera"}; 
	        		
	     System.out.println("\n=================================");
         System.out.println("Tu jugada: " + opciones[jugadaUsuario - 1]);
         System.out.println("Máquina: " + opciones[jugadaMaquina - 1]);
         System.out.println("---------------------------------");

         if (jugadaUsuario == jugadaMaquina) {
             System.out.println("¡Es un Empate!");
         } 
        
         else if ((jugadaUsuario == 1 && jugadaMaquina == 3) || 
                  (jugadaUsuario == 2 && jugadaMaquina == 1) || 
                  (jugadaUsuario == 3 && jugadaMaquina == 2)) { 
             System.out.println("¡Felicidades! ¡Has Ganado! ");
         } 

         else {
             System.out.println("¡Lo siento! La Máquina Gana. ");
         }
         System.out.println("=================================");
     } 
	}
	
	sc.close();	
}

	        	
		}

	
	        	
	

