package mvc;


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;

public class Dblog {
        // DB용 ArrayList 이름 DbList 생성
		
        public static ArrayList<String> DbList = new ArrayList<>();
        
        // ArrayList에 내용 추가 (*조심 : 메인 들어가 있음)
        public static void main(String[] args) {
	        	// 예제삽입 -> 둘의 str받아와야함
        		DbList.add("2024-01-12, 15:51:14에 1고객님이 고객님의 계좌에서 1000원 을 입금하셨습니다.");
	            DbList.add("Jane Smith");
	            
	    // ArrayList를 .txt 파일 변경함수 실행   
	            saveArrayListToFile(DbList, "src/banksystem/Dblist.txt");
        // 
	            loadArrayListFromFile("src/banksystem/Dblist.txt");
//	            String a = (String) "j" + "qwe\n";
//	            a.getBytes(); 준규가 말한 string을 겟바이트 하기
        } 
        
        // ArrayList(DbList) -> txt 저장하는 함수 
//        public static void saveArrayListToFile(ArrayList<String> arrayList, String fileName) {
//            try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName, StandardCharsets.UTF_8, true))) {
//                // ArrayList의 각 요소를 파일에 쓰기
//                for (String data : arrayList) {
//                    writer.write(data);
//                    writer.newLine();  // 각 데이터를 새로운 줄에 쓰기
//                }
//
//                System.out.println("데이터가 파일에 성공적으로 추가되었습니다.");
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//        }
        
        public static void saveArrayListToFile(ArrayList<String> arrayList, String fileName) {
            try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName, StandardCharsets.UTF_8, true))) {
                // ArrayList의 각 요소를 파일에 쓰기
                for (String data : arrayList) {
                    writer.write(data);
                    writer.newLine();  // 각 데이터를 새로운 줄에 쓰기
                }

                System.out.println("데이터가 파일에 성공적으로 추가되었습니다.");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        
        
        //txt -> ArrayList(loadedDataList) 넘긴 후 출력하는 함수  
        public static ArrayList<String> loadArrayListFromFile(String fileName) {
            ArrayList<String> loadedDataList = new ArrayList<>();

            try (BufferedReader reader = new BufferedReader(new FileReader(fileName, StandardCharsets.UTF_8))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    loadedDataList.add(line);
                }

                System.out.println("파일에서 데이터를 성공적으로 읽었습니다.");
                
                for (String data : loadedDataList) {
                    System.out.println(data);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }

            return loadedDataList;
        }
        public void run() {
        	
        }
    }