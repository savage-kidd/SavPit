from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            size_hint=(0.9, 0.6),
                            check=True,
                            rows_num =10,
                            column_data=[
                                ("Id", dp(18)),
                                ("Food", dp(20)),
                                ("Calories", dp(20)),
                            ],
                            row_data=[
                                ("1", "Burger", "300"),
                                ("2", "Oats", "150"),
                                ("3", "Pizza", "90"),
                                ("4", "Fish", "200"),
                                ("5", "Muffin", "250"),
                                ("6", "Cake", "160"),
                                ("7", "Rice", "190"),
                                ("8", "Mince", "140"),
                                ("9", "Noodles", "50"),
                                ("10", "Fries", "100")
                            ]
                            )
        table.bind(on_check_press=self.check_press)
        table.bind(on_row_press=self.row_press)
        screen.add_widget(table)
        return screen

    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)

    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)


DemoApp().run()
