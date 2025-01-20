public class Leone extends Animale_Terrestre{
    private double peso;
    private double velocità;

    public Leone(double zampe, String genere) {
        super(zampe, genere);
    }

    public Leone(double zampe, String genere, double peso, double velocità) {
        super(zampe, genere);
        this.peso = peso;
        this.velocità = velocità;
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

    @Override
    public String toString() {
        return "\nLeone peso = " + peso + ", velocità = " + velocità + ", Verso = " + Verso();
    }

    @Override
    public String Verso() {
        return "Roar";
    }
}