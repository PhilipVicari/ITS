public class ContoCorrenteRisparmio extends ContoCorrente{
    private double tassoInteresse;

    public ContoCorrenteRisparmio(int numeroConto, double saldo, double tassoInteresse) {
        super(numeroConto, saldo);
        this.tassoInteresse = tassoInteresse;
    }

    public double ApplicaInteressi(){
        double nuovoSaldo = getSaldo() + getSaldo() * tassoInteresse / 100;
        return nuovoSaldo;
    }

}
