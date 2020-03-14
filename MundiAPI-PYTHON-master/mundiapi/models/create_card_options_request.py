# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateCardOptionsRequest(object):

    """Implementation of the 'CreateCardOptionsRequest' model.

    Options for creating the card

    Attributes:
        verify_card (bool): Indicates if the card should be verified before
            creation. If true, executes an authorization before saving the
            card.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "verify_card":'verify_card'
    }

    def __init__(self,
                 verify_card=None):
        """Constructor for the CreateCardOptionsRequest class"""

        # Initialize members of the class
        self.verify_card = verify_card


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
        verify_card = dictionary.get('verify_card')

        # Return an object of this model
        return cls(verify_card)


