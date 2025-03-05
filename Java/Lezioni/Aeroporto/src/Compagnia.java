import java.util.ArrayList;
class Compagnia {
    private String nome;
    private ArrayList<Aereo> aerei;

    public Compagnia(String nome) {
        this.nome = nome;
        aerei = new ArrayList<>();
    }

    public void aggiungiAereo(int numeroPosti) {
        Aereo nuovoAereo = new Aereo(numeroPosti);
        aerei.add(nuovoAereo);
        System.out.println("Aereo con " + numeroPosti + " posti aggiunto alla compagnia " + nome);
    }

    public Aereo getAereo(int indice) {
        if (indice >= 0 && indice < aerei.size()) {
            return aerei.get(indice);
        } else {
            System.out.println("Aereo non esistente.");
            return null;
        }
    }
}