from ._anvil_designer import DashboardSpielerTemplate
from anvil import *
import anvil.server

class DashboardSpieler(DashboardSpielerTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Daten vom Server laden
    spieler_daten = anvil.server.call('get_spieler_liste')

    # Das RepeatingPanel im Data Grid mit den Daten füllen
    self.repeating_panel_1.items = spieler_daten