from pyodide.http import pyfetch
import json

class Browser:
    def __init__(self):
        self.history = []
        self.cache = {}
    
    async def fetch_url(self, url):
        if url in self.cache:
            return self.cache[url]
            
        try:
            response = await pyfetch(url)
            content = await response.text()
            
            # Store in history
            self.history.append({
                'url': url,
                'timestamp': Date.now(),
                'status': response.status
            })
            
            # Cache successful responses
            if response.status == 200:
                self.cache[url] = content
                
            return content
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_history(self):
        return self.history
    
    def clear_cache(self):
        self.cache = {}
