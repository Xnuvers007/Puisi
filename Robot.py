import pyttsx3
import time
import webbrowser
import os, sys

mesin = pyttsx3.init()
mesin.setProperty('volume', 1)
rate = 100
mesin.setProperty('rate', rate)

def txt():
   print("Ini Adalah program Puisi Versi Robot...") #IG FARHAN = fhrhn_juna.6199
   print("Puisi Dibuat oleh fhrhn_juna.6199")
   print("=="*10+"===========")
   print("|"+"==="*10+"|")
   print("[1.] Langit Senja...")
   print("[2.] ")
   print("|"+"==="*10+"|")
   print("=="*10+"===========")
   print("\n")
   pilih = int(input("Masukan Nomornya: "))
   print("\n")
   if(pilih==1):
      Langit()
   else:
      print("Yang Anda Masukan Salah...")

def Langit():
   print ('''
\\\request from Indra///

Langit senja...
Saat dunia menjadi jingga...
Ketika mentari kembali kepersinggahannya...
Dan seakan menjadi lukisan alam yang nyata...

Langit jingga...
Burung burung mengukir siluet indah...
Air memantulkan pesonanya...
Dari cahaya yang aku mengaguminya...

Langit senja yang indah...
Dari pesisir sang nirwana..
Adalah karya indah sang pencipta...
Yang akan aku kagumi sepanjang massa...

- fhrhn_juna.6199
''')
   a = "\t\tLangit\t\t\n"
   b = "Langit Senja...\n"
   c = "Saat Dunia Menjadi Jingga...\n"
   d = "Ketika Mentari kembali Kepersinggahannya...\n"
   e = "Dan Seakan Menjadi Lukisan Alam yang nyata...\n\n"
   f = "Langit jingga...\n"
   g = "Burung burung mengukir siluet indah...\n"
   h = "Air memantulkan pesonanya...\n"
   i = "Dari cahaya yang aku mengaguminya...\n\n"
   j = "Langit senja yang indah...\n"
   k = "Dari pesisir sang nirwana..\n"
   l = "Adalah karya indah sang pencipta...\n"
   m = "Yang akan aku kagumi sepanjang massa..."
   bicara = mesin.say(a)
   time.sleep(1)
   bicara = mesin.say(b)
   time.sleep(1)
   bicara = mesin.say(c)
   time.sleep(1)
   bicara = mesin.say(d)
   time.sleep(1)
   bicara = mesin.say(e)
   time.sleep(1)
   bicara = mesin.say(f)
   time.sleep(1)
   bicara = mesin.say(g)
   time.sleep(1)
   bicara = mesin.say(h)
   time.sleep(1)
   bicara = mesin.say(i)
   time.sleep(1)
   bicara = mesin.say(j)
   time.sleep(1)
   bicara = mesin.say(k)
   time.sleep(1)
   bicara = mesin.say(l)
   time.sleep(1)
   bicara = mesin.say(m)
   bicara = mesin.runAndWait()
   print(bicara)

txt()
