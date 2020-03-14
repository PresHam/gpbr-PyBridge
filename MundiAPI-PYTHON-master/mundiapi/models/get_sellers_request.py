# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class GetSellersRequest(object):

    """Implementation of the 'GetSellersRequest' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        document (string): TODO: type description here.
        code (string): TODO: type description here.
        status (string): TODO: type description here.
        mtype (string): TODO: type description here.
        created_since (string): TODO: type description here.
        created_until (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "document":'document',
        "code":'code',
        "status":'status',
        "mtype":'type',
        "created_since":'created_Since',
        "created_until":'created_Until'
    }

    def __init__(self,
                 name=None,
                 document=None,
                 code=None,
                 status=None,
                 mtype=None,
                 created_since=None,
                 created_until=None):
        """Constructor for the GetSellersRequest class"""

        # Initialize members of the class
        self.name = name
        self.document = document
        self.code = code
        self.status = status
        self.mtype = mtype
        self.created_since = created_since
        self.created_until = created_until


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
        name = dictionary.get('name')
        document = dictionary.get('document')
        code = dictionary.get('code')
        status = dictionary.get('status')
        mtype = dictionary.get('type')
        created_since = dictionary.get('created_Since')
        created_until = dictionary.get('created_Until')

        # Return an object of this model
        return cls(name,
                   document,
                   code,
                   status,
                   mtype,
                   created_since,
                   created_until)


