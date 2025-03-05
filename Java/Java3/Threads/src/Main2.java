public class Main2 {
    public static void main(String[] args) {
		
		Thread2 Runnable = new Thread2();

		Thread t2 = new Thread(Runnable);
		t2.start();

        System.out.println("Thread principale: " + Thread.currentThread().getName());
	}
}
