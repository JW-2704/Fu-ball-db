from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

from .DashboardMarktwert import DashboardMarktwert
from .DashboardTaktik import DashboardTaktik

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Forms einmal erstellen
    self.marktwert_form = DashboardMarktwert()
    self.taktik_form = DashboardTaktik()

    # Startseite laden
    self.column_panel_2.clear()
    self.column_panel_2.add_component(self.marktwert_form)

  def marktwert_click(self, **event_args):
    self.column_panel_2.clear()
    self.column_panel_2.add_component(self.marktwert_form)

  def taktik_click(self, **event_args):
    self.column_panel_2.clear()
    self.column_panel_2.add_component(self.taktik_form)