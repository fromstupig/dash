import socket
import uuid
import difflib
from datetime import datetime

import requests
from flask_sqlalchemy import get_debug_queries
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


class Utility(object):
    @staticmethod
    def uuid():
        return str(uuid.uuid4())

    @staticmethod
    def slug(name):
        return name.strip().lower().replace(' ', '').replace('-', '')

    @staticmethod
    def web_slug(text):
        """
        :param text: string need to slug
        :return: slug string
        """
        return text.strip().lower().replace(' ', '-')

    @staticmethod
    def dict2array(obj):
        """
        :param obj: python dictionary object
        :return: array with dict value
        """
        return list(map(lambda x: x[1], obj.items()))

    @staticmethod
    def strptime(time='00:00'):
        """
        :param time: python string with strict hour minute format (HH:MM)
        :return: datetime
        """
        return datetime.strptime(time, '%H:%M')

    @staticmethod
    def can_represents_int(s):
        """
        :param s: python string
        :return: true if string can represents as int else false
        """
        try:
            int(s or '')
            return True
        except (ValueError, TypeError):
            return False

    @staticmethod
    def first_or_none(l):
        """
        :param l: python list
        :return: first value of list or none as list empty
        """
        return next(iter(l) or [], None)

    @staticmethod
    def sql_log():
        info = get_debug_queries()
        for i in info:
            print('\n--------\n')
            print('Query: ', i.statement, i.parameters)
            print('Excute time: ', i.duration)
            print('\n--------\n')

    @staticmethod
    def get_attribute(obj, attribute, default_value=None):
        """
        Get attribute if object is class instance and value of key if object is dicts
        :param obj: object need to retrieve value
        :param attribute: name of attribute
        :param default_value: return default value if none
        :return: value of attribute
        """
        return obj.get(attribute, default_value) if isinstance(obj, dict) else getattr(obj, attribute, default_value)

    @staticmethod
    def only(source, *keys):
        """
        :param source: dictionary
        :param keys: list key need to get from source
        :return: new dictionary with new keys only
        """
        return {key: source[key] for key in keys if key in source}

    @staticmethod
    def safe_bool(value):
        """
        Convert value to boolean
        :param value: a value
        :return: true or false
        """
        if isinstance(value, bool):
            return value
        return True if str(value).lower() in ['yes', 'true', '1'] else False

    @staticmethod
    def is_valid_ipv4_address(address):
        """
        :param address: string ip address
        :return: true or false
        """
        try:
            socket.inet_pton(socket.AF_INET, address)
        except AttributeError:
            try:
                socket.inet_aton(address)
            except socket.error:
                return False
            return address.count('.') == 3
        except socket.error:
            return False

        return True

    @staticmethod
    def is_valid_ipv6_address(address):
        """
        :param address: string ip address
        :return: true or false
        """
        try:
            socket.inet_pton(socket.AF_INET6, address)
        except socket.error:
            return False
        return True

    @staticmethod
    def requests_retry_session(retries=3, back_off_factor=0.3, status_force_list=(500, 502, 504), session=None):
        """
        :param retries: total retries
        :param back_off_factor: A back-off factor to apply between attempts after the second try
        :param status_force_list: list of error status
        :param session: modified session
        :return: A Requests session
        """
        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=back_off_factor,
            status_forcelist=status_force_list,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        return session

    @staticmethod
    def calculate_string_sequence_match(keyword, result):
        """
        Calculate sequence matching ratio between two difference strings in range [0, 1] within 1 mean identical
        :param keyword: string 1
        :param result: string 2
        :return: matching ration as double value
        """
        if keyword and result:
            keyword = keyword.strip().lower()
            result = result.strip().lower()
            if keyword == result or keyword in result or result in keyword:
                return 1

            return difflib.SequenceMatcher(None, keyword, result).ratio()

        return 0
