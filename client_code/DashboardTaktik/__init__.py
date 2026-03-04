from ._anvil_designer import DashboardTaktikTemplate
from anvil import *
import anvil.server
import plotly.graph_objects as go

class DashboardTaktik(DashboardTaktikTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    data = anvil.server.call('get_formation_stats')

    labels = [r[0] for r in data]
    values = [r[1] for r in data]

    self.plot_taktik.data = [
      go.Pie(labels=labels, values=values, hole=0.3)
    ]
    self.plot_taktik.layout.title = "Meistgenutzte Formationen"