# coding: utf-8

from pprint import pformat
from six import iteritems
import re


class User(object):

    def __init__(self, name=None, fine=None):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'fine': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'fine': 'fine'
        }

        self._name = name
        self._fine = fine


    @property
    def name(self):
        """
        Gets the name of this User.


        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this User.


        :param name: The name of this User.
        :type: str
        """

        self._name = name

    @property
    def fine(self):
        """
        Gets the fine of this User.


        :return: The fine of this User.
        :rtype: bool
        """
        return self._fine

    @fine.setter
    def fine(self, fine):
        """
        Sets the fine of this User.


        :param fine: The fine of this User.
        :type: bool
        """

        self._fine = fine

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
