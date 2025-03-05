// 1) Libreria e Libri
// Crea una superclasse Libro con attributi come titolo e autore.
// Aggiungi un metodo descrivi() che restituisca una descrizione del libro.
// Crea una classe derivata Romanzo che estende Libro.
// Aggiungi l'attributo genere (es. "Fantasy", "Giallo").
// Sovrascrivi il metodo descrivi() per includere il genere nella descrizione.
// Crea un'altra classe derivata Enciclopedia con un attributo numeroVolumi.
// Testa le classi creando vari oggetti e chiamando il metodo descrivi().
public class Main {
    public static void main(String[] args) {
        Romanzo romanzo = new Romanzo("Il Signore degli Anelli", "J.R.R. Tolkien", "Fantasy");
        Enciclopedia enciclopedia = new Enciclopedia("Enciclopedia Treccani", "AA.VV.", "12");

        System.out.println("\n" + romanzo.descrivi());
        System.out.println("\n" + enciclopedia.descrivi());
    }
}