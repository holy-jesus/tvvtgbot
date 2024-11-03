## 🤖 Так вам видно телеграм бот

Телеграм бот для демонстрации работы библиотеки TakVamVidno

### Запуск 

```
python -m venv ./venv/

# Для Linux
source ./venv/bin/activate
# Для Windows
./venv/Scripts/activate.bat
 
pip install -r requirements.txt

# Для Linux
export OPENAI_API_KEY="TOKEN"
export telegram_token="TG_TOKEN"
# Для Windows
$env:OPENAI_API_KEY="TOKEN"
$env:telegram_token="TG_TOKEN"
 
python main.py
```
