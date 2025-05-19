import time

def countdown(seconds):
    for remaining_time in range(seconds, 0, -1):
        mins, secs = divmod(remaining_time, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end="\r")
        time.sleep(1)

def password_check():
    correct_password = 'abc123'
    tries = 3
    lockout_time = 30

    while True:
        for attempt in range(tries):
            password = input("Enter a password: ")
            if password == correct_password:
                print("You entered the correct password.\nYou have been logged in.")
                return
            else:
                print(f"Invalid Password. Try {tries - attempt - 1} attempts left.")
        
        print(f"You have exceeded the maximum attempts. Logging you out for {lockout_time} seconds.")
        countdown(lockout_time)


password_check()
