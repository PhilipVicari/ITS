
public class Animale_Terrestre extends Animale{
    private double zampe;
    private String genere;


    @Override
    public String Verso() {
        return null;
    }
    public Animale_Terrestre(double zampe, String genere) {
        super();
        this.zampe = zampe;
        this.genere = genere;
    }
    public double getZampe() {
        return zampe;
    }
    public void setZampe(double zampe) {
        this.zampe = zampe;
    }
    public String getGenere() {
        return genere;
    }
    public void setGenere(String genere) {
        this.genere = genere;
    }
    @Override
    public String toString() {
        return "\nAnimale_Terrestre: zampe = " + zampe + ", genere = " + genere + ", Verso = " + Verso();
    }

    public static Animale Crea_Animale() {
            return null;
    }
}