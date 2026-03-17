from ._anvil_designer import DashboardSpieleTemplate
from anvil import *
import anvil.server

class DashboardSpiele(DashboardSpieleTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Hier rufen wir die Daten vom Backend ab
    spiel_daten = anvil.server.call('get_spiele_liste')
    self.repeating_panel_1.items = spiel_daten