# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.create_emv_data_decrypt_request
import mundiapi.models.create_card_payment_contactless_poi_request

class CreateEmvDecryptRequest(object):

    """Implementation of the 'CreateEmvDecryptRequest' model.

    TODO: type model description here.

    Attributes:
        icc_data (string): TODO: type description here.
        card_sequence_number (string): TODO: type description here.
        data (CreateEmvDataDecryptRequest): TODO: type description here.
        poi (CreateCardPaymentContactlessPOIRequest): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "icc_data":'icc_data',
        "card_sequence_number":'card_sequence_number',
        "data":'data',
        "poi":'poi'
    }

    def __init__(self,
                 icc_data=None,
                 card_sequence_number=None,
                 data=None,
                 poi=None):
        """Constructor for the CreateEmvDecryptRequest class"""

        # Initialize members of the class
        self.icc_data = icc_data
        self.card_sequence_number = card_sequence_number
        self.data = data
        self.poi = poi


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        icc_data = dictionary.get('icc_data')
        card_sequence_number = dictionary.get('card_sequence_number')
        data = mundiapi.models.create_emv_data_decrypt_request.CreateEmvDataDecryptRequest.from_dictionary(dictionary.get('data')) if dictionary.get('data') else None
        poi = mundiapi.models.create_card_payment_contactless_poi_request.CreateCardPaymentContactlessPOIRequest.from_dictionary(dictionary.get('poi')) if dictionary.get('poi') else None

        # Return an object of this model
        return cls(icc_data,
                   card_sequence_number,
                   data,
                   poi)


