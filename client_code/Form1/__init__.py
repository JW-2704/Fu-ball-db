from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

from ..DashboardMarktwert import DashboardMarktwert
from ..DashboardTaktik import DashboardTaktik
from ..DashboardStadium import DashboardStadium # Neu importieren

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Alle Forms einmal im Speicher erstellen
    self.marktwert_form = DashboardMarktwert()
    self.taktik_form = DashboardTaktik()
    self.stadium_form = DashboardStadium() # Neu erstellt

    # Startseite laden
    self.column_panel_2.clear()
    self.column_panel_2.add_component(self.marktwert_form)

  @handle("marktwert", "click")
  def marktwert_click(self, **event_args):
    self.column_panel_2.clear()
    self.column_panel_2.add_component(self.marktwert_form)

  @handle("taktik", "click")
  def taktik_click(self, **event_args):
    self.column_panel_2.clear()
    self.column_panel_2.add_component(self.taktik_form)

  @handle("stadium", "click") # Name des neuen Buttons im Designer
  def stadium_click(self, **event_args):
    self.column_panel_2.clear()
    self.column_panel_2.add_component(self.stadium_form)