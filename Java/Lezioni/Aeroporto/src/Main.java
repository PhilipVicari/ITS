import java.util.ArrayList;
import java.util.LinkedList;
 
public class Main {
    
    public static void main(String[] args) {
        //Ho definito una variabile che si chiama li 
        //ed è una LinkedList di numeri interi
        LinkedList<Integer> li = new LinkedList<Integer>();
        
        li.add(7);
        li.add(9);
        li.add(2);
        for (var i: li) {
        System.out.println(i);
        }
        ArrayList<Boolean> lai = new ArrayList<Boolean>();
    /*
         * * Definire una classe Aereo con numero di posti fisso (vettore di booleani)
            * Definire una classe Compagnia che gestisce N aerei, con N dinamico nel senso che non si conosce a priori ma ogni tanto viene aggiunto un nuovo aereo
            * Definire una classe Biglietteria che gestisce due Compagnie e che consente di prenotare i posti su un aereo
            * Nel main
            * 1) creare due compagnie
            * 2) aggiungere le due compagnie alla agenzia
            * 3) aggiungere qualche aereo a ogni compagnia
            * 4) realizzare un menu per prenotare posto su un aereo
            * 5) Stampare per ogni compagnia e per ogni aereo i posti prenotati e il numero di posto ancora disponibili
         */
        
         // 1) Creare due compagnie
                Compagnia RayaPain = new Compagnia("RayaPain");
                Compagnia AirItalia = new Compagnia("AirItalia");
        
                // 2) Aggiungere aerei alle compagnie
                RayaPain.aggiungiAereo(100); // Aggiunge un aereo con 100 posti a RayaPain
                AirItalia.aggiungiAereo(150); // Aggiunge un aereo con 150 posti a AirItalia
        
                // 3) Creare la biglietteria che gestisce le due compagnie
                Biglietteria biglietteria = new Biglietteria(RayaPain, AirItalia);
        
                // 4) Prenotare alcuni posti
                biglietteria.prenotaPosto(RayaPain, 0, 10); // Prenota il posto 10 sul primo aereo della RayaPain
                biglietteria.prenotaPosto(AirItalia, 0, 20); // Prenota il posto 20 sul primo aereo della AirItalia
            }
        }