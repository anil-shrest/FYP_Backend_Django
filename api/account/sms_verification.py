from twilio.rest import Client

# Twilio API credentials
TWILIO_ACCOUNT_SID = 'AC3820ca706ad0383fbec0555303204689'
TWILIO_AUTH_TOKEN = 'ac7900ce79bcecd6f1b8c3da62b3473e'

# Verification Service SID
TWILIO_VERIFICATION_SID = 'VA2a796a4632d63bd59153f2d4bcb58b5e'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# To authenticate user via SMS OTP before registration
def verifications(phone_number, via):
    return client.verify \
        .services(TWILIO_VERIFICATION_SID) \
        .verifications \
        .create(to=phone_number, channel=via)


def verification_checks(phone_number, token):
    return client.verify \
        .services(TWILIO_VERIFICATION_SID) \
        .verification_checks \
        .create(to=phone_number, code=token)
