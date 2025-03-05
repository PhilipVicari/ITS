import java.util.Random;

class ParseClass {
    private static String[] nomiCibo = {
        "Pasta al pesto", "Risotto ai funghi", "Spaghetti alla carbonara",  // Primi
        "Bistecca", "Pollo arrosto", "Salmone alla griglia",               // Secondi
        "Tiramisu", "Panna cotta", "Gelato al cioccolato"                  // Dolci
    };
    private static double[] calorieCibo = {
        400, 450, 500,  // Calorie per i Primi
        600, 550, 500,  // Calorie per i Secondi
        300, 250, 200   // Calorie per i Dolci
    };
    private static double[] prezzoCibo = {
        8.0, 7.5, 9.0,  // Prezzo per i Primi
        15.0, 12.0, 14.0, // Prezzo per i Secondi
        6.0, 5.0, 4.0    // Prezzo per i Dolci
    };
    private static String[] tipiCibo = {
        "Primo", "Primo", "Primo", "Secondo", "Secondo", "Secondo", "Dolce", "Dolce", "Dolce"
    };
    private static Random random = new Random();

    public static Cibo Parse(String className) {
        if (className.equals("Cibo")){
            String nome = nomiCibo[random.nextInt(nomiCibo.length)];
            double calorie = calorieCibo[random.nextInt(calorieCibo.length)];
            double prezzo = prezzoCibo[random.nextInt(prezzoCibo.length)];
            String tipo = tipiCibo[random.nextInt(tipiCibo.length)];
            return new Cibo(nome, tipo, prezzo, calorie);
        }
        return null;
    }
}
