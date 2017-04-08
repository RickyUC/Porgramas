__author__ = 'Ricardo Del Rio'

from cartas import Carta


with open('stock_prices.csv') as archivo:
    cartas = (linea for linea in archivo)
    lista_cartas = [Carta()]



