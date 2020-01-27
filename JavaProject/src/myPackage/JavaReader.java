package myPackage;
import java.io.*;


public class JavaReader {  
  
    public static void main(String[] args) {  
    	 try {
    		 Reader rd = new FileReader("C:\\Users\\ABHAY\\eclipse-workspace\\JavaProject\\output.txt");
    		 int data = rd.read();
    		 while(data!=-1) {
    			 System.out.print((char)data);
    			 data = rd.read();
    		 }
    		 rd.close();
    	 }catch(Exception ex) {
    		 System.out.println(ex.getMessage());
    	 }
    		  
    }  
}  