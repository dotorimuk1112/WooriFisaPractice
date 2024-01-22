package mvc;

import java.util.Scanner;

public class main {
	public static void main(String[] args) {
		DwAccount 최현규 = new DwAccount();
		DwAccount 최현규2 = new DwAccount();

		최현규.deposit();
		최현규2.deposit();

		최현규.balanceCheck();
		최현규2.balanceCheck();

		최현규.withDraw();
		최현규2.withDraw();

		최현규.balanceCheck();
		최현규2.balanceCheck();

		최현규.remittance(최현규2);

		최현규.balanceCheck();
		최현규2.balanceCheck();

	}

}