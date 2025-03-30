from flask import Flask, render_template, request, redirect, url_for
from gestio_participants import afegir_participant, carregar_participants_de_fitxer, desar_participants_a_fitxer
from gestio_partides import generar_partides, carregar_partides_de_fitxer, desar_partides_a_fitxer
from puntuacions import actualitzar_puntuacions, calcular_ranquing
from utils import validar_nom
import os

app = Flask(__name__)

# Configuración de archivos
PARTICIPANTS_FILE = 'participants.txt'
PARTIDES_FILE = 'partides.txt'
PUNTUACIONS_FILE = 'puntuacions.txt'

# Variables globales
participants = []
partides = []
puntuacions = {}

# Cargar datos existentes al iniciar
if os.path.exists(PARTICIPANTS_FILE):
    participants = carregar_participants_de_fitxer(PARTICIPANTS_FILE)
if os.path.exists(PARTIDES_FILE):
    partides = carregar_partides_de_fitxer(PARTIDES_FILE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/participants', methods=['GET', 'POST'])
def gestionar_participants():
    global participants
    error = None
    
    if request.method == 'POST':
        nom = request.form['nom']
        if validar_nom(nom):
            if nom not in participants:  # Evitar duplicados
                participants.append(nom)
                desar_participants_a_fitxer(participants, PARTICIPANTS_FILE)
                return redirect(url_for('gestionar_participants'))  # Recarga la página
            else:
                error = "Aquest participant ja està registrat."
        else:
            error = "Nom invàlid. Només es permeten lletres i espais."
    
    return render_template('participants.html', participants=participants, error=error)

@app.route('/partides')
def mostrar_partides():
    global partides
    if not partides and participants:
        partides = generar_partides(participants)
        desar_partides_a_fitxer(partides, PARTIDES_FILE)
    return render_template('partides.html', partides=partides)

@app.route('/puntuacions')
def mostrar_puntuacions():
    global puntuacions
    if participants and not puntuacions:
        puntuacions = {participant: 0 for participant in participants}
    
    ranking = calcular_ranquing(puntuacions)
    return render_template('puntuacions.html', puntuacions=puntuacions, ranking=ranking)

@app.route('/ranking')
def mostrar_ranking():
    global puntuacions
    if participants and not puntuacions:
        puntuacions = {participant: 0 for participant in participants}
    
    ranking = calcular_ranquing(puntuacions)
    return render_template('ranking.html', ranking=ranking)

@app.route('/actualitzar_puntuacio', methods=['POST'])
def actualitzar_puntuacio():
    global puntuacions
    guanyador = request.form['guanyador']
    puntuacions = actualitzar_puntuacions(puntuacions, guanyador)
    return redirect(url_for('mostrar_puntuacions'))

if __name__ == '__main__':
    app.run(debug=True)