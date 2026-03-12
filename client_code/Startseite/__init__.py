from ._anvil_designer import StartseiteTemplate
from anvil import *
import anvil.server

from ..DashboardMarktwert import DashboardMarktwert
from ..DashboardTaktik import DashboardTaktik
from ..DashboardStadium import DashboardStadium
from ..DashboardSpieler import DashboardSpieler
from ..DashboardWettbewerbe import DashboardWettbewerbe

class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.marktwert_form = DashboardMarktwert()
    self.taktik_form = DashboardTaktik()
    self.stadium_form = DashboardStadium()
    self.spieler_form = DashboardSpieler()
    self.wettbewerb_form = DashboardWettbewerbe()

    self.column_panel_2.clear()

  @handle("marktwert", "click")
  def marktwert_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.column_panel_2.clear()
    self.column_panel_2.add_component(self.marktwert_form)

  @handle("taktik", "click")
  def taktik_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.column_panel_2.clear()
    self.column_panel_2.add_component(self.taktik_form)

  @handle("stadium", "click")
  def stadium_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.column_panel_2.clear()
    self.column_panel_2.add_component(self.stadium_form)

  @handle("spieler", "click")
  def spieler_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.column_panel_2.clear()
    self.column_panel_2.add_component(self.spieler_form)

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.coloum_panel_2.clear()
    self.column_panel_2.add_component(self.wettbewerb_form)
