from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation

class EMIApp(App):
    def build(self):
        self.title = 'EMI Calculator'
        
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Header
        with self.layout.canvas.before:
            Color(0, 0.7, 1, 1)  # light blue
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)
        
        self.header = Label(text='EMI Calculator', size_hint=(1, 0.2))
        self.layout.add_widget(self.header)
        
        # Loan Amount
        self.loan_amount_label = Label(text='Loan Amount:', size_hint=(1, 0.2))
        self.loan_amount_input = TextInput(multiline=False, size_hint=(1, 0.2))
        self.layout.add_widget(self.loan_amount_label)
        self.layout.add_widget(self.loan_amount_input)
        
        # Interest Rate
        self.interest_rate_label = Label(text='Interest Rate (%):', size_hint=(1, 0.2))
        self.interest_rate_input = TextInput(multiline=False, size_hint=(1, 0.2))
        self.layout.add_widget(self.interest_rate_label)
        self.layout.add_widget(self.interest_rate_input)
        
        # Loan Term
        self.loan_term_label = Label(text='Loan Term (months):', size_hint=(1, 0.2))
        self.loan_term_input = TextInput(multiline=False, size_hint=(1, 0.2))
        self.layout.add_widget(self.loan_term_label)
        self.layout.add_widget(self.loan_term_input)
        
        # Calculate Button
        self.calculate_button = Button(text='Calculate EMI', size_hint=(1, 0.2))
        self.calculate_button.bind(on_press=self.calculate_emi)
        self.layout.add_widget(self.calculate_button)
        
        # EMI Result
        self.emi_label = Label(text='', size_hint=(1, 0.2))
        self.layout.add_widget(self.emi_label)
        
        return self.layout
    
    def calculate_emi(self, instance):
        try:
            # Get input values
            P = float(self.loan_amount_input.text)
            r = float(self.interest_rate_input.text) / 100 / 12
            n = int(self.loan_term_input.text)
            
            # Calculate EMI
            EMI = P * r * ((1 + r) ** n) / (((1 + r) ** n) - 1)
            
            # Display EMI
            self.emi_label.text = f'EMI: {EMI:.2f}'
            
            # Animation
            anim = Animation(color=(0, 1, 0, 1)) + Animation(color=(1, 1, 1, 1))
            anim.start(self.emi_label)
            
        except Exception as e:
            self.emi_label.text = 'Error: Invalid Input'
            anim = Animation(color=(1, 0, 0, 1)) + Animation(color=(1, 1, 1, 1))
            anim.start(self.emi_label)

if __name__ == '__main__':
    EMIApp().run()


