# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.get_gateway_error_response

class GetGatewayResponseResponse(object):

    """Implementation of the 'GetGatewayResponseResponse' model.

    The Transaction Gateway Response

    Attributes:
        code (string): The error code
        errors (list of GetGatewayErrorResponse): The gateway response errors
            list

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code":'code',
        "errors":'errors'
    }

    def __init__(self,
                 code=None,
                 errors=None):
        """Constructor for the GetGatewayResponseResponse class"""

        # Initialize members of the class
        self.code = code
        self.errors = errors


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
        code = dictionary.get('code')
        errors = None
        if dictionary.get('errors') != None:
            errors = list()
            for structure in dictionary.get('errors'):
                errors.append(mundiapi.models.get_gateway_error_response.GetGatewayErrorResponse.from_dictionary(structure))

        # Return an object of this model
        return cls(code,
                   errors)


