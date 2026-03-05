from ._anvil_designer import DashboardMarktwertTemplate
from anvil import *
import anvil.server
import plotly.graph_objects as go

class DashboardMarktwert(DashboardMarktwertTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    db_data = anvil.server.call('get_marktwerte_pro_verein')

    vereine = [r[0] for r in db_data]
    werte = [r[1] for r in db_data]

    self.plot_marktwerte.data = [
      go.Bar(x=vereine, y=werte, marker_color='#2196F3')
    ]
    self.plot_marktwerte.layout.title = "Kaderwerte pro Verein"