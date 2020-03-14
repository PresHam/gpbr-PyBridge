# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ClearSaleRequest(object):

    """Implementation of the 'ClearSaleRequest' model.

    TODO: type model description here.

    Attributes:
        custom_sla (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "custom_sla":'custom_sla'
    }

    def __init__(self,
                 custom_sla=None):
        """Constructor for the ClearSaleRequest class"""

        # Initialize members of the class
        self.custom_sla = custom_sla


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
        custom_sla = dictionary.get('custom_sla')

        # Return an object of this model
        return cls(custom_sla)


