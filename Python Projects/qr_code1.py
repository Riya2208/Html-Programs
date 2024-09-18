import qrcode as qr
img = qr.make('https://chatgpt.com/')
img.save("chat_Gpt.png")