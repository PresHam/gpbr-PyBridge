# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateCheckoutBankTransferRequest(object):

    """Implementation of the 'CreateCheckoutBankTransferRequest' model.

    Checkout bank transfer payment request

    Attributes:
        bank (list of string): Bank
        retries (int): Number of retries for processing

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bank":'bank',
        "retries":'retries'
    }

    def __init__(self,
                 bank=None,
                 retries=None):
        """Constructor for the CreateCheckoutBankTransferRequest class"""

        # Initialize members of the class
        self.bank = bank
        self.retries = retries


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
        bank = dictionary.get('bank')
        retries = dictionary.get('retries')

        # Return an object of this model
        return cls(bank,
                   retries)


