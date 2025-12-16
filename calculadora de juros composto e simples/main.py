#!/usr/bin/env python3
import argparse
from math import pow


def juros_simples(capital: float, taxa_percent: float, tempo: float) -> float:
    taxa = taxa_percent / 100.0
    montante = capital * (1 + taxa * tempo)
    return montante


def juros_compostos(capital: float, taxa_percent: float, tempo: float, comp_per_year: int = 1) -> float:
    taxa = taxa_percent / 100.0
    n = comp_per_year
    montante = capital * pow(1 + taxa / n, n * tempo)
    return montante


def format_currency(value: float) -> str:
    return f"R$ {value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')


def main():
    parser = argparse.ArgumentParser(description="Calculadora de juros simples e compostos")
    parser.add_argument('-m', '--modo', choices=['simples', 'composto'], default='composto', help='Modo: simples ou composto')
    parser.add_argument('-c', '--capital', type=float, required=True, help='Capital inicial (ex: 1000)')
    parser.add_argument('-r', '--taxa', type=float, required=True, help='Taxa percentual anual (ex: 5 para 5%%)')
    parser.add_argument('-t', '--tempo', type=float, required=True, help='Tempo em anos (ex: 2.5)')
    parser.add_argument('-n', '--periodos', type=int, default=1, help='Compostos por ano (apenas para composto)')

    args = parser.parse_args()

    C = args.capital
    i = args.taxa
    t = args.tempo

    if args.modo == 'simples':
        mont = juros_simples(C, i, t)
        juros = mont - C
        print('Juros Simples')
    else:
        mont = juros_compostos(C, i, t, args.periodos)
        juros = mont - C
        print('Juros Compostos')

    print(f'Capital inicial: {format_currency(C)}')
    print(f'Taxa anual: {i}%')
    print(f'Tempo: {t} anos')
    if args.modo == 'composto':
        print(f'Compostos por ano: {args.periodos}')
    print(f'Montante: {format_currency(mont)}')
    print(f'Juros: {format_currency(juros)}')


if __name__ == '__main__':
    main()
