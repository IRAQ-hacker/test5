import os
import telebot
import youtube_dl

bot = telebot.TeleBot("token")


@bot.message_handler(commands=['start'])
def shoot(message):
  bot.send_message(message.chat.id, "Send your link video")


@bot.message_handler()
def run(message):

  bot.send_message(message.chat.id, "Please wait...")
    
  video_info = youtube_dl.YoutubeDL().extract_info(
      url = message.text, download=False
  )
  filename = f"{video_info['title']}.mp3"
  options={
      'format':'bestaudio/best',
      'keepvideo':False,
      'outtmpl':filename,
  }

  with youtube_dl.YoutubeDL(options) as ydl:
      ydl.download([video_info['webpage_url']])

  print("Download complete... {}".format(filename))
  bot.send_audio(message.chat.id, audio=open(filename, 'rb'))

bot.polling()
