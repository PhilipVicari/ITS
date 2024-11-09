
class Aereo {
    private boolean[] posti;

    public Aereo(int numeroPosti) {
        posti = new boolean[numeroPosti];
    }

    public boolean prenotaPosto(int numeroPosto) {
        if (numeroPosto < 0 || numeroPosto >= posti.length) {
            System.out.println("Numero di posto non valido");
            return false;
        }
        if (!posti[numeroPosto]) {
            posti[numeroPosto] = true;
            System.out.println("Posto " + numeroPosto + " prenotato.");
            return true;
        } else {
            System.out.println("Posto " + numeroPosto + " già occupato.");
            return false;
        }
    }

    public int getNumeroPosti() {
        return posti.length;
    }

    public boolean isPostoDisponibile(int numeroPosto) {
        return !posti[numeroPosto];
    }
}