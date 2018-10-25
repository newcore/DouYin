from tqdm import tqdm


class Downloader(object):
    
    def __init__(self, handlers=[]):
        """
        init attributes
        :param handlers:
        """
        self.handlers = handlers
    
    def add_handler(self, handler):
        """
        add one handler
        :param handler: handler object
        :return:
        """
        self.handlers.append(handler)
    
    def set_handlers(self, handlers):
        """
        set handlers
        :param handlers:
        :return:
        """
        self.handlers = handlers
    
    def get_handlers(self):
        """
        get handlers of downloader
        :return:
        """
        return self.handlers
    
    def process_item(self, obj):
        """
        process item
        :param obj: single obj
        :return:
        """
        raise NotImplementedError
    
    def process_items(self, objs):
        """
        process items
        :param objs: objs
        :return:
        """
        with tqdm(total=len(objs)) as pbar:
            for obj in objs:
                self.process_item(obj)
                pbar.update(1)
    
    def download(self, data):
        """
        download video or video lists
        :param data:
        :return:
        """
        data = data if isinstance(data, list) else [data]
        self.process_items(data)
        
        
        
    
