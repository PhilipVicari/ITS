public class Coccodrillo extends Animale_Terrestre{
    private double peso;
    private double velocità;
    private double potenza_Morso;

    public Coccodrillo(double zampe, String genere, double peso, double velocità, double potenza_Morso) {
        super(zampe, genere);
        this.peso = peso;
        this.velocità = velocità;
        this.potenza_Morso = potenza_Morso;
    }

    public Coccodrillo(double zampe, String genere) {
        super(zampe, genere);
    }
    public double getPeso() {
        return peso;
    }
    public void setPeso(double peso) {
        this.peso = peso;
    }
    public double getVelocità() {
        return velocità;
    }
    public void setVelocità(double velocità) {
        this.velocità = velocità;
    }
    public double getPotenza_Morso() {
        return potenza_Morso;
    }
    public void setPotenza_Morso(double potenza_Morso) {
        this.potenza_Morso = potenza_Morso;
    }

    @Override
    public String toString() {
        return "\nCoccodrillo peso = " + peso + ", velocità = " + velocità + ", potenza_Morso = " + potenza_Morso
                + ", Verso = " + Verso();
    }

    @Override
    public String Verso() {
        return "Non c'è nessuno che lo sa";
    }

}