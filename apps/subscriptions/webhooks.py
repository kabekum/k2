import stripe

def handle_payment_success(event):
    firm_id = event['data']['object']['metadata']['firm_id']
    # activate subscription
