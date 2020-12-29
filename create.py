class WebView(QWebEngineView):
	def __init__(self, parent):
		super().__init__(parent)
	def createWindow(self, webWindowType):
		return main_demo.browser