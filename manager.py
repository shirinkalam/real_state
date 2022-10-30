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
            for obj in self._class.object_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    results.append(obj)
        return results

    def get(self, **kwargs):
        for key, value in kwargs.items():
            for obj in self._class.object_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    return obj
        return None
