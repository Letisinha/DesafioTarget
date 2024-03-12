# DesafioTarget
Nesse repositório apresento os resultados do desafio para o estágio em desenvolvimento na Target Sistemas. 

---------------------------------------------------

1) Observe o trecho de código abaixo:

````
int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?
````

### [Solução Soma](https://github.com/Letisinha/DesafioTarget/blob/main/Scripts/Soma.py) 

---------------------------------------------------

2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

### [Solução Fibonacci](https://github.com/Letisinha/DesafioTarget/blob/main/Scripts/fibonacci.py)

---------------------------------------------------

3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, **9**

b) 2, 4, 8, 16, 32, 64, **128**

c) 0, 1, 4, 9, 16, 25, 36, **49**

d) 4, 16, 36, 64, **100**

e) 1, 1, 2, 3, 5, 8, **13**

f) 2,10, 12, 16, 17, 18, 19, **200**

### [Solução automatizada Lógica](https://github.com/Letisinha/DesafioTarget/blob/main/Scripts/logica.py)

---------------------------------------------------

4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

### Solução:
````
Considerando os três interruptores como **int 1, int 2 e int 3** irei e as salas como **sala X**, **sala Y** e **sala Z**:
- Deixar o **int 1** desligado.
- Ligar o **int 2** por proximadamente 10 minutos e então desligá-lo.
- Deixar o **int 3** ligado o tempo todo.
E então ir até a **sala X** pela primeira vez.
- Se a lâmpada estiver acesa, pertence ao **int 3**
- Se estiver desligada e quente, pertence ao **int 2**
Na segunda ida, já sabendo, pelo menos a relação entre um interruptor e uma lâmpada e excluindo ambos:
- Deixo uma das lâmpadas restantes acesa e a outra apagada
- Vou até a **sala Y** e verifico se a lâmpada está acesa ou apagada
- Estando acesa ou apagada, será possível deduzir qual interruptor pertence à **sala Z**.
````

---------------------------------------------------

5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

### [Solução Inversão](https://github.com/Letisinha/DesafioTarget/blob/main/Scripts/inverter.py)
