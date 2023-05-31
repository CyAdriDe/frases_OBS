import pandas as pd
import time
import csv

def read_sheet():
	SHEET_ID = '1F7Q3YZZ8vzKq5ifFmp04NrrXKJDMzTDrXNmp-WcVsQ4'
	SHEET_NAME = 'Sheet1'
	url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
	df = pd.read_csv(url)
	df.to_csv('llista_sheets.csv', index=False, encoding='utf-8')

def create_list():
	TEMPS_ESPERA = 8
	with open('llista_sheets.csv', 'r') as f:
		frases = []
		text = f.readline()
		while text != "":
			frases.append(text.rstrip())
			text = f.readline()
	frases = frases[::-1]

	for item in frases:
		with open('llista.txt', 'w') as fp:
			print(item)
			fp.write(item)
			fp.close()
		time.sleep(TEMPS_ESPERA)

if __name__ == '__main__':
	while (True):
		read_sheet()
		create_list()