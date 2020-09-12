import time
start_time = time.time()
import urllib.request, json
import datetime
with urllib.request.urlopen("http://open-api.myhelsinki.fi/v1/events/") as url:
    data = json.loads(url.read().decode())

print("--- %s seconds ---" % (time.time() - start_time)) # Saadaan aika joka käytettiin JSON:nin lataamiseen

# Lataamiseen kuluu erittäi suuri aika. Lataus kesti --- 9.342572927474976 seconds --- 100MB/s netillä, kun taas ohjelma koko suoritettiin ajassa --- 11.650035381317139 seconds --- 
# Ladattavan koon myötä itse ohjelma ei paljoakaan hidastu mutta lataamiseen kulutettu aika kasvaa

lista = []

def mergeSort(lista): 
    if len(lista) > 1: 
        keskikohta = len(lista)//2  # Lasketaan keskikohta
        L = lista[:keskikohta]      # Puolitetaan lista
        R = lista[keskikohta:] 
  
        mergeSort(L)                #Käytetään rekursiivista funktiota apuna
        mergeSort(R) 
  
        i = j = k = 0
        
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                lista[k] = L[i] 
                i+= 1
            else: 
                lista[k] = R[j] 
                j+= 1
            k+= 1
          
        while i < len(L): 
            lista[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            lista[k] = R[j] 
            j+= 1
            k+= 1
    return lista

for i,x in enumerate(data["data"]):
    try:
        lista.append((x["event_dates"]["starting_day"],i))    # Datan muuntelua str:stä datetimeen jotta vertailu helpottuisi
    except:
        pass


print(lista)

for i in mergeSort(lista):
    print(datetime.datetime.strptime(data["data"][i[1]]["event_dates"]["starting_day"],"%Y-%m-%dT%H:%M:%S.%fZ"),data["data"][i[1]]["name"]["fi"] )      # Luodaan nätimpää tulostusta

print("--- %s seconds ---" % (time.time() - start_time))    # Saadaan ohjelman kokonaisajoaika