from twilio.rest import Client

def mobile_phone():
    account_sid='#############account Apikey##############'
    auth_token ='#############author apiket###############'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                           twiml='<Response><Say>hello soma i am from bulma team</Say></Response>',
                           to='##########mobile number############',
                           from_='############twilio number##########'
                           )

    print(call)
