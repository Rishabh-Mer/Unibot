import requests

def SendOtp(mobileNumber, otp):
    url = 'https://apps.sandeshlive.com/API/WebSMS/Http/v1.0a/index.php?userid=1190&password=YaGpo7LdXOt5wiDA&sender=UNIVSE&to={0}&message=Dear Student/Parent, OTP is {1} - UNIVSE&reqid=1&format=text'.format(mobileNumber, otp)
    requests.get(url)
