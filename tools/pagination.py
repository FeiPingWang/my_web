'''
分页类
'''

class Pagination:
    def __init__(self, cur_page, total_page):
        self.page = cur_page
        self.total_page = total_page
        if cur_page > 1 and cur_page < total_page:
            self.have_next = True
            self.have_prev = True
        elif cur_page == 1:
            self.have_next = True
            self.have_prev = False
        elif cur_page == total_page:
            self.have_prev = True
            self.have_next = False
            
    def __repr__(self):
        return 'pagination cur page {}, total page {}， have next {}, have prev {}'.\
            format(self.page, self.total_page, self.have_next, self.have_prev)
            
           
            
        