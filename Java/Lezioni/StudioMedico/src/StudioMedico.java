
import java.util.ArrayList;

public class StudioMedico {
    private ArrayList<Paziente> Pazienti = new ArrayList<>();
    private ArrayList<Medico> Medici = new ArrayList<>();
    public StudioMedico(ArrayList<Paziente> pazienti, ArrayList<Medico> medici) {
        Pazienti = pazienti;
        Medici = medici;
    }

    
    public ArrayList<Paziente> getPazienti() {
        return Pazienti;
    }
    public void setPazienti(ArrayList<Paziente> pazienti) {
        Pazienti = pazienti;
    }
    public ArrayList<Medico> getMedici() {
        return Medici;
    }
    public void setMedici(ArrayList<Medico> medici) {
        Medici = medici;
    }
    
    public void aggiungiPaziente(Paziente p) {
        Pazienti.add(p);
        System.out.println("Paziente aggiunto: " + p);
    }

    public void aggiungiMedico(Medico m) {
        Medici.add(m);
        System.out.println("Medico aggiunto: " + m);
    }

    public void mostraTuttiIPazienti(){
        System.out.println("I Pazienti sono: " + Pazienti);
    }

    public void mostraTuttiIMedici(){
        System.out.println("I Medici sono: " + Medici);
    }


    @Override
    public String toString() {
        return "StudioMedico [Pazienti=" + Pazienti + ", Medici=" + Medici + "]";
    }

    
}
