public class Gallina extends Animale_Terrestre{
    private double peso;
    private double velocità;

    public Gallina(double zampe, String genere, double peso, double velocità) {
        super(zampe, genere);
        this.peso = peso;
        this.velocità = velocità;
    }

    public Gallina(double zampe, String genere) {
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

    @Override
    public String toString() {
        return "\nGallina: peso = " + peso + ", velocità = " + velocità + ", Verso = " + Verso();
    }

    @Override
    public String Verso() {
        return "coccode";
    }

}