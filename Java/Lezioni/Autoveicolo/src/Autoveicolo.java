public class Autoveicolo {
    double cilindrata;
    double consumo;
    double serbatoio;
    String colore;
    double prezzo;
    
    public Autoveicolo(int cilindrata, double consumo, double serbatoio, 
                       String colore, double prezzo) {
        this.cilindrata = cilindrata;
        this.consumo = consumo;
        this.serbatoio = serbatoio;
        this.colore = colore;
        this.prezzo = prezzo;
    }
    public double getCilindrata() {
        return cilindrata;
    }
    public void setCilindrata(double cilindrata) {
        this.cilindrata = cilindrata;
    }
    public double getConsumo() {
        return consumo;
    }
    public void setConsumo(double consumo) {
        this.consumo = consumo;
    }
    public double getSerbatoio() {
        return serbatoio;
    }
    public void setSerbatoio(double serbatoio) {
        this.serbatoio = serbatoio;
    }
    public String getColore() {
        return colore;
    }
    public void setColore(String colore) {
        this.colore = colore;
    }
    public double getPrezzo() {
        return prezzo;
    }
    public void setPrezzo(double prezzo) {
        this.prezzo = prezzo;
    }
    public double CalcolaAutonomia(double Velocita_Media, double N){
        double tempo_ore = N / 60;
        return Velocita_Media * tempo_ore;
    }
}
