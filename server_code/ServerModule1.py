from anvil.files import data_files
import anvil.server
import sqlite3


@anvil.server.callable
def get_marktwerte_pro_verein():
  conn = sqlite3.connect(data_files['Fußball.db'])
  cur = conn.cursor()
  cur.execute("SELECT Verein.name, SUM(Fußballer.marktwert) FROM Verein JOIN Fußballer ON Verein.vid = Fußballer.vid GROUP BY Verein.name")
  return cur.fetchall()

@anvil.server.callable
def get_verein_liste():
  conn = sqlite3.connect(data_files['Fußball.db'])
  cur = conn.cursor()
  cur.execute("SELECT name, personal, gruendung FROM Verein ORDER BY gruendung")
  return [{"name": r[0], "personal": r[1], "gruendung": r[2]} for r in cur.fetchall()]

@anvil.server.callable
def get_formation_stats():
  conn = sqlite3.connect(data_files['Fußball.db'])
  cur = conn.cursor()
  cur.execute("SELECT taktik, COUNT(*) FROM Formation GROUP BY taktik")
  return cur.fetchall()

@anvil.server.callable
def get_stadium_stats():
    conn = sqlite3.connect(data_files['Fußball.db'])
    cur = conn.cursor()
    cur.execute("SELECT name, ort, kapazitaet FROM Stadium ORDER BY kapazitaet DESC")
    return cur.fetchall()

@anvil.server.callable
def get_spieler_liste():
    conn = sqlite3.connect(data_files['Fußball.db'])
    cur = conn.cursor()
    cur.execute("SELECT name, herkunft, position, marktwert, alter_wert FROM Fußballer ORDER BY marktwert DESC")
    return [{'name': r[0], 'herkunft': r[1], 'position': r[2], 'marktwert': r[3], 'alter_wert': r[4]} for r in cur.fetchall()]


@anvil.server.callable
def get_wettbewerb_liste():
    conn = sqlite3.connect(data_files['Fußball.db'])
    cur = conn.cursor()
    cur.execute("SELECT turnier_name, preisgeld, anzahl_runden FROM Wettbewerb")
    return [{"turnier_name": r[0], "preisgeld": r[1], "anzahl_runden": r[2]} for r in cur.fetchall()]

@anvil.server.callable
def get_spiele_liste():
  conn = sqlite3.connect(data_files['Fußball.db'])
  cur = conn.cursor()
  cur.execute("SELECT Spiel.spid, Spiel.datum, Spiel.ergebnis, Spiel.zuschauer, Stadium.name, Wettbewerb.turnier_name FROM Spiel LEFT JOIN Stadium ON Spiel.sid = Stadium.sid LEFT JOIN Wettbewerb ON Spiel.wid = Wettbewerb.wid")
  rows = cur.fetchall()

  spiele_liste = []
  for r in rows:
    spid = r[0]
    cur.execute("""
            SELECT Verein.name FROM Verein 
            JOIN Hat ON Verein.vid = Hat.vid 
            WHERE Hat.spid = ?
        """, (spid,))
    vereine = [row[0] for row in cur.fetchall()]

    spiele_liste.append({
      "datum": r[1],
      "ergebnis": r[2],
      "zuschauer": r[3],
      "stadium": r[4],
      "wettbewerb": r[5],
      "paarung": " vs. ".join(vereine) if vereine else "Keine Teams"
    })
  return spiele_liste