public class Thread5 implements Runnable{
    private int parametro;

    public Thread5(int parametro) {
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
        if (parametro < 10){
            for (int i = 1; i <= 10; i++){
                System.out.println(i);
            }
        }
    }

}
