import os
import pygame
from pyfiglet import Figlet
import sys
# ENG
voice1_en = 'en-IN-NeerjaExpressiveNeural'
voice2_en = 'en-US-AndrewNeural'
eng = {"voice1_en" : 'en-IN-NeerjaExpressiveNeural',"voice2_en" : 'en-US-AndrewNeural'}
voice3_e = 'en-US-AnaNeural'  # KIDS VOICE
voice4_e = 'en-US-SteffanNeural'
voice5_e = 'en-US-AriaNeural'
voice6_e = 'en-US-AvaNeural'
voice7_e = 'en-US-BrianNeural'
voice8_e = 'en-US-ChristopherNeural'
voice9_e = 'en-US-EmmaNeural'
voice10_e = 'en-US-EricNeural'
voice11_e = 'en-US-GuyNeural'
voice12_e = 'en-US-JennyNeural'
voice13_e = 'en-US-MichelleNeural'
voice14_e = 'en-US-RogerNeural'

# HINDI
voice2_hi = 'hi-IN-MadhurNeural'
voice1_hi = 'hi-IN-SwaraNeural'
hi = {"voice2_hi" : 'hi-IN-MadhurNeural',"voice1_hi" : 'hi-IN-SwaraNeural'}

# MALAYALAM
voice1_ml = 'ml-IN-SobhanaNeural'
voice2_ml = 'ml-IN-MidhunNeural'
ml = {"voice1_ml" : 'ml-IN-SobhanaNeural',"voice2_ml" : 'ml-IN-MidhunNeural'}

#KANADA
voice2_kn = 'kn-IN-GaganNeural'
voice1_kn = 'kn-IN-SapnaNeural'
kn = {"voice2_kn" : 'kn-IN-GaganNeural',"voice1_kn" : 'kn-IN-SapnaNeural'}

#TAMIL
voice1_tl = 'ta-IN-PallaviNeural'
voice2_tl = 'ta-IN-ValluvarNeural'
tl ={"voice1_tl" : 'ta-IN-PallaviNeural',"voice2_tl" : 'ta-IN-ValluvarNeural'}

#BANGLA
voice2_bl = 'bn-IN-BashkarNeural'
voice1_bl = 'bn-IN-TanishaaNeural'
bl = {"voice2_bl" : 'bn-IN-BashkarNeural',"voice1_bl" : 'bn-IN-TanishaaNeural'}

#GUJARATI
voice1_gu = 'gu-IN-DhwaniNeural'
voice2_gu = 'gu-IN-NiranjanNeural'
gu = {"voice1_gu" : 'gu-IN-DhwaniNeural',"voice2_gu" : 'gu-IN-NiranjanNeural'}

#MARATHI
voice1_mr = 'mr-IN-AarohiNeural'
voice2_mr = 'mr-IN-ManoharNeural'
mr = {"voice1_mr" : 'mr-IN-AarohiNeural',"voice2_mr" : 'mr-IN-ManoharNeural'}

#URDU
voice2_ur = 'ur-IN-SalmanNeural'
voice1_ur = 'ur-PK-UzmaNeural'
ur = {"voice2_ur" : 'ur-IN-SalmanNeural',"voice1_ur" : 'ur-PK-UzmaNeural'}

ln_set = {1:"en",2:"hi",3:"ur",4:"mr",5:"bl",6:"gu",7:"tl",8:"kn",9:"ml"}

f = Figlet(font='slant')
print(f.renderText('EdgeTTS - creator'))
print("\nNOTE : INTERNET IS REQUIRED!")
print("SUGGESTION : PLEASE USE THE NATIVE SCRIPT OF LANGUAGE EG. DEVNAGRI FOR HINDI")
print("\nGreetings! User.\n")
def speak(data,lang):
    
    command = f'edge-tts --voice "{lang}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        print("Audio saved as 'data.mp3' -- Thank you edge-tts :)\n\n")
def cmd():
    while True:
        
        
        print("Select Menu >>")
        print('1. Start')
        print('2. Credits')
        print('3. Exit')
        
        cmd1 = input(">>")

        if cmd1 == "1":
            print("\n\nWhich Language do you want ?")
            print("1. English")
            print("2. Hindi")
            print("3. Urdu")
            print("4. Marathi")
            print("5. Bangla")
            print("6. Gujarati")
            print("7. Tamil")
            print("8. Kanada")
            print("9. Malayalam")
            ln = input(">>")

            def gen():
                gender = input("Gender [M/F] >>")
                genx = 0
                if gender == "M":
                    genx = 2
                elif gender == "F":
                    genx = 1
                else:
                    print("Invalid Please Re-Try")
                    cmd()
                    
                return genx
            if ln == "1":
                gender = gen()
                data = input("\nEnter your data >>")
                lang = f"voice{gender}_en"
                speak(data,eng[lang])
                
            elif ln == "2":
                gender = gen()
                data = input("\nEnter your data >>")
                lang = f"voice{gender}_hi"
                speak(data,hi[lang])
                
            elif ln == "3":
                gender = gen()
                print(gender)
                data = input("\nEnter your data >>")
                lang = f"voice{gender}_ur"
                speak(data,ur[lang])
                
            elif ln == "4":
                gender = gen()
                data = input("\nEnter your data >>")
                lang = f"voice{gender}_mr"
                speak(data,mr[lang])
                
            elif ln == "5":
                gender = gen()
                data = input("\nEnter your data >>")
                lang = f"voice{gender}_bl"
                speak(data,bl[lang])
                
            elif ln == "6":
                gender = gen()
                data = input("\nEnter your data >>")
                lang = f"voice{gender}_gu"
                speak(data,gu[lang])
                
            elif ln == "7":
                gender = gen()
                data = input("\nEnter your data >>")
                lang = f"voice{gender}_tl"
                speak(data,tl[lang])
                
            elif ln == "8":
                gender = gen()
                data = input("\nEnter your data >>")
                lang = f"voice{gender}_kn"
                speak(data,kn[lang])
                
            elif ln == "9":
                gender = gen()
                data = input("\nEnter your data >>")
                lang = f"voice{gender}_ml"
                speak(data,ml[lang])
                
                
                
                    

        elif cmd1 == "2":
            print('\n\nProgram Developer : Anshul Wycliffe')
            print("TTS Provider : Microsoft Edge's TTS")
            print("Media Player : Pygame\n\n")

        elif cmd1 == "3":
            sys.exit()

        



#speak("My name is Anshul Wycliffe, मेरा नाम अंशुल वाईक्लिफ है") # HINDI
        
#speak("My name is Anshul Wycliffe,എൻ്റെ പേര് അൻഷുൽ വൈക്ലിഫ്") # MALAYALAM
        
#speak("My name is Anshul Wycliffe,ನನ್ನ ಹೆಸರು ಅನ್ಶುಲ್ ವೈಕ್ಲಿಫ್") # KANADA
        
#speak("My name is Anshul Wycliffe,আমার নাম আনশুল উইক্লিফ") # BANGLA
        
#speak("My name is Anshul Wycliffe,મારું નામ અંશુલ વાઈક્લિફ છે") #GUJARATI
        
#speak("My name is Anshul Wycliffe,माझे नाव अंशुल वायक्लिफ आहे") #MARATHI
        
#speak("My name is Anshul Wycliffe,என் பெயர் அன்ஷுல் விக்லிஃப்") #TAMIL
        
#speak("My name is Anshul Wycliffe,میرا نام انشول وائکلف ہے۔") #URDU
        
#speak("pygame 2.5.2 (SDL 2.28.3, Python 3.12.2),Hello from the pygame community") # ENGLISH

cmd()
        
