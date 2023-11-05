import logging

import requests
from requests import HTTPError


class DealerService:
    def __init__(self):
        self.token = ''
        self.url = ''

    def init_app(self, app):
        self.token = app.config['DS_TOKEN']
        self.url = app.config['DS_URL']

    def get_vehicle_payment_by_deal(self, params: dict):
        deal_type = params['dealType']

        body = {
            'paymentParameters': {},
            'vehicleParameters': {}
        }

        body['paymentParameters']['dealType'] = deal_type
        body['vehicleParameters']['vin'] = params['vin']

        if deal_type == 'lease':
            body['paymentParameters']['upFrontDefinition'] = {
                'type': 'dueAtSigning'
            }
            body['paymentParameters']['upFrontDefinition']['amount'] = params['dueAtSigningAmount']
            body['paymentParameters']['mileage'] = params['mileage']

        if deal_type == 'loan':
            body['paymentParameters']['upFrontDefinition'] = {
                'type': 'down'
            }
            body['paymentParameters']['upFrontDefinition']['amount'] = params['downPayment']

        if 'term' in params:
            body['paymentParameters']['term'] = params['term']

        if 'buyerZipcode' in params:
            body['paymentParameters']['buyerZipcode'] = params['buyerZipcode']

        if 'creditTier' in params:
            body['paymentParameters']['creditTier'] = params['creditTier']

        if 'dealerZipcode' in params:
            body['paymentParameters']['dealerZipcode'] = params['dealerZipcode']

        if 'monthlyPayment' in params:
            body['paymentParameters']['monthlyPayment'] = params['monthlyPayment']

        if 'msrp' in params:
            body['vehicleParameters']['msrp'] = params['msrp']

        try:
            rv = requests.post(self.url, json=body, headers={
                "Content-Type": "application/json",
                "Authorization": "DS {}".format(self.token)
            })

            return rv.json()
        except HTTPError as err:
            raise err


dealer_service = DealerService()
