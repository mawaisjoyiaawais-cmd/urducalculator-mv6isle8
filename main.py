import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# ایپ کو ڈیسک ٹاپ پر جانچنے کے لیے ونڈو کا سائز مقرر کریں
Window.size = (350, 550)

# .kv کوڈ کو براہ راست پائتھن فائل میں لوڈ کریں
Builder.load_string('''
<CalculatorLayout>:
    display: display_label
    orientation: 'vertical'
    padding: 10
    spacing: 10
    canvas.before:
        Color:
            rgba: 0.1, 0.1, 0.1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        id: display_label
        text: "0"
        font_size: '48sp'
        size_hint: 1, 0.25
        halign: "right"
        valign: "middle"
        text_size: self.width - 20, self.height

    GridLayout:
        cols: 4
        spacing: 10
        size_hint: 1, 0.75

        # ------------ بٹنوں کی قطاریں ------------
        Button:
            text: "C"
            font_size: '24sp'
            on_press: root.clear_display()
            background_color: (0.9, 0.3, 0.3, 1)
        Button:
            text: "()"
            font_size: '24sp'
            on_press: root.handle_parentheses()
            background_color: (0.5, 0.5, 0.5, 1)
        Button:
            text: "DEL"
            font_size: '24sp'
            on_press: root.delete_last()
            background_color: (0.9, 0.5, 0.2, 1)
        Button:
            text: "/"
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.2, 0.6, 0.8, 1)

        Button:
            text: "7"
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.3, 0.3, 0.3, 1)
        Button:
            text: "8"
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.3, 0.3, 0.3, 1)
        Button:
            text: "9"
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.3, 0.3, 0.3, 1)
        Button:
            text: "*"
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.2, 0.6, 0.8, 1)

        Button:
            text: "4"
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.3, 0.3, 0.3, 1)
        Button:
            text: "5"
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.3, 0.3, 0.3, 1)
        Button:
            text: "6"
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.3, 0.3, 0.3, 1)
        Button:
            text: "-"
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.2, 0.6, 0.8, 1)

        Button:
            text: "1"
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.3, 0.3, 0.3, 1)
        Button:
            text: "2"
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.3, 0.3, 0.3, 1)
        Button:
            text: "3"
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.3, 0.3, 0.3, 1)
        Button:
            text: "+"
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.2, 0.6, 0.8, 1)

        Button:
            text: ""
            font_size: '24sp'
            background_color: (0.1, 0.1, 0.1, 1)
        Button:
            text: "0"
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.3, 0.3, 0.3, 1)
        Button:
            text: "."
            font_size: '24sp'
            on_press: root.add_to_expression(self.text)
            background_color: (0.5, 0.5, 0.5, 1)
        Button:
            text: "="
            font_size: '24sp'
            on_press: root.calculate_result()
            background_color: (0.2, 0.8, 0.2, 1)
''')

class CalculatorLayout(BoxLayout):
    display = ObjectProperty(None)
    expression = ""
    parentheses_open = False

    def add_to_expression(self, value):
        # اگر ڈسپلے پر '0' یا 'غلطی' ہے تو اسے صاف کریں
        if self.display.text == "0" and value not in "+-*/":
            self.expression = ""
            self.display.text = ""
        elif self.display.text == "غلطی":
            self.expression = ""
            self.display.text = ""

        self.expression += value
        self.display.text = self.expression

    def clear_display(self):
        self.expression = ""
        self.display.text = "0"
        self.parentheses_open = False

    def delete_last(self):
        if self.display.text == "غلطی" or self.display.text == "0":
            return

        if self.expression:
            last_char = self.expression[-1]
            if last_char == '(':
                self.parentheses_open = False
            elif last_char == ')':
                self.parentheses_open = True
            self.expression = self.expression[:-1]
            if not self.expression:
                self.display.text = "0"
            else:
                self.display.text = self.expression
        else:
            self.display.text = "0"

    def handle_parentheses(self):
        if self.display.text == "0" or self.display.text == "غلطی":
            self.expression = ""
            self.display.text = ""
            
        if not self.parentheses_open:
            self.expression += '('
            self.parentheses_open = True
        else:
            self.expression += ')'
            self.parentheses_open = False
        self.display.text = self.expression
                
    def calculate_result(self):
        if not self.expression:
            return
        try:
            # حفاظتی اقدام: صرف اجازت یافتہ حروف کا استعمال کریں
            safe_expression = "".join(c for c in self.expression if c in "0123456789.+-*/()")
            if not safe_expression:
                raise ValueError("Invalid Expression")

            # eval یہاں محفوظ ہے کیونکہ ان پٹ ہمارے بٹنوں سے کنٹرول ہوتا ہے
            result = str(eval(safe_expression))
            self.expression = result
            self.display.text = result
        except Exception as e:
            self.display.text = "غلطی" # غلطی کا پیغام
            self.expression = ""
            self.parentheses_open = False

class UrduCalculatorApp(App):
    def build(self):
        self.title = 'کیلکولیٹر'
        return CalculatorLayout()

if __name__ == '__main__':
    UrduCalculatorApp().run()
