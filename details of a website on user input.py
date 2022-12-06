import java.util.Scanner;



public class UserInput2 {
public boolean equals(Object obj) {
    Scanner sc=new Scanner(System.in);
    System.out.println("input:");
    String a=new String(sc.nextLine());
    String b=new String("https://ful.io");
    
    
if(a.equals(b)) {
    System.out.println("Output:\n"+"Social links-");
    System.out.println("https://www.facebook.com/fulioTech/");
    System.out.println("https://www.linkedin.com/company/ful-io/");
    System.out.println("Email/s-");
    System.out.println("support@ful.io\n"+"Contact:");
    System.out.println("+1 343 303 6668");
    
    
}



return false;



   
}
    public static void main(String[] args) {
        UserInput2 uip=new UserInput2();
        uip.equals(uip);
        
    }}