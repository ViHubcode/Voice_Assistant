import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import requests
import yfinance as yf

netflix = yf.Ticker('NFLX')
print(netflix.info)