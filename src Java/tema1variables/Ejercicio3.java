package tema1variables;

public class Ejercicio3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String nombre, apellidos;
		double iva, calculoIva, total;
		int importe;
		nombre="Alberto";
		apellidos="Ruiz";
		importe=100;
		iva=0.21;
		calculoIva=importe*iva;
		total=importe+calculoIva;
		System.out.println(" Bienvenido "+ nombre+ " "+apellidos);
		System.out.println(" importe es "+ importe);
		System.out.println(" total iva es "+ calculoIva);
		System.out.println(" El total ticket es "+ total);
	}

}