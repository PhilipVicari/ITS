import java.util.ArrayList;

public class Banca {
    private ArrayList<ContoCorrente> contiCorrenti = new ArrayList<>();

    public void aggiungiConto(ContoCorrente conto) {
        contiCorrenti.add(conto);
        System.out.println("Conto aggiunto: " + conto);
    }

    public void MostraTuttiSaldi(){
        for (ContoCorrente conto : contiCorrenti) {
            System.out.println("Numero Conto: " + conto.getNumeroConto() + ", Saldo: " + conto.getSaldo());
        }
    }
}
