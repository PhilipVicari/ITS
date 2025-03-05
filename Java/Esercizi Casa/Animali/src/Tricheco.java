public class Tricheco extends Animale_Acquatico{
    private double lunghezza;
    private String colore;
    private int eta;

    

    public Tricheco(String colore, int eta, double lunghezza, double pinne, String genere) {
        super(pinne, genere);
        this.colore = colore;
        this.eta = eta;
        this.lunghezza = lunghezza;
    }

    public Tricheco() {
    }


    public double getLunghezza() {
        return lunghezza;
    }
    public void setLunghezza(double lunghezza) {
        this.lunghezza = lunghezza;
    }
    public String getColore() {
        return colore;
    }
    public void setColore(String colore) {
        this.colore = colore;
    }
    public int geteta() {
        return eta;
    }
    public void seteta(int eta) {
        this.eta = eta;
    }

    @Override
    public String toString() {
        return "\nTricheco lunghezza = " + lunghezza + ", colore = " + colore + ", eta = " + eta;
    }
}
