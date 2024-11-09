
class Biglietteria {
    private Compagnia AirItalia;
    private Compagnia RayaPain;

    public Biglietteria(Compagnia AirItalia, Compagnia RayaPain) {
        this.AirItalia = AirItalia;
        this.RayaPain = RayaPain;
    }

    public boolean prenotaPosto(Compagnia compagnia, int indiceAereo, int numeroPosto) {
        Aereo aereo = compagnia.getAereo(indiceAereo);
        if (aereo != null) {
            return aereo.prenotaPosto(numeroPosto);
        }
        return false;
    }
}