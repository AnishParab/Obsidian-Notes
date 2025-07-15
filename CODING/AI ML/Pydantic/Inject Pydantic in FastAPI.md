``` python
from fastapi import Fastapi, Depends
from pydantic import BaseModel, EmailStr # type: ignore

app = Fastapi()

class UserSignup(BaseModel):
	username: str
	email: EmailStr
	password: str

class Settings(BaseModel):
	app_name: str = "Chai App"
	admin_email: str = "admin@email.com"

# Use Settings as a dependency injection
def get_settings():
	return Settings()
# This will be needed when you make a custom route /settings

@app.post('/signup')
def signup(user: UserSignup):
	return {'message': f'User {user.username} signed up successfully'}

# Create dependency injection
@app.get('/settings')
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
	return settings
```

---
