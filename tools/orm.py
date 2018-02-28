from models import new_session
from tools.log import logger


# args是查询的实例，tuple_or_list是query返回的结果集
def convert_to_dict(args, tuple_or_list):
    if isinstance(tuple_or_list, tuple):
        i = 0
        dict = {}
        for arg in args:
            dict[str(arg)] = tuple_or_list[i]
            i += 1
        return dict
            
    elif isinstance(tuple_or_list, list):
        list_dict = []
        for l in tuple_or_list:
            i = 0
            dict = {}
            for arg in args:
                dict[str(arg)] = l[i]
                i += 1
            list_dict.append(dict)
        return list_dict
    
    else:
        logger.error('convert_to_dict: unknown type')
        
    return None
    

# 封装查询操作，由query返回tuple, 改为返回字典
def Query_all(*args, **kwargs):
    session = new_session()
    result = session.query(*args).all()
    session.close()
    return convert_to_dict(args, result)
    
