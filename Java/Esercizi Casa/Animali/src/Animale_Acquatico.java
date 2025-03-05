public class Animale_Acquatico extends Animale{
    private double pinne;
    private String genere;



    @Override
    public String toString() {
        return "\nAnimale_Acquatico: pinne = " + pinne + ", genere = " + genere + ", Verso = " + Verso();
    }

    public double getPinne() {
        return pinne;
    }

    public void setPinne(double pinne) {
        this.pinne = pinne;
    }

    public String getGenere() {
        return genere;
    }

    public void setGenere(String genere) {
        this.genere = genere;
    }

    public Animale_Acquatico() {
        super();
    }

    public Animale_Acquatico(double pinne, String genere) {
        super();
        this.pinne = pinne;
        this.genere = genere;
    }

    @Override
    public String Verso() {
        return null;
    }

}