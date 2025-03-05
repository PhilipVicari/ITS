
import static java.lang.Thread.sleep;

public class Thread4_1 implements Runnable{

    @Override
    public void run() {
        int durata = 1000;
        for (int i = 0; i <= 5; i++) {
            try {
                System.out.println(i);
                sleep(durata);
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }        
        }
    }

    
}
