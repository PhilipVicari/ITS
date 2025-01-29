public class Main5 {
    public static void main(String[] args) {
        Thread5 contatore1 = new Thread5(4);
        Thread5_1 contatore2 = new Thread5_1(3);
  
        Thread thread1 = new Thread(contatore1);
        Thread thread2 = new Thread(contatore2);
  
        thread2.start();
    }
}
