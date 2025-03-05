
import java.util.ArrayList;

public class Paziente extends Persona {
    private ArrayList<String> Patologie = new ArrayList<>();

    public Paziente(String nome, String cognome, String codicefiscale, ArrayList<String> patologie) {
        super(nome, cognome, codicefiscale);
        Patologie = patologie;
    }

    public ArrayList<String> getPatologie() {
        return Patologie;
    }

    public void setPatologie(ArrayList<String> patologie) {
        Patologie = patologie;
    }

    public void aggiungiPatologia(String Patologia) {
        Patologie.add(Patologia);
        System.out.println("Patologia aggiunta: " + Patologia);
    }

    public void RimuoviPatologia(String Patologia) {
        Patologie.remove(Patologia);
        System.out.println("\nPatologia Rimossa: " + Patologia);
    }

    public void mostraInfo() {
        System.out.println("\nNome Paziente: " + this.getNome());
        System.out.println("Cognome Paziente: " + this.getCognome());
        System.out.println("Codice Fiscale Paziente: " + this.getCodicefiscale());
        System.out.println("Patologie del Paziente: " + Patologie + "\n");
    }
    

    @Override
    public String toString() {
        return "Paziente [Patologie=" + Patologie + ", Nome:" + getNome() + ", Cognome:"
                + getCognome() + ", Codicefiscale:" + getCodicefiscale() + "]";
    }

    

}
