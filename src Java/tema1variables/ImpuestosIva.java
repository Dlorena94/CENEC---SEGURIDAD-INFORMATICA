package tema1variables;

import java.util.Scanner;

public class ImpuestosIva {
	public static void main(String[]args) {
		Scanner scanner = new Scanner (System.in);
		
		System.out.print("Importe:");
				double Importe = scanner.nextDouble();
				
		System.out.print("Unidades:");
		int unidades = scanner.nextInt();
		
		System.out.print("Tipo de Iva (4, 7 o 21): ");
		int tipoIva = scanner.nextInt();
		
		scanner.close();
		
		double porcentaje = 0.0;
		double cantidadIva = 0.0;
		double totalBruto = Importe * unidades;  
		double totalSinIva = totalBruto;
		double descuento = 0.0;
		
		if (tipoIva == 4) {
		    porcentaje = 0.04;
		} else if (tipoIva == 7) {
		    porcentaje = 0.07;
		} else if (tipoIva == 21) {
		    porcentaje = 0.21;
		}
	
		if (totalSinIva > 10000) {
		    descuento = totalSinIva * 0.40;
		} else if (totalSinIva > 5000) {
		    descuento = totalSinIva * 0.30;
		} else if (totalSinIva > 1000) {
		    descuento = totalSinIva * 0.20;
		} else {
		    descuento = totalSinIva * 0.10;
		}

		totalSinIva = totalSinIva - descuento;
		cantidadIva = totalSinIva * porcentaje;
		double totalPagar = totalSinIva + cantidadIva;
		
	System.out.println("\n --- TOTAL ---");
	System.out.printf("Importe Unitario: %.2f €%n ", Importe);
	System.out.printf("Unidades: %d%n", unidades);
	System.out.println("---");
	System.out.printf("Total (sin IVA): %.2f €%n", totalBruto
			);
	System.out.printf("Iva (%d%%): %.2f €%n", tipoIva, cantidadIva);
	System.out.println("---");
	System.out.printf("TOTAL A PAGAR:   %.2f €%n", totalPagar);
	
	
	}
	
	}

