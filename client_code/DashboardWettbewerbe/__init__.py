from ._anvil_designer import DashboardWettbewerbeTemplate
from anvil import *
import anvil.server

class DashboardWettbewerbe(DashboardWettbewerbeTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Daten vom Server laden
    wettbewerb_daten = anvil.server.call('get_wettbewerb_liste')

    # Das RepeatingPanel im Data Grid mit den Daten füllen
    self.repeating_panel_1.items = wettbewerb_daten