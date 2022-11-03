class Manager:
    def __init__(self, _class=None):
        self._class = _class

    def search(self, **kwargs):
        """

        :param kwargs: a=2, c=12, name='ali'
        :return: obj(a=1, c=12, name='ali')
        """
        results = list()
        for key, value in kwargs.items():
            if key.endswith('__min'):
                key = key[:-5]
                compare_key = 'min'
            elif key.endswith('__max'):
                key = key[:-5]
                compare_key = 'max'
            else:
                compare_key = 'equal'
            for obj in self._class.object_list:
                if hasattr(obj, key):
                    if compare_key == 'min':
                        result = bool(getattr(obj, key) >= value)
                    elif compare_key == 'max':
                        result = bool(getattr(obj, key) <= value)
                    else:
                        result = bool(getattr(obj, key) == value)
                    if result:
                        results.append(obj)
        return results

    def get(self, **kwargs):
        for key, value in kwargs.items():
            for obj in self._class.object_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    return obj
        return None

    def count(self):
        return len(self._class.object_list)
