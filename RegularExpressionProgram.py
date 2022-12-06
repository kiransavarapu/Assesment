package regularexpression;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class RegularExpression {
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      System.out.println("Enter your name: ");
      String name = sc.nextLine();
      System.out.println("Enter your Phone number: ");
      String phone = sc.next();
     
      String regex ="^(\\+\\d{1,2}\\s?)?1?\\-?\\.?\\s?\\(?\\d{3}\\)?[\\s.-]?\\d{3}[\\s.-]?\\d{4}$";
     
      Pattern pattern = Pattern.compile(regex);
      
      Matcher matcher = pattern.matcher(phone);
      
      if(matcher.matches()) {
         System.out.println("Given phone number is valid");
      } else { 
         System.out.println("Given phone number is not valid");
      }
   }
}