from ._anvil_designer import DashboardVereinTemplate
from anvil import *
import anvil.server

class DashboardVerein(DashboardVereinTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    verein_daten = anvil.server.call('get_verein_liste')
    self.repeating_panel_1.items = verein_daten