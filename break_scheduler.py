import webbrowser,time # Impotring The Time , webbrowser Libraries
url = 'https://www.youtube.com' # URL to Open The Given Website To Take Break

print('\n WELCOME TO BREAK SCHEDULE REMINDER !! \n ') # WELCOME Message


while True: # While Loop To Repete Section Of Code n Number Of Times
    try:
        break_time = int(input('How No.Of Times You Need Break:\n')) # Try Block To Resume Program WithOut Any Error Message!!
    except:
        print('Sorry! it Must be A Integer \n') # Except Block To Run Program WithOut Interruption!!
        continue
    else:
        break  # Break Statement To End The While loop


while True:  # While Loop To Repete Section Of Code n Number Of Times
    try:
        n = float(input('Enter No.Of Hours after which break will be Scheduled : \n')) # Try Block To Resume Program WithOut Any Error Message!!
        n *= 3600 # As The Time is Calculated in Seconds To Convert Into Hours We Multiply 60 * 60
    except:
        print('Please Enter The No.of Hours \n') # Except Block To Run Program WithOut Interruption!!
        continue
    else:
        break # Break Statement To End The While loop


local_time  = 0 # Initial Time , Will be Added Later


while break_time > local_time: # While loop Runs Code Untill local_time is Equal To break_time

    time.sleep(n) # Keep Track of Time To Wait For "n" Hours
    webbrowser.open(url) # Will allow displaying Web-based documents to users
    local_time += 1 # Incrementing The value Of local_time By 1 Every Time
