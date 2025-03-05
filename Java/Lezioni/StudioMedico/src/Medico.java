public class Medico extends Persona{
    private String Specializzazione;

    public Medico(String nome, String cognome, String codicefiscale, String specializzazione) {
        super(nome, cognome, codicefiscale);
        Specializzazione = specializzazione;
    }

    public String getSpecializzazione() {
        return Specializzazione;
    }

    public void setSpecializzazione(String specializzazione) {
        Specializzazione = specializzazione;
    }
    

    public void MostraInfoMedico() {
        System.out.println("\nNome Medico: " + this.getNome());
        System.out.println("Cognome Medico: " + this.getCognome());
        System.out.println("Codice Fiscale Medico: " + this.getCodicefiscale());
        System.out.println("Specializzazione del Medico: " + Specializzazione + "\n");
    }

    @Override
    public String toString() {
        return "Medico [Specializzazione=" + Specializzazione + ", getNome()=" + getNome() + ", getCognome()="
                + getCognome() + ", getCodicefiscale()=" + getCodicefiscale() + "]";
    }
                          
    }

    

    
