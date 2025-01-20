import java.util.LinkedList;
public class Main {

    public static void main(String[] args) {
        
      /*

            * Progetto 2
            * Sia data la classe astratta Animale che espone il metodo astratto String Verso();
            * Si realizzino le sottoclassi:
            * -AnimaleTerrestre, 
              -AnimaleAcquatico 
              con gli attributi zampe (per animale terrestre), pinne (per animale acquatico) e il genere Mammifero o Pesce o Rettile
            * Si realizzino le classi derivate da AnimaleTerrestre o AnimaleAcquatico
            * Leone, Gallina, Coccordillo, Tricheco, Delfino, Pesce Spada
            * e inventare qualche attributo per ognuna di queste classi (tipo peso, velocità, ...)
            * Creare una lista di animali di questi tipi, possibilmente più di uno per classe
            * Poi: Creare un menu che consente di creare nuovi animali, di salvare su file la lista di animali (in formato JSON), di recuperare il file la lista di animali. 

        */

        Pesce_Spada Viktor = new Pesce_Spada(2, "Maschio", 4, 5, 1, 34, "Grigio");
        Pesce_Spada Giovanni = new Pesce_Spada(2, "Femmina", 5, 3, 1, 23, "Grigio");

        Delfino Ivan = new  Delfino(2, "Maschio", 5, 3, 34);
        Delfino Sergej = new  Delfino(2, "Femmina", 6, 4, 55);

        Tricheco Ronaldo = new Tricheco("Grigio", 34, 3, 2, "Neutro");
        Tricheco Rosario = new Tricheco("Grigio",21, 5, 2, "Femmina");
        
        Leone Gennaro = new Leone(4, "Mammifero", 67, 25);
        Leone Mufasa = new Leone(4, "Mammifero", 55, 33);

        Gallina cocca = new Gallina(2, "Mammifero", 5, 7);
        Gallina cocco = new Gallina(2, "Mammifero", 6, 8);

        Coccodrillo giacomo = new Coccodrillo(4, "Rettile", 200, 10, 1600);
        Coccodrillo Philippa = new Coccodrillo(4, "Rettile", 150, 13, 1250);

        LinkedList<Animale> lA = new LinkedList<Animale>();
        lA.add(Philippa);
        lA.add(Mufasa);
        lA.add(giacomo);
        lA.add(cocco);
        lA.add(cocca);
        lA.add(Gennaro);
        lA.add(Ivan);
        lA.add(Sergej);
        lA.add(Viktor);
        lA.add(Giovanni);
        lA.add(Sergej);
        lA.add(Ronaldo);
        lA.add(Rosario);
        
        System.out.println(lA);
      }

}