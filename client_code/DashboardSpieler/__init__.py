from ._anvil_designer import DashboardSpielerTemplate
from anvil import *
import anvil.server

class DashboardSpieler(DashboardSpielerTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    spieler_daten = anvil.server.call('get_spieler_liste')
    self.repeating_panel_1.items = spieler_daten