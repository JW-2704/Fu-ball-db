from anvil import data_files
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