
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        //PRIMA PARTE: ESTRARRE GLI OPERANDI E L'OPERATORE DALLA STRINGA
        Scanner scanner = new Scanner(System.in);
        System.out.println("Inserisci l'operazione da fare: ");

        String operazione = scanner.nextLine();
        operazione = operazione.replaceAll(" ", "");
        System.out.println(operazione);

        String[] operandi = operazione.split("[//+//-//*// / //]");

        for (String s : operandi){
            System.out.println(s);
        }

        String[] voperatore = operazione.split("[0-9]+");
        for (String s: voperatore) {
            System.out.println("<" + s + ">");
        }

        String operatore = voperatore[1];
//----------------------------------------------------------------------------------------------------
        //SECONDA PARTE: ESEGUIRE L'OPERAZIONE IMMESSA IN INPUT
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
