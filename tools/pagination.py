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
            
           
            
        