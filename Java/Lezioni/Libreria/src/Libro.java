public class Libro {
    private String Titolo;
    private String Autore;
    
    public String getTitolo() {
        return Titolo;
    }
    public void setTitolo(String titolo) {
        Titolo = titolo;
    }
    public String getAutore() {
        return Autore;
    }
    public void setAutore(String autore) {
        Autore = autore;
    }
    public Libro(String titolo, String autore) {
        this.Titolo = titolo;
        this.Autore = autore;
    }
    // Metodo descrivi
    public String descrivi() {
        return "Titolo: " + Titolo + ", Autore: " + Autore;
    }
}
