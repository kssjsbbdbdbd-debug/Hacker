from kivy.app import App
from kivy.uix.webview import WebView

class OceanGramApp(App):
    def build(self):
        # Ссылка на твой OceanGram (Tiiny)
        url = "https://blue-helli-20.tiiny.site" 
        return WebView(url=url)

if __name__ == '__main__':
    OceanGramApp().run()
