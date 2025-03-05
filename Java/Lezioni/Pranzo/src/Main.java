public class Main {

	public static void main(String[] args) {
		/*
		 * Creiamo una classe Cibo con gli attributi che deciderete voi
		 * Creiamo un array di 10 Cibi (che sarebbe il pranzo o la cena)
		 */

        //1) Calcolare il numero totale di calorie assunte con questo menu
		Cibo[] menu = new Cibo[9];
        double Calorie_tot=0;
        for (int i = 0; i < menu.length; i++) {
            menu[i] = (Cibo)ParseClass.Parse("Cibo");
            System.out.println(menu[i]);
            Calorie_tot += menu[i].getCalorie();
        }
        System.out.println("\nLe calorie totali sono: " + Calorie_tot);
		//2) Costruire a partire da questo menu un pranzo per 50 persone,
		//   dove ogni portata è composta da tre cibi presi a caso da questo menu
		// Esempio, se menu fosse di 5 elementi, allora una 
		// portata del pranzo per 50 persone
		// sarà composta di tre elementi di menu presi a caso
		/* Difficoltà:
		 * 	Il pranzo di 50 persone è un array di pranzi dove ogni singolo pranzo contiene tre portate. Come fare? 
		 *
		 *Altro esempio
		 *Supponiamo che menu sia composto da (elenco solo i 
		 *nomi delle pietanze, senza indicare calorie o quant'altro,
		 *per semplicità di lettura dell'esempio stesso
		 *	[pasta e ceci, lombata, sogliola, pesce persico, delizia al limone, carciofi, pasta al forno, creme brulee, carbonara]
		 *Io intendo realizzare un pranzo per 50 persone del tipo
		 *persona1		persona2		persona3 ...
		 *pasta e ceci	pasta al forno	carbonara
		 *sogliola		sogliola		lombata
		 *creme brulee	del al limone	carciofi
		 */
        for (int i = 0; i < 5; i++) {
            System.out.println("\nQuesta persona ha questo menu: ");
            for (int j = 0; j < 3; j++) {
                System.out.println(j+1 + ")" + menu[(int)(Math.random()*5)]);
                }
            }
        }
	}
