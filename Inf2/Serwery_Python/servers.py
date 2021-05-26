# <Łukasz> <Orpik>, <302892>

#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict
from abc import ABC, abstractmethod
from copy import deepcopy
from re import fullmatch


class Product:
    # doklej metody z konspektu
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __hash__(self):
        return hash((self.name, self.price))

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price


class Server(ABC):
    n_max_returned_entries = 4

    def __init__(self):
        super().__init__()

    @abstractmethod
    def add(self, list_of_product: List[Product] = None):
        pass

    @abstractmethod
    def remove(self, list_of_product: List[Product] = None):
        pass

    @abstractmethod
    def get_product_by_name(self, n_letters: int) -> List[Product]:
        pass

    def get_entries(self, n_letters: int) -> Optional[List[Product]]:
        list_of_matching_products = self.get_product_by_name(n_letters)

        if len(list_of_matching_products) > self.n_max_returned_entries:
            raise TooManyProductsFoundError(self, len(list_of_matching_products))

        return sorted(list_of_matching_products)


class ServersError(Exception):
    def __init__(self, server: Server, msg=None):
        self.server = server
        if msg is None:
            msg = "\nA servers error occured with server: {}".format(self.server)
            print('Check this bitch')
        super().__init__(msg)


class TooManyProductsFoundError(ServersError):
    def __init__(self, this, number_of_products_found):
        super().__init__(this, msg="\nToo many products were found = {}".format(number_of_products_found))
        self.number_of_products_found = number_of_products_found


class ListServer(Server):

    def __init__(self, list_of_product: List[Product] = None):
        super().__init__()
        if list_of_product:
            self.list_of_product = deepcopy(
                sorted(list(dict.fromkeys(list_of_product))))  # pozbywanie się duplikatow z listy produktow

    def add(self, list_of_product: List[Product] = None):
        if list_of_product:
            self.list_of_product.extend(list_of_product)

    def remove(self, list_of_product: List[Product] = None):
        if list_of_product:
            for elem in list_of_product:
                try:
                    self.list_of_product.remove(elem)
                except ValueError:
                    print('Product {} ordered to be removed have not been found on the list'.format(elem))

    def get_product_by_name(self, n_letters: int) -> List[Product]:
        list_of_matching_products = [element for element in self.list_of_product if
                                     fullmatch('^[a-zA-Z]{{{n}}}\\d{{2,3}}$'.format(n=n_letters), element.name,
                                               flags=0)]

        return sorted(list_of_matching_products)


class MapServer(Server):
    def __init__(self, list_of_product: List[Product] = None):
        super().__init__()
        if list_of_product:
            self.dict_of_product = {element.name: element.price for element in sorted(list_of_product)}

    def get_product_by_name(self, n_letters: int) -> List[Product]:
        list_of_matching_products = [Product(name, price) for name, price in self.dict_of_product.items() if
                                     fullmatch('^[a-zA-Z]{{{n}}}\\d{{2,3}}$'.format(n=n_letters), name, flags=0)]

        return sorted(list_of_matching_products)

    def add(self, list_of_product: List[Product] = None):
        if list_of_product:
            self.dict_of_product.update({element.name: element.price for element in list_of_product})

    def remove(self, list_of_product: List[Product] = None):
        if list_of_product:
            for elem in list_of_product:
                try:
                    self.dict_of_product.pop(elem)
                except KeyError:
                    print('Product {} ordered to be removed have not been found in the dict'.format(elem))


class Client:
    def __init__(self, server: Server):
        self.server = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        try:
            list_of_products_found = self.server.get_entries(n_letters)
        except TooManyProductsFoundError:
            return None
        if list_of_products_found:
            return sum([elem.price for elem in list_of_products_found])
        else:
            return None


