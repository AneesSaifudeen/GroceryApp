from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.label import Label

items = [
    {"text": "Egg", "selected": 'normal', "input_data": "0"},
    {"text": "Rice", "selected": 'normal', "input_data": "0"},
    {"text": "Wheat", "selected": 'normal', "input_data": "0"},
    {"text": "Jaggery", "selected": 'normal', "input_data": "0"},
    {"text": "Sugar", "selected": 'normal', "input_data": "0"},
    {"text": "Maida", "selected": 'normal', "input_data": "0"},
    {"text": "Potato", "selected": 'normal', "input_data": "0"},
    {"text": "Cabbage", "selected": 'normal', "input_data": "0"},
    {"text": "Cauliflower", "selected": 'normal', "input_data": "0"},
    {"text": "Ghee", "selected": 'normal', "input_data": "0"},
    {"text": "Groundnut Oil", "selected": 'normal', "input_data": "0"},
    {"text": "Coconut", "selected": 'normal', "input_data": "0"},
    {"text": "Peas", "selected": 'normal', "input_data": "0"},
    {"text": "Chillies", "selected": 'normal', "input_data": "0"},
    {"text": "Ketchup", "selected": 'normal', "input_data": "0"},
    {"text": "Jam", "selected": 'normal', "input_data": "0"},
    {"text": "Rice FLour", "selected": 'normal', "input_data": "0"},
    {"text": "Cumin", "selected": 'normal', "input_data": "0"},
]


class MenuScreen(Screen):
    pass


class MyViewClass(RecycleDataViewBehavior, BoxLayout):
    text = StringProperty("")
    text_input = StringProperty("")
    index = None

    def set_state(self, state, app):
        app.root.get_screen('game').container.data[self.index]['selected'] = state

    def set_input(self, text, app):
        app.root.get_screen('game').container.data[self.index]['input_data'] = text

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(MyViewClass, self).refresh_view_attrs(rv, index, data)


class MyRecycleView(RecycleView):
    data = items


class SettingsScreen(Screen):
    container = ObjectProperty(None)


class SelectedItems(Screen):
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SelectedItems, self).__init__(**kwargs)
        print("init is called")
        Clock.schedule_once(self.setup_scroll_view, 1)

    def setup_scroll_view(self, dt):
        print("setup_scroll_view is called")
        self.container.bind(minimum_height=self.container.setter('height'))
        self.add_text_inputs()

    def add_text_inputs(self):
        print("add_text_inputs is called")
        self.container.clear_widgets()
        for item in self.manager.get_screen('game').container.data:
            if item['selected'] == 'down':
                self.container.add_widget(
                    Label(text=item['text'], font_name="Calibri", font_size=20, size_hint_y=None, height=50))
                self.container.add_widget(
                    Label(text=item['input_data'], font_name="Calibri", font_size=20, size_hint_y=None, height=50))


class ScreenManagement(ScreenManager):
    pass


class MyApp(App):

    def build(self):
        return ScreenManagement()


MyApp().run()
