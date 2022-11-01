# coding=utf-8
#-*- coding: latin 1 -*-

valor1 = input("Insira um valor: ")
valor2 = input("Insira um segundo valor: ")
valor3 = input("Insira um terceiro valor: ")
menor = valor1
if valor1<valor2 and valor1<valor3:
    menor = valor1
if valor2<valor1 and valor2<valor3:
    menor = valor2
if valor3<valor1 and valor3<valor2:
    menor = valor3

print "O menor valor inserido foi:", menor