public class Desafio {
    public static void Main(string[] args) {
        // Ler os valores do usuário
        float valorsalário = float.Parse(Console.ReadLine());
        float valorBeneficios = float.Parse(Console.ReadLine());

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
        Console.WriteLine($"{saida:F2}");
    }
}
