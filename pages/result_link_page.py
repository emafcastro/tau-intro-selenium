class DuckDuckGoResultLinkPage:

    def __init__(self, browser):
        self.browser = browser
    
    def title(self):
        return self.browser.title