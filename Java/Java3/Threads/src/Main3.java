public class Main3 {
    public static void main(String[] args) {
      Thread3 contatore1 = new Thread3();
      Thread3 contatore2 = new Thread3();

      Thread thread1 = new Thread(contatore1);
      Thread thread2 = new Thread(contatore2);

      thread1.start();
      thread2.start();
	}
}
