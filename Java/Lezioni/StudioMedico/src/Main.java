import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws Exception {
        /*
         * 3) Gestione di uno Studio Medico
         * 
Crea una superclasse Persona con attributi di base:
nome (String)
cognome (String)
codiceFiscale (String)

Crea una classe derivata Paziente che estende Persona.
Aggiungi un attributo patologie (lista di stringhe) per memorizzare le patologie del paziente.
Aggiungi metodi per aggiungere e rimuovere patologie dalla lista.
Aggiungi un metodo mostraInfo() che visualizzi le informazioni del paziente e le patologie.

Crea una classe derivata Medico che estende Persona.
Aggiungi un attributo specializzazione (String).
Aggiungi un metodo mostraInfo() che visualizzi le informazioni del medico e la sua specializzazione.

Crea una classe StudioMedico per gestire pazienti e medici.

Crea due liste: una lista di Paziente e una lista di Medico.
Aggiungi metodi aggiungiPaziente(Paziente p) e aggiungiMedico(Medico m) per aggiungere pazienti e medici alle rispettive liste.
Aggiungi un metodo mostraTuttiIPazienti() per visualizzare le informazioni di tutti i pazienti.
Aggiungi un metodo mostraTuttiIMedici() per visualizzare le informazioni di tutti i medici.

Nel metodo main:
Crea un'istanza della classe StudioMedico.
Crea alcuni Paziente e Medico, imposta i loro attributi e aggiungili alle liste dello studio medico.
Chiama i metodi per visualizzare tutte le informazioni sui pazienti e i medici.
         */
        StudioMedico studio1 = new StudioMedico(new ArrayList<>(), new ArrayList<>());

        Paziente p1 = new Paziente("Andrea", "Rossi", "Mammeta", new ArrayList<>());
        p1.aggiungiPatologia("IperTensione");
        Paziente p2 = new Paziente("Mario", "Rossi", "coiwc", new ArrayList<>());
        p2.aggiungiPatologia("Ischemia");
        Paziente p3 = new Paziente("Valentino", "Rossi", "ovwqac", new ArrayList<>());
        p3.aggiungiPatologia("Infarto");
        Medico m1 = new Medico("Franco", "Baresi", "ForzaMilan", "Cardiologia");
        Medico m2 = new Medico("Irene", "Petrucci", "meiwocf", "Neurologia");
        Medico m3 = new Medico("Riccardo", "fioravanti", "Dbwqaicwla", "Cardiologia");

        studio1.aggiungiMedico(m1);
        studio1.aggiungiMedico(m2);
        studio1.aggiungiMedico(m3);

        studio1.aggiungiPaziente(p1);
        studio1.aggiungiPaziente(p2);
        studio1.aggiungiPaziente(p3);

        m1.MostraInfoMedico();
        System.out.println("\n");
        m2.MostraInfoMedico();
        System.out.println("\n");
        m3.MostraInfoMedico();
        System.out.println("\n");


        p1.mostraInfo();
        p2.mostraInfo();
        p3.mostraInfo();

    }
}
