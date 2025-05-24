import datetime
import ctypes

def daily_greeting():
    hour = datetime.datetime.now().hour

    if 5 <= hour <= 11:
        return "🌞 Good Morning and enjoy your summer break! Enjoy your coffees if you do have one."
    if 11 < hour < 18:
        return "🌤 Good Afternoon! Please spend some time outside if you need to! I also care about your health rather than just some business."
    if 18 <= hour < 24:
        return "🌙 Good evening! Enjoy your solitude whilst you can! Most people don’t even know how to begin sitting still."
    if 0 <= hour < 5:
        return "🌃 Late night owl? Very interesting! Enjoy whatever the hell you want to! But please have some limits, health is the most important factor!"
    return "❓ Time is confusing. Check system clock."

message = daily_greeting()
ctypes.windll.user32.MessageBoxW(0, message, "👋 Daily Greeter", 0)