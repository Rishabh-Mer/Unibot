import requests

def SendOtp(mobileNumber, otp):
    url = 'https://apps.sandeshlive.com/API/WebSMS/Http/v1.0a/index.php?userid=750&password=3Kq5m98PHAafxQ0N&sender=UniGrp&to={0}&message=OTP is {1}&reqid=1&format=text'.format(mobileNumber, otp)
    requests.get(url)
