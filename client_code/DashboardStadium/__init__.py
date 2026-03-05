from ._anvil_designer import DashboardStadiumTemplate
from anvil import *
import anvil.server
import plotly.graph_objects as go

class DashboardStadium(DashboardStadiumTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Daten abrufen (Name, Ort, Kapazität)
    data = anvil.server.call('get_stadium_stats')

    stadium_namen = [f"{r[2]} ({r[1]})" for r in data] # Name + Ort
    kapazitaet = [r[2] for r in data]

    # Visualisierung der Stadionkapazitäten
    self.plot_stadium.data = [
      go.Bar(
        x=stadium_namen,
        y=kapazitaet,
        marker_color='#FF9800', # Orangefarbene Balken
        text=kapazitaet,
        textposition='auto'
      )
    ]

    self.plot_stadium.layout.title = "Stadien nach Kapazität"
    self.plot_stadium.layout.xaxis.title = "Stadion (Ort)"
    self.plot_stadium.layout.yaxis.title = "Plätze"