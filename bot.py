import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="Enter your API key"
)

# Pause to give you time to switch to the desired window
# time.sleep(2)

def is_last_message_from_sender(chat_log, sender_name="Enter contact name"):
    # Split the entire chat into lines
    messages = chat_log.strip().split("/2025]")[-1]

    if sender_name in messages:
        return True
    return False

  

    # Step 1: Click on the chrome icon at (1213, 1051)
pyautogui.click(1213, 1051)
time.sleep(1)  # Wait for app or window to open

while True:


    # Step 2: Click and drag to select text from (700, 252) to (1861, 928)
    pyautogui.moveTo(679, 238)
    pyautogui.dragTo(1860, 931, duration=1.0, button='left')  # drag for 1 second

    # Step 3: Copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(1760, 901)

    # Step 4: Read the clipboard contents into a variable
    chat_History = pyperclip.paste()

    # Output the copied text
    # print("Copied Text:")
    print(chat_History)

    if is_last_message_from_sender(chat_History):

        completion = client.chat.completions.create(
            model = "deepseek/deepseek-chat-v3-0324:free",
            messages=[
                {"role": "system", "content": "You are a person named kkk who speaks hindi as well english. You are from India and is a coder. you analyze chat history and respond like kkk. Out put should be the next chat response (text message only)"},
                {"role": "user", "content": chat_History}
            ]
        )

        response = completion.choices[0].message.content

        pyperclip.copy(response)



        pyautogui.click(1172, 971)
        time.sleep(1)

        # Step 2: Paste the text (from clipboard)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # Step 3: Press Enter
        pyautogui.press('enter')
