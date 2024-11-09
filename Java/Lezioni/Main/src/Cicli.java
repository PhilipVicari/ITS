import java.util.Scanner;
 
public class Cicli {
 
    public static void main(String[] args) {
        int pippo = 10;
    // Stampare i numeri interi da 0 a 10 (10 escluso)
        for (int i = 0; i < 10; i++) {
            pippo = pippo + i;
            System.out.println(i);
        }

    // Stampare la tabellina del 7 in due modi diversi
        for (int i=0; i<=70; i+=7){
            System.out.println("Il Primo Modo è: " + i);
        }
        for (int i=1; i<=10; i++){
            int prodotto = 7 * i;
            System.out.println("Il Secondo Modo è: " + prodotto);
        }
    //Legge due numeri da input e riconosce se sono maggiori o minori di 0
        Scanner Legge = new Scanner(System.in);
        for (int i = 0; i<=10; i++){
            int N= Legge.nextInt();
            if (N > 10){
                System.out.println("Il numero è maggiore di 10");
            }else{
                System.out.println("Il numero è minore di 10");
            }   
        }
        
    }   
    
}