public class Persona {
    private String nome;
    private String Cognome;
    private String Codicefiscale;
    public Persona(String nome, String cognome, String codicefiscale) {
        this.nome = nome;
        Cognome = cognome;
        Codicefiscale = codicefiscale;
    }
    @Override
    public String toString() {
        return "Persona [nome=" + nome + ", Cognome=" + Cognome + ", Codicefiscale=" + Codicefiscale + ", toString()="
                + super.toString() + "]";
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getCognome() {
        return Cognome;
    }
    public void setCognome(String cognome) {
        Cognome = cognome;
    }
    public String getCodicefiscale() {
        return Codicefiscale;
    }
    public void setCodicefiscale(String codicefiscale) {
        Codicefiscale = codicefiscale;
    }

    
}
