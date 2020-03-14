# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.get_address_response

class GetSellerResponse(object):

    """Implementation of the 'GetSellerResponse' model.

    TODO: type model description here.

    Attributes:
        id (string): Identification
        name (string): TODO: type description here.
        code (string): TODO: type description here.
        document (string): TODO: type description here.
        description (string): Description
        status (string): Status
        created_at (string): Creation date
        updated_at (string): Updated date
        address (GetAddressResponse): Address
        metadata (dict<object, string>): Metadata
        deleted_at (string): Deleted date

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "code":'code',
        "document":'document',
        "description":'description',
        "status":'Status',
        "created_at":'CreatedAt',
        "updated_at":'UpdatedAt',
        "address":'Address',
        "metadata":'Metadata',
        "deleted_at":'DeletedAt'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 code=None,
                 document=None,
                 description=None,
                 status=None,
                 created_at=None,
                 updated_at=None,
                 address=None,
                 metadata=None,
                 deleted_at=None):
        """Constructor for the GetSellerResponse class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.code = code
        self.document = document
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.address = address
        self.metadata = metadata
        self.deleted_at = deleted_at


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
        id = dictionary.get('id')
        name = dictionary.get('name')
        code = dictionary.get('code')
        document = dictionary.get('document')
        description = dictionary.get('description')
        status = dictionary.get('Status')
        created_at = dictionary.get('CreatedAt')
        updated_at = dictionary.get('UpdatedAt')
        address = mundiapi.models.get_address_response.GetAddressResponse.from_dictionary(dictionary.get('Address')) if dictionary.get('Address') else None
        metadata = dictionary.get('Metadata')
        deleted_at = dictionary.get('DeletedAt')

        # Return an object of this model
        return cls(id,
                   name,
                   code,
                   document,
                   description,
                   status,
                   created_at,
                   updated_at,
                   address,
                   metadata,
                   deleted_at)


