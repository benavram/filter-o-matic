# -*- coding: utf-8 -*-
"""Module Name - Module Purpose

"""
from .settings import REDIS_CONN



def word_lists(list_type):
    return_list = []
    f_str = list_type + ':*'
    for key in REDIS_CONN.scan_iter(f_str):
        list_content = REDIS_CONN.hscan(key)
        list_category = list_content[1]['list_cat'.encode("utf-8")]
        word = list_content[1]['word'.encode("utf-8")]
        rating = list_content[1]['rating'.encode("utf-8")]
        wordtype = list_content[1]['word_type'.encode("utf-8")]
        tmp_lst = (wordtype.decode("utf-8"),
                   word.decode("utf-8"),
                   rating.decode("utf-8"),
                   list_category.decode("utf-8")
                   )
        return_list.append(tmp_lst)
    return return_list
