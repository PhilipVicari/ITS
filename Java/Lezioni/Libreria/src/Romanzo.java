class Romanzo extends Libro {
    private String genere;

    // Costruttore
    public Romanzo(String titolo, String autore, String genere) {
        super(titolo, autore);
        this.genere = genere;
    }

    // Sovrascrittura del metodo descrivi
    @Override
    public String descrivi() {
        return super.descrivi() + ", Genere: " + genere;
    }
}