# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.get_payment_authentication_response

class GetCheckoutDebitCardPaymentResponse(object):

    """Implementation of the 'GetCheckoutDebitCardPaymentResponse' model.

    TODO: type model description here.

    Attributes:
        statement_descriptor (string): Descrição na fatura
        authentication (GetPaymentAuthenticationResponse): Payment
            Authentication response object data

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "statement_descriptor":'statement_descriptor',
        "authentication":'authentication'
    }

    def __init__(self,
                 statement_descriptor=None,
                 authentication=None):
        """Constructor for the GetCheckoutDebitCardPaymentResponse class"""

        # Initialize members of the class
        self.statement_descriptor = statement_descriptor
        self.authentication = authentication


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
        statement_descriptor = dictionary.get('statement_descriptor')
        authentication = mundiapi.models.get_payment_authentication_response.GetPaymentAuthenticationResponse.from_dictionary(dictionary.get('authentication')) if dictionary.get('authentication') else None

        # Return an object of this model
        return cls(statement_descriptor,
                   authentication)


