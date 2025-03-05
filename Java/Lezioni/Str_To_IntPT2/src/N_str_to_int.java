
import java.util.Scanner;

public class N_str_to_int {
    public static void main(String[] args) throws Exception {
        //PRIMA PARTE: ESTRARRE GLI OPERANDI E L'OPERATORE DALLA STRINGA
        //Input da Tastiera
        Scanner scanner = new Scanner(System.in);
        System.out.println("\nInserisci l'operazione da fare: ");
        String operazione = scanner.nextLine();
        //Eliminazione degli spazi
        operazione = operazione.replaceAll(" ", "");
        System.out.println(operazione);
        //Ricavo gli Operandi dall'operazione
        String[] operandi = operazione.split("[//+//-//*// / //]");

        for (String s : operandi){
            System.out.println(s);
        }
        //Ricavo il segno utilizzato
        String[] voperatore = operazione.split("[0-9]+");
        for (String s: voperatore) {
            System.out.println("<" + s + ">");
        }
        String operatore = voperatore[1];
        
        for (int i = 0; i < operandi.length; i++) {
            int op1 = Integer.parseInt(operandi[0]);
            int op2 = Integer.parseInt(operandi[1]);
            switch (operatore){
                case "+":
                
                    System.out.println(op1 + op2);
                    break;
                case "-":
                    System.out.println(op1 - op2);
                    break;
                case "*":
                    System.out.println(op1 * op2);
                    break;
                case "/":
                    System.out.println(op1 / op2);
                    break;
        }
    }
}
}