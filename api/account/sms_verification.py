from twilio.rest import Client

# Twilio API credentials
TWILIO_ACCOUNT_SID = 'AC3820ca706ad0383fbec0555303204689'
TWILIO_AUTH_TOKEN = 'daac59c1f4df6b53871f291b919c2a6d'

# Verification Service SID
TWILIO_VERIFICATION_SID = 'VA2a796a4632d63bd59153f2d4bcb58b5e'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


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
