from ._anvil_designer import DashboardStadiumTemplate
from anvil import *
import anvil.server
import plotly.graph_objects as go

class DashboardStadium(DashboardStadiumTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    data = anvil.server.call('get_stadium_stats')
    labels = [f"{r[0]} - {r[1]}" for r in data]
    kapazitaet = [r[2] for r in data]

    self.plot_stadium.data = [
      go.Bar(
        x=labels,
        y=kapazitaet,
        marker_color='red',
        text=kapazitaet,
        textposition='auto',
        name="Plätze"
      )
    ]
    self.plot_stadium.layout.title = "Stadien und Standorte"

  