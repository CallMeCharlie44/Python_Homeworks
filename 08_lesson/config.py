import requests

class APIconfig:
    def __init__(self):
        self.url = "https://ru.yougile.com"
        self.token = self.get_token()
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
    
    
    def get_token(self):
        payload = {
        "login" : "Мой логин",
        "password" : "Мой пароль",
        "companyId" : "Айди компании"   
        }
        respons = requests.post(self.url+"/api-v2/auth/keys/get", json=payload )
        return respons.json()[0]["key"]
    
    
    def create_poject(self, title):
        payload = {
            "title": title
        }
        return requests.post(self.url+"/api-v2/projects", headers=self.headers, json=payload)
    
    def get_poject(self, id):
        
        return requests.get(self.url+f"/api-v2/projects/{id}", headers=self.headers)
    
    def update_title_project(self, title, id):
        return requests.put(f"{self.url}/api-v2/projects/{id}", json= {"title" : title}, headers=self.headers)
    

        
    




        



