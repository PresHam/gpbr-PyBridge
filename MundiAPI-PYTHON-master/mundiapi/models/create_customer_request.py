# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import mundiapi.models.create_address_request
import mundiapi.models.create_phones_request

class CreateCustomerRequest(object):

    """Implementation of the 'CreateCustomerRequest' model.

    Request for creating a new customer

    Attributes:
        name (string): Name
        email (string): Email
        document (string): Document number. Only numbers, no special
            characters.
        mtype (string): Person type. Can be either 'individual' or 'company'
        address (CreateAddressRequest): The customer's address
        metadata (dict<object, string>): Metadata
        phones (CreatePhonesRequest): TODO: type description here.
        code (string): Customer code
        gender (string): Customer Gender

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "email":'email',
        "document":'document',
        "mtype":'type',
        "address":'address',
        "metadata":'metadata',
        "phones":'phones',
        "code":'code',
        "gender":'gender'
    }

    def __init__(self,
                 name=None,
                 email=None,
                 document=None,
                 mtype=None,
                 address=None,
                 metadata=None,
                 phones=None,
                 code=None,
                 gender=None):
        """Constructor for the CreateCustomerRequest class"""

        # Initialize members of the class
        self.name = name
        self.email = email
        self.document = document
        self.mtype = mtype
        self.address = address
        self.metadata = metadata
        self.phones = phones
        self.code = code
        self.gender = gender


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
        email = dictionary.get('email')
        document = dictionary.get('document')
        mtype = dictionary.get('type')
        address = mundiapi.models.create_address_request.CreateAddressRequest.from_dictionary(dictionary.get('address')) if dictionary.get('address') else None
        metadata = dictionary.get('metadata')
        phones = mundiapi.models.create_phones_request.CreatePhonesRequest.from_dictionary(dictionary.get('phones')) if dictionary.get('phones') else None
        code = dictionary.get('code')
        gender = dictionary.get('gender')

        # Return an object of this model
        return cls(name,
                   email,
                   document,
                   mtype,
                   address,
                   metadata,
                   phones,
                   code,
                   gender)


