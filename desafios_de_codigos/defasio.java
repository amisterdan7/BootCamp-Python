package desafios_de_codigos;

// Calcular o percentual de imposto sobre o salário
// R$ 0 00 a R$ 1100 = 5% imposto
// R$ 1100,00 a R$ 2500 = 10% imposto
// Acima de R$ 2500 = 15% imposto

import java.util.Scanner;

public class defasio {
    
    public static void main(String[] args) {
        
        //Ler os valores do usuário
        Scanner scanner = new Scanner(System.in);
        float valorsalário = scanner.nextFloat();
        float valorBeneficios = scanner.nextFloat();

        float valorImposto = 0;
        if(valorsalário >= 0 && valorsalário <= 1100){
            valorImposto = 0.05f * valorsalário;
        }
        else if(valorsalário > 1100 && valorsalário <= 2500){
            valorImposto = 0.10f * valorsalário;
        }
        else if(valorsalário > 2500){
            valorImposto = 0.15f * valorsalário;
        }
        
        float saida = valorsalário - valorImposto + valorBeneficios;
        System.out.println(String.format("%.2f", saida));


        scanner.close();
    }

   
}
