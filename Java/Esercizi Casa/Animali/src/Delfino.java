public class Delfino extends Animale_Acquatico{
    private int età;             // Età del delfino in anni
    private double lunghezza;    // Lunghezza del delfino in metri
    private double peso;
    
    
    public Delfino() {
    }


    public Delfino(double pinne, String genere, int età, double lunghezza, double peso) {
        super(pinne, genere);
        this.età = età;
        this.lunghezza = lunghezza;
        this.peso = peso;
    }


    public int getEtà() {
        return età;
    }


    public void setEtà(int età) {
        this.età = età;
    }


    public double getLunghezza() {
        return lunghezza;
    }


    public void setLunghezza(double lunghezza) {
        this.lunghezza = lunghezza;
    }


    public double getPeso() {
        return peso;
    }


    public void setPeso(double peso) {
        this.peso = peso;
    }


    @Override
    public String toString() {
        return "\nDelfino età = " + età + ", lunghezza = " + lunghezza + ", peso = " + peso;
    }
    
}
