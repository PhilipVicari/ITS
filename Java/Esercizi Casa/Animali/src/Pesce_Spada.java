public class Pesce_Spada extends Animale_Acquatico{
    private int età;              // Età del pesce spada in anni
    private double lunghezza;
    private double lunghezza_becco;     // Lunghezza del pesce spada in metri
    private double peso;          // Peso del pesce spada in chilogrammi
    private String colore;
    public Pesce_Spada(double pinne, String genere, int età, double lunghezza, double lunghezza_becco, double peso,
            String colore) {
        super(pinne, genere);
        this.età = età;
        this.lunghezza = lunghezza;
        this.lunghezza_becco = lunghezza_becco;
        this.peso = peso;
        this.colore = colore;
    }
    public Pesce_Spada() {
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
    public double getLunghezza_becco() {
        return lunghezza_becco;
    }
    public void setLunghezza_becco(double lunghezza_becco) {
        this.lunghezza_becco = lunghezza_becco;
    }
    public double getPeso() {
        return peso;
    }
    public void setPeso(double peso) {
        this.peso = peso;
    }
    public String getColore() {
        return colore;
    }
    public void setColore(String colore) {
        this.colore = colore;
    }
    @Override
    public String toString() {
        return "\nPesce_Spada età = " + età + ", lunghezza = " + lunghezza + ", lunghezza_becco = " + lunghezza_becco
                + ", peso = " + peso + ", colore = " + colore;
    }
    
    
}
