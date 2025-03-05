public class Main {
    
// 2) Gestione dei Conti Correnti
//-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
// Crea una superclasse ContoCorrente con i seguenti attributi:

// numeroConto (int)
// saldo (double)

// Metodi:
// deposita(double importo): aggiunge l'importo al saldo.
// preleva(double importo): sottrae l'importo dal saldo solo se il saldo è sufficiente. In caso contrario, stampa un messaggio d'errore.
// mostraSaldo(): stampa il numero del conto e il saldo attuale.
//-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// Crea una classe derivata ContoCorrenteRisparmio che estende ContoCorrente.

// Aggiungi un attributo tassoInteresse (double) per rappresentare il tasso di interesse annuo.
// Aggiungi un metodo applicaInteressi() che aggiunge gli interessi al saldo, calcolati con la formula: saldo += saldo * tassoInteresse / 100.
//-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// Crea una classe Banca che gestisce i conti correnti.

// All'interno della classe Banca, crea un array di ContoCorrente per contenere fino a 10 conti correnti.
// Aggiungi un metodo aggiungiConto(ContoCorrente conto) per aggiungere un nuovo conto all'array.
// Aggiungi un metodo mostraTuttiISaldi() per scorrere l'array e mostrare il saldo di tutti i conti correnti.
//-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
// Nel metodo main:

// Crea un'istanza della classe Banca.
// Crea alcuni ContoCorrente e ContoCorrenteRisparmio, imposta i loro saldi e aggiungili all'array della banca.
// Chiama mostraTuttiISaldi() per visualizzare i saldi di tutti i conti.
    public static void main(String[] args) throws Exception {
        Banca banca = new Banca();

        ContoCorrente conto1 = new ContoCorrente(1, 50);
        ContoCorrente conto2 = new ContoCorrente(2, 70);
        ContoCorrente conto3 = new ContoCorrente(3, 43);

        ContoCorrenteRisparmio contoR = new ContoCorrenteRisparmio(14, 50, 3);
        banca.aggiungiConto(conto1);
        banca.aggiungiConto(conto2);
        banca.aggiungiConto(conto3);
        banca.aggiungiConto(contoR);

        conto1.Preleva(5);
        banca.MostraTuttiSaldi();
    }

}
