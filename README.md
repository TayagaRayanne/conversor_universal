# Conversor Universal

Bem-vindo ao **Conversor Universal**!  
Este projeto é um aplicativo de linha de comando em Python que permite converter facilmente entre diferentes unidades de temperatura, moeda, medidas e tempo. Ele foi desenvolvido com foco em organização, clareza e facilidade de uso, sendo ideal para estudantes, professores, desenvolvedores iniciantes ou qualquer pessoa que precise realizar conversões rápidas no dia a dia.

---

## Funcionalidades

O Conversor Universal oferece os seguintes módulos de conversão:

- **Temperatura**
  - Celsius para Fahrenheit
  - Fahrenheit para Celsius

- **Moeda**
  - Real para Dólar (com cotação configurável)
  - Dólar para Real

- **Medidas**
  - Metros para Quilômetros
  - Quilômetros para Metros

- **Tempo**
  - Segundos para Minutos
  - Minutos para Segundos

---

## Como funciona

Ao executar o programa, você verá um menu principal com as opções de conversão. Basta escolher o tipo de conversão desejada e seguir as instruções na tela para inserir os valores. O resultado da conversão será exibido imediatamente, sempre com duas casas decimais para facilitar a leitura.

O código é modularizado: cada tipo de conversão possui sua própria classe, localizada na pasta `conversor/`. Isso facilita a manutenção e a expansão do projeto.

---

## Estrutura do Projeto

- **Main.py**: Arquivo principal, responsável pelo menu e interação com o usuário.
- **conversor/**: Pasta com as classes de conversão, cada uma especializada em um tipo de unidade.

---

## Pontos de dificuldades

Os conversores foram desenvolvidos de forma simplificada, cada um com apenas duas funcionalidades. Ainda assim, enfrentei algumas dificuldades, principalmente relacionadas aos cálculos.

Um exemplo foi ao implementar a conversão de segundos para minutos. Inicialmente, utilizei apenas uma divisão simples e não considerei a necessidade de calcular o "resto da divisão" (módulo). Só percebi esse detalhe após encontrar alguns erros no resultado.

Gostaria de destacar que esse é o meu primeiro projeto feito 100% sozinha, sem apoio direto de professores ou tutores. Enfrentei vários desafios ao longo do processo, e superá-los me trouxe uma alegria enorme. Fico muito feliz em compartilhar essa experiência aqui.

---

## Licença

Este projeto é livre para uso educacional e pessoal.

---
  
Sinta-se à vontade para contribuir ou sugerir melhorias!
