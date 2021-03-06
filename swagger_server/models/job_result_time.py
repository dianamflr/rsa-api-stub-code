# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class JobResultTime(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, creation: datetime=None, start: datetime=None, end: datetime=None):  # noqa: E501
        """JobResultTime - a model defined in Swagger

        :param creation: The creation of this JobResultTime.  # noqa: E501
        :type creation: datetime
        :param start: The start of this JobResultTime.  # noqa: E501
        :type start: datetime
        :param end: The end of this JobResultTime.  # noqa: E501
        :type end: datetime
        """
        self.swagger_types = {
            'creation': datetime,
            'start': datetime,
            'end': datetime
        }

        self.attribute_map = {
            'creation': 'creation',
            'start': 'start',
            'end': 'end'
        }
        self._creation = creation
        self._start = start
        self._end = end

    @classmethod
    def from_dict(cls, dikt) -> 'JobResultTime':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The jobResult_time of this JobResultTime.  # noqa: E501
        :rtype: JobResultTime
        """
        return util.deserialize_model(dikt, cls)

    @property
    def creation(self) -> datetime:
        """Gets the creation of this JobResultTime.

        The time at which the job was created in pending status  # noqa: E501

        :return: The creation of this JobResultTime.
        :rtype: datetime
        """
        return self._creation

    @creation.setter
    def creation(self, creation: datetime):
        """Sets the creation of this JobResultTime.

        The time at which the job was created in pending status  # noqa: E501

        :param creation: The creation of this JobResultTime.
        :type creation: datetime
        """
        if creation is None:
            raise ValueError("Invalid value for `creation`, must not be `None`")  # noqa: E501

        self._creation = creation

    @property
    def start(self) -> datetime:
        """Gets the start of this JobResultTime.

        The time at which the job entered `inprogress` status  # noqa: E501

        :return: The start of this JobResultTime.
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start: datetime):
        """Sets the start of this JobResultTime.

        The time at which the job entered `inprogress` status  # noqa: E501

        :param start: The start of this JobResultTime.
        :type start: datetime
        """

        self._start = start

    @property
    def end(self) -> datetime:
        """Gets the end of this JobResultTime.

        The time at which the job entered `completed` or `failed` status  # noqa: E501

        :return: The end of this JobResultTime.
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end: datetime):
        """Sets the end of this JobResultTime.

        The time at which the job entered `completed` or `failed` status  # noqa: E501

        :param end: The end of this JobResultTime.
        :type end: datetime
        """

        self._end = end
