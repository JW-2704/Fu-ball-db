from anvil.files import data_files
import anvil.server
import sqlite3


@anvil.server.callable
def get_marktwerte_pro_verein():
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
    cur.execute("SELECT name, ort, kapazitaet FROM Stadium ORDER BY kapazitaet DESC")
    return cur.fetchall()

@anvil.server.callable
def get_spieler_liste():
  with sqlite3.connect(data_files['Fußball.db']) as conn:
    cur = conn.cursor()
    cur.execute("SELECT name, herkunft, position, marktwert, alter_wert FROM Fußballer ORDER BY marktwert DESC")
    return [{'name': r[0], 'herkunft': r[1], 'position': r[2], 'marktwert': r[3], 'alter_wert': r[4]} for r in cur.fetchall()]


@anvil.server.callable
def get_wettbewerb_liste():
  with sqlite3.connect(data_files['Fußball.db']) as conn:
    cur = conn.cursor()
    cur.execute("SELECT turnier_name, preisgeld, anzahl_runden FROM Wettbewerb")
    return [{"turnier_name": r[0], "preisgeld": r[1], "anzahl_runden": [2]} for r in cur.fetchall()]