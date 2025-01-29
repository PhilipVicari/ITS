

public class Thread5_1 implements Runnable{
    private int parametro;

    public Thread5_1(int parametro) {
        this.parametro = parametro;
    }

    
    public int getParametro() {
        return parametro;
    }
    
    public void setParametro(int parametro) {
        this.parametro = parametro;
    }
    @Override
    public void run() {
        if (parametro >= 90){
            for (int i = 100; i < 90; i--) {
                System.out.println(i);
            }
        }
    }

    
}
