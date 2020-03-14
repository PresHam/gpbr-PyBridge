# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.get_price_bracket_response

class GetPricingSchemeResponse(object):

    """Implementation of the 'GetPricingSchemeResponse' model.

    Response object for getting a pricing scheme

    Attributes:
        price (int): TODO: type description here.
        scheme_type (string): TODO: type description here.
        price_brackets (list of GetPriceBracketResponse): TODO: type
            description here.
        minimum_price (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "price":'price',
        "scheme_type":'scheme_type',
        "price_brackets":'price_brackets',
        "minimum_price":'minimum_price'
    }

    def __init__(self,
                 price=None,
                 scheme_type=None,
                 price_brackets=None,
                 minimum_price=None):
        """Constructor for the GetPricingSchemeResponse class"""

        # Initialize members of the class
        self.price = price
        self.scheme_type = scheme_type
        self.price_brackets = price_brackets
        self.minimum_price = minimum_price


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
        price = dictionary.get('price')
        scheme_type = dictionary.get('scheme_type')
        price_brackets = None
        if dictionary.get('price_brackets') != None:
            price_brackets = list()
            for structure in dictionary.get('price_brackets'):
                price_brackets.append(mundiapi.models.get_price_bracket_response.GetPriceBracketResponse.from_dictionary(structure))
        minimum_price = dictionary.get('minimum_price')

        # Return an object of this model
        return cls(price,
                   scheme_type,
                   price_brackets,
                   minimum_price)


