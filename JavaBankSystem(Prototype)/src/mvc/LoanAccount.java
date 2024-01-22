package mvc;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class LoanAccount extends DwAccount {
    static double loanBalance;
    LoanProduct loanProduct;
    LocalDate repayDate;

    ArrayList<String> LoanAccountDbList = Dblog.DbList;

    public LoanAccount() {
        this.repayDate = LocalDate.now().plusYears(1);
        // 대출 상품 선택
        LoanProduct selectedProduct = setAdditionalInfo();

        // 선택된 대출 상품에 따라 대출 잔액 설정
        while (selectedProduct == null) {
            System.out.println("다시 대출 상품을 선택해주세요.");
            selectedProduct = setAdditionalInfo();
        }

        if (selectedProduct == LoanProduct.청년전세대출) {
            loanBalance = 100000000.0; // 예시로 10,000으로 설정
            this.loanProduct = selectedProduct;
        } else if (selectedProduct == LoanProduct.주부긴급대출) {
            loanBalance = 3000000.0; // 예시로 20,000으로 설정
            this.loanProduct = selectedProduct;
        } else if (selectedProduct == LoanProduct.직장인비상금대출) {
            loanBalance = 5000000.0; // 예시로 30,000으로 설정
            this.loanProduct = selectedProduct;
        }

        LoanAccountDbList.add(String.format("%s에 %s님이 계좌를 개설하셨습니다.", LocalDate.now(), name));
        Dblog.saveArrayListToFile(LoanAccountDbList, "src/banksystem/LoanAccountLog.txt");
    }

    public LoanProduct setAdditionalInfo() {
        System.out.println("받으시려는 대출 상품을 선택해주세요");
        System.out.println("1. 청년전세대출(24세~36세만 가능)");
        System.out.println("2. 주부대출(직업이 주부인 고객만 가능)");
        System.out.println("3. 직장인비상금대출(연 소득 4000만원 이상만 가능)");
        Scanner scanner = new Scanner(System.in);

        // 입력이 있는지 확인
        while (!scanner.hasNextLine()) {
            System.out.println("잘못 입력하셨습니다. 없는 상품이거나 대출 가능 대상이 아닙니다.");
            scanner.next(); // 입력이 없을 경우 버퍼를 비워줌
        }

        String selectedProduct = scanner.nextLine();

        // 문자열을 LoanProduct Enum 상수로 변환
        switch (selectedProduct) {
            case "1":
                if (isAgeInRange(24, 36)) {
                    return LoanProduct.청년전세대출;
                } else {
                    System.out.println("나이가 24세~36세가 아닙니다.");
                }
                break;
            case "2":
                if (job.equals("주부")) {
                    return LoanProduct.주부긴급대출;
                } else {
                    System.out.println("직업이 주부가 아닙니다.");
                }
                break;
            case "3":
                if (income >= 40000000) {
                    return LoanProduct.직장인비상금대출;
                } else {
                    System.out.println("연 소득이 4000만 원 이상이 아닙니다.");
                }
                break;
            default:
                System.out.println("올바르지 않은 대출 상품 선택");
        }

        return null;
    }

    // getter
    public double getLoanBalance() {
        return loanBalance;
    }

    public void LoanAccountInfo() {
        // 비밀번호 확인
        System.out.println("비밀번호 네 자리를 입력하세요.");
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        if (input == passwd) {
            System.out.println("고객명: " + name);
            System.out.println("나이: " + age);
            System.out.println("직업: " + job);
            System.out.println("개설 목적: " + purpose);
            System.out.println("수입: " + income);
            System.out.println("계좌번호: " + accountNum);
            System.out.println("대출 상품명: " + loanProduct);
            System.out.println("대출 잔액: " + loanBalance);
            System.out.println("대출 상환일자: " + repayDate);
        } else {
            System.out.println("비밀번호가 틀립니다.");
            LoanAccountDbList.add(String.format("%s에 %s님이 %s계좌의 비밀번호를 틀렸습니다.", LocalDate.now(), name, accountNum));
            Dblog.saveArrayListToFile(LoanAccountDbList, "src/banksystem/LoanAccountLog.txt");
        }
        // Dblog.add(LocalDate.now()+",
        // "+LocalTime.now().format(DateTimeFormatter.ofPattern("HH:mm:ss"))+
        // "에 "+this.name+"고객님이 고객님의 계좌에서 "+
        // this.remittanceBill+"원 을 송금하셨습니다.");
        // 실행
        LoanAccountDbList.add(String.format("%s에 %s님이 계좌 정보를 확인했습니다..", LocalDate.now(), name));
        Dblog.saveArrayListToFile(LoanAccountDbList, "src/banksystem/LoanAccountLog.txt");
    }

    private boolean isAgeInRange(int minAge, int maxAge) {
        return age >= minAge && age <= maxAge;
    }

    public void run() {
        Scanner scanner = new Scanner(System.in);
        int userInput;

        while (true) {
            System.out.println("원하시는 업무를 선택하세요");
            System.out.println("1. 대출 잔액 확인 / 2. 대출 상환");

            if (scanner.hasNextInt()) {
                userInput = scanner.nextInt();

                if (userInput == 1) {
                    System.out.println(name + "님의 대출 잔액은 " + loanBalance + "원입니다.");
                } else if (userInput == 2) {
                    // 대출 상환 로직을 추가할 수 있습니다.
                } else {
                    System.out.println("1 또는 2가 아닌 값을 입력했습니다. 다시 시도하세요.");
                    scanner.nextLine();
                    continue;
                }

                // 스캐너를 닫지 않고 반복을 빠져나갑니다.
                break;
            } else {
                System.out.println("1 혹은 2를 입력하세요.");
                scanner.next(); // 잘못된 입력을 버립니다.
            }
        }

        // 반복이 끝나면 사용이 끝날 때 스캐너를 닫아줍니다.
        scanner.close();
    }

    public void repayment() {
        // HashMap 생성
        Map<String, String> repaymentAccountMap = new HashMap<>();

        // 계좌 정보 추가
        repaymentAccountMap.put("123456789", "password1");
        repaymentAccountMap.put("987654321", "password2");

        // 변수 입력
        Scanner scanner = new Scanner(System.in);
        System.out.println("계좌번호를 입력하세요:");
        String enteredAccountNum = scanner.nextLine();

        System.out.println("비밀번호를 입력하세요:");
        String enteredPassword = scanner.nextLine();

        // 입력된 값이 HashMap에 저장된 값과 일치하는지 확인
        if (repaymentAccountMap.containsKey(enteredAccountNum) &&
                repaymentAccountMap.get(enteredAccountNum).equals(enteredPassword)) {
            System.out.println("정상적으로 실행됩니다.");
            // 여기에 실행하고자 하는 코드를 추가하세요.
        } else {
            System.out.println("계좌번호 또는 비밀번호가 일치하지 않습니다.");
        }
    }

    // Enum
    public enum LoanProduct {
        청년전세대출,
        주부긴급대출,
        직장인비상금대출
    }
}

// 로그 기록 경우의 수
// 1. 계좌 개설시
// 2. 계좌 조회시
// 3. 비밀번호 틀렸을 때