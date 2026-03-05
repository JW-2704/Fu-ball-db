from anvil.files import data_files
import anvil.server
import sqlite3


@anvil.server.callable
def get_marktwerte_pro_verein():
  # Annahme: Deine DB heißt 'fussball.db' in den Data Files
  conn = sqlite3.connect(data_files['Fußball.db'])
  cur = conn.cursor()
  cur.execute("SELECT v.name, SUM(f.marktwert) FROM Verein v JOIN Fußballer f ON v.vid = f.vid GROUP BY v.name")
  return cur.fetchall()

@anvil.server.callable
def get_formation_stats():
  conn = sqlite3.connect(data_files['Fußball.db'])
  cur = conn.cursor()
  cur.execute("SELECT taktik, COUNT(*) FROM Formation GROUP BY taktik")
  return cur.fetchall()

@anvil.server.callable
def get_stadium_stats():
  with sqlite3.connect(data_files['Fußball.db']) as conn:
    cur = conn.cursor()
    # Verknüpft Verein mit Stadium über die Spiel-Tabelle oder direkt, 
    # hier basierend auf der Stadium-Tabelle für eine Kapazitätsübersicht
    query = "SELECT name, ort, kapazitaet FROM Stadium ORDER BY kapazitaet DESC"
    cur.execute(query)
    return cur.fetchall()

@anvil.server.callable
def get_spieler_liste():
  with sqlite3.connect(data_files['Fußball.db']) as conn:
    cur = conn.cursor()
    # Wir selektieren Name, Herkunft, Position und Marktwert
    query = "SELECT name, herkunft, position, marktwert, alter_wert FROM Fußballer ORDER BY marktwert DESC"
    cur.execute(query)
    # Umwandlung in eine Liste von Dicts für das Data Grid
    return [{'name': r[0], 'herkunft': r[1], 'position': r[2], 'marktwert': r[3], 'alter_wert': r[4]} for r in cur.fetchall()]