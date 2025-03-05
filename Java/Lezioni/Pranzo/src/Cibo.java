class Cibo {
    private String nome;
    private double calorie;
    private double prezzo;
    private String tipo;

    // Costruttore aggiornato con controllo del tipo
    public Cibo(String nome, String tipo, double prezzo, double calorie) {
        this.nome = nome;
        this.calorie = calorie;
        this.prezzo = prezzo;

        // Controllo del tipo, ammettiamo solo "Primo", "Secondo" o "Dolce"
        if (tipo.equals("Primo") || tipo.equals("Secondo") || tipo.equals("Dolce")) {
            this.tipo = tipo;
        }
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getCalorie() {
        return calorie;
    }

    public void setCalorie(double calorie) {
        this.calorie = calorie;
    }

    public double getPrezzo() {
        return prezzo;
    }

    public void setPrezzo(double prezzo) {
        this.prezzo = prezzo;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    @Override
    public String toString() {
        return nome + " (" + tipo + ", " + calorie + " kcal, " + prezzo + " €)";
    }
}
