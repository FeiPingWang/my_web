from flask import current_app
import math
'''
分页类
'''

class Pagination:
    def __init__(self, cur_page, total_page):
        self.page = cur_page
        self.total_page = total_page
        self.have_prev = False
        self.have_next = False
        
        if cur_page < total_page:
            self.have_next = True
        if cur_page > 1:
            self.have_prev = True
            
    def __repr__(self):
        return 'pagination cur page {}, total page {}， have next {}, have prev {}'.\
            format(self.page, self.total_page, self.have_next, self.have_prev)

    @classmethod
    def get_total_page_num(cls, total, **kwargs):
        per_num = current_app.config['PER_PAG_NUM']
        divisor = total / per_num
        remainder = total % per_num
        if divisor <= 1:
            return 1
        elif divisor > 1 and remainder == 0:
            return int(divisor)
        else:
            return math.floor(divisor) + 1
           
            
        