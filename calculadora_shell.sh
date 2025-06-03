#!/bin/bash


# Calculador


echo "Digite o primeiro número:"
read num1

echo "Digite o segundo número:"
read num2

echo "Escolha uma operação (soma, subtracao, multiplicacao, divisao):"
read operacao

if [ "$operacao" == "soma" ]; then
  resultado=$((num1 + num2))
elif [ "$operacao" == "subtracao" ]; then
  resultado=$((num1 - num2))
elif [ "$operacao" == "multiplicacao" ]; then
  resultado=$((num1 * num2))
elif [ "$operacao" == "divisao" ]; then
  resultado=$((num1 / num2))
else
  echo "Operação inválida!"
  exit 1
fi

echo "Resultado: $resultado"



