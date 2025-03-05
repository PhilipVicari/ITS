public class TestAutoveicolo {
    public static void main(String[] args) throws Exception {
        Autoveicolo Auto1 = new Autoveicolo(1500, 15.0, 50.0, "Rosso", 13000.0);
        Autoveicolo Auto2 = new Autoveicolo(2000, 20.0, 60.0, "Giallo", 35000.0);
        Autoveicolo Auto3 = new Autoveicolo(3500, 30.0, 70.0, "Nero", 100000.0);
        Autoveicolo Auto4 = new Autoveicolo(4000, 40.0, 90.0, "Blu", 180000.0);
        Autoveicolo Auto5 = new Autoveicolo(500, 5.0, 25.0, "Verde", 5000.0);
        
        /*Calcolo Km */
        
        double Autonomia = Auto1.CalcolaAutonomia(70.0, 191.0);
        System.out.println("\nIl risultato è: \n" + Autonomia + " KM");
        double Autonomia2 = Auto2.CalcolaAutonomia(92.0, 191.0);
        System.out.println("Il risultato è: \n" + Autonomia2 + " KM");
        double Autonomia3 = Auto3.CalcolaAutonomia(33.0, 191.0);
        System.out.println("Il risultato è: \n" + Autonomia3 + " KM");
        double Autonomia4 = Auto4.CalcolaAutonomia(65.0, 191.0);
        System.out.println("Il risultato è: \n" + Autonomia4 + " KM");
        double Autonomia5 = Auto5.CalcolaAutonomia(220.0, 191.0);
        System.out.println("Il risultato è: \n" + Autonomia5 + " KM");
    }
}
