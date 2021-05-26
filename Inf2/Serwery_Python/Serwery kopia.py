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


class Server(ABC):
    n_max_returned_entries = 2

    # get_product_by_name- to będziemy obslugiwac w get entries, to ma byc abstrakcyjne, filtracja oraz zwrot przefiltrowanej listy
    @abstractmethod
    def get_product_by_name(self, ) -> List[Product]:

    # zaimplementuj tu entries
    @abstractmethod
    def get_entries(self, n: int) -> Optional[List[Product]]:
        pass


#

class ServersError(Exception):
    def __init__(self, server: Server, msg=None):
        self.server = server
        if msg is None:
            msg = "\nA servers error occured with server: {}".format(self.server)
        super().__init__(msg)


class TooManyProductsFoundError(ServersError):
    def __init__(self, this, number_of_products_found):
        super().__init__(*this, msg="\nToo many products were found = {}".format(number_of_products_found))
        self.number_of_products_found = number_of_products_found


class ListServer(Server):

    def __init__(self, product: Product = None, list_of_product: List[Product] = None):
        super().__init__(*args, **kwargs)
        self.list_of_product = deepcopy(list_of_product)
        self.list_of_product.append(product)

    # brakuje jeszcze super init
    def get_entries(self, n_letters: int) -> List[Product]:
        list_of_matching_products = [element for element in self.list_of_product if
                                     fullmatch('^[a-zA-Z]{{{n}}}\\d{{2,3}}$'.format(n=n_letters), element, flags=0)]
        if len(list_of_matching_products) > self.n_max_returned_entries:
            raise TooManyProductsFoundError(self, len(list_of_matching_products))

        return sorted(list_of_matching_products)


class MapServer(Server):
    def __init__(self, product: Product = None, list_of_product: List[Product] = None):
        if list_of_product:
            self.dict_of_product = {element.name: element.price for element in list_of_product}

        if product:
            self.dict_of_product[product.name] = product.price

    def get_entries(self, n_letters: int) -> List[Product]:
        list_of_matching_products = [Product(name, price) for name, price in self.dict_of_product.items() if
                                     fullmatch('^[a-zA-Z]{{{n}}}\\d{{2,3}}$'.format(n=n_letters), name, flags=0)]
        if len(list_of_matching_products) > self.n_max_returned_entries:
            raise TooManyProductsFoundError(self, len(list_of_matching_products))
        return sorted(list_of_matching_products)


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
    def __init__(self, server: Server):
        self.server = server  # ZMIEN NA REFERENCJE POZNIEJ, TAK ABY POPRAWNIE ZREALIZOWAC REFERENCJE

    def get_total_price(self, n_letters: Optional[int]) -> Optional[List[Product]]:
        try:
            list_of_products_found = self.server.get_entries(n_letters)
        except TooManyProductsFoundError:
            return None

        return list_of_products_found
