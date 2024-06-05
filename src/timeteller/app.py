"""
The application for telling time
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import pytz
import datetime


class TimeTeller(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        location_label = toga.Label("Your location: ", style=Pack(padding=(0, 5)))
        self.location_input = toga.TextInput(style=Pack(flex=1))
        location_box = toga.Box(style=Pack(direction=ROW, padding=5))
        location_box.add(location_label)
        location_box.add(self.location_input)

        button = toga.Button("Tell Me Time!", on_press=self.tell_time, style=Pack(padding=5))
        main_box.add(location_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def tell_time(self, widget):
        location = self.location_input.value
        location_dict = {"上海": "Asia/Shanghai",
                         "Shanghai": "Asia/Shanghai",
                         "shanghai": "Asia/Shanghai",
                         "sh": "Asia/Shanghai",
                         "SH": "Asia/Shanghai",
                         "东京": "Asia/Tokyo",
                         "Tokyo": "Asia/Tokyo",
                         "tokyo": "Asia/Tokyo",
                         "伦敦": "Europe/London",
                         "London": "Europe/London",
                         "london": "Europe/London",
                         "纽约": "America/New_York",
                         "New York": "America/New_York",
                         "new york": "America/New_York",
                         "NY": "America/New_York"}
        loc = location_dict.get(location, "Asia/Shanghai")
        self.main_window.info_dialog(
            location, datetime.datetime.now(tz=pytz.timezone(loc)).strftime("%Y-%m-%d %H:%M:%S %A")
        )


def main():
    return TimeTeller()
