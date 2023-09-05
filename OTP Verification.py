import random

def generate_OTP():
    """Generate a random 6-digit OTP"""
    digits = "0123456789"
    otp = "".join(random.sample(digits,6))
    
    return otp

def send_OTP(phone_number, otp):
    """Simulate sending OTP to a phone number (print it)"""
    print(f"OTP sent to {phone_number}: {otp}")

def verification(entered_otp, otp):
    """Verify the entered OTP"""
    return entered_otp == otp

# Simulate a user entering their phone number
phone_number = input("\nEnter your phone number: ")

# Generate and send OTP
otp = generate_OTP()
send_OTP(phone_number, otp)

# Simulate a user entering the OTP for verification
entered_otp = input("\nEnter the OTP you received: ")

# Verify the OTP
if verification(entered_otp, otp):
    print("OTP verification successful!\n\n")
else:
    print("\nOTP verification failed,\nRetry\n\n")
    