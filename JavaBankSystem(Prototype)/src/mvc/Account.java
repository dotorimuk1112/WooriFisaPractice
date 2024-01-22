package mvc;

import java.util.Random;
import java.util.Scanner;

public class Account {
	String name;
	int age;
	String job;
	String purpose;
	double income;
	String accountNum;
	int passwd;
	int balance = 0;

	Account() {
		this.accountNum = generateRandomNumber();
		Scanner sc = new Scanner(System.in);
		System.out.print("이름: ");
		this.name = sc.next();
		System.out.print("나이: ");
		this.age = sc.nextInt();
		System.out.print("직업: ");
		this.job = sc.next();
		System.out.print("계좌 개설 목적: ");
		this.purpose = sc.next();
		System.out.print("수입: ");
		this.income = sc.nextDouble();
		System.out.println("계좌 비밀번호: ");
		this.passwd = sc.nextInt();
	}

	private String generateRandomNumber() {
		Random random = new Random();
		StringBuilder randomNumber = new StringBuilder();

		for (int i = 0; i < 13; i++) {
			int digit = random.nextInt(10); // 0에서 9 사이의 난수 생성
			randomNumber.append(digit);
		}
		return randomNumber.toString();
	}
}