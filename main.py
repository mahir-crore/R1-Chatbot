import pyautogui
import time
import pyperclip
from openai import OpenAI




client = OpenAI(
  api_key="<Your Key Here>",
)

def is_last_message_from_sender(chat_log, sender_name="myself"):
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False
    
    

    #  Click on the Browser  icon at coordinates (653,743)
pyautogui.click(653,743)
time.sleep(1)  
while True:
    time.sleep(5)
#    Drag the mouse from (507,145) to (521,676) and  select the text
    pyautogui.moveTo(507,145)
    pyautogui.dragTo(521,676, duration=2.0, button='left')

   
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2) 
    pyautogui.click(921,367) #close selecting 

    # Retrieve the text from the clipboard 
    chat_history = pyperclip.paste()

    
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named Manjeet  who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Rohan Das: "},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

    #    Click at msg section   (614,696)
        pyautogui.click(614,696)
        time.sleep(1) 

       
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  

        # Step 7: Press Enter
        pyautogui.press('enter')