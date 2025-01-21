public class Main4 {
    public static void main(String[] args) {
        Thread4 contatore1 = new Thread4();
        Thread4 contatore2 = new Thread4();
  
        Thread thread1 = new Thread(contatore1);
        Thread thread2 = new Thread(contatore2);
  
        thread1.start();
        thread2.start();
      }
}
