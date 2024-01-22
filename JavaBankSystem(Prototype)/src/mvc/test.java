package mvc;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        // HashMap 생성
        Map<String, String> accountMap = new HashMap<>();

        // 계좌 정보 추가
        accountMap.put("123456789", "password1");
        accountMap.put("987654321", "password2");

        // 변수 입력
        Scanner scanner = new Scanner(System.in);
        System.out.println("계좌번호를 입력하세요:");
        String enteredAccountNum = scanner.nextLine();

        System.out.println("비밀번호를 입력하세요:");
        String enteredPassword = scanner.nextLine();

        // 입력된 값이 HashMap에 저장된 값과 일치하는지 확인
        if (accountMap.containsKey(enteredAccountNum) && 
        		accountMap.get(enteredAccountNum).equals(enteredPassword)) {
            System.out.println("정상적으로 실행됩니다.");
            // 여기에 실행하고자 하는 코드를 추가하세요.
        } else {
            System.out.println("계좌번호 또는 비밀번호가 일치하지 않습니다.");
        }

        // 스캐너 닫기
        scanner.close();
    }
}
