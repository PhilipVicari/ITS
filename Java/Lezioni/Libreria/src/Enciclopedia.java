public class Enciclopedia extends Libro{
    
    private String NumeroVolumi;

    public Enciclopedia(String titolo, String autore, String NumeroVolumi) {
        super(titolo, autore);
        this.NumeroVolumi = NumeroVolumi;
    }
    
    @Override
    public String descrivi() {
        return NumeroVolumi;
    }
}
