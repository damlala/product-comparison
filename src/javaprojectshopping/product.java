package javaprojectshopping;
import java.util.Scanner;

public class product {

	public static void main(String[] args) {
	Scanner damla = new Scanner(System.in);
    System.out.println("Please enter the amount of first product");
	int amount1 = damla.nextInt();
	System.out.println("Please enter the price of first product");
	double price1 = damla.nextDouble();
	double product1 = price1*amount1;
	System.out.println("First product's total is:"+ product1);
	System.out.println("Please enter the amount of second product");
	int amount2 = damla.nextInt();
	System.out.println("Please enter the price od second product");
	double price2 =damla.nextDouble();
	double product2 = price2*amount2;
	System.out.println("Second product's total is:"+product2);
	if (product1<product2) {
		System.out.println("Second product is more expensive than first product");
	}
			else
		System.out.println("First product is more expensive than second product");
	}
	
	
	}

