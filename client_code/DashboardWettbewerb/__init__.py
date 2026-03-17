from ._anvil_designer import DashboardWettbewerbTemplate
from anvil import *
import anvil.server

class DashboardWettbewerb(DashboardWettbewerbTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    wettbewerb_daten = anvil.server.call('get_wettbewerb_liste')
    self.repeating_panel_1.items = wettbewerb_daten