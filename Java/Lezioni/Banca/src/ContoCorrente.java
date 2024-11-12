public class ContoCorrente {
    private int NumeroConto;
    private double Saldo;
    //Getter & Setter

    public int getNumeroConto() {
        return NumeroConto;
    }

    public void setNumeroConto(int numeroConto) {
        NumeroConto = numeroConto;
    }

    public double getSaldo() {
        return Saldo;
    }

    public void setSaldo(double saldo) {
        Saldo = saldo;
    }
    //Costruttore
    
    public ContoCorrente(int numeroConto, double saldo) {
        this.NumeroConto = numeroConto;
        this.Saldo = saldo;
    }
    //Metodi
    
    public double Deposita(double importo){
        Saldo = Saldo + importo;
        return Saldo;
    }
    
    public double Preleva(double importo){
        if (Saldo > importo){
            Saldo = Saldo - importo;
            return Saldo;
        } else{
            System.out.println("Saldo non Sufficiente");
            return 0;
        }
    }
    public double MostraSaldo(){
        System.out.println(NumeroConto);
        System.out.println(Saldo);
        return 0;

    }
}
