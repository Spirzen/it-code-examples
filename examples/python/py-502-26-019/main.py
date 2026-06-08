from collections.abc import MutableMapping

class TrackedDict(MutableMapping):
    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)
        self._changes = []

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        action = "update" if key in self._data else "add"
        self._changes.append((action, key, value))
        self._data[key] = value

    def __delitem__(self, key):
        old_value = self._data.pop(key)
        self._changes.append(("delete", key, old_value))

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"TrackedDict({self._data})"

    def get_changes(self):
        return self._changes.copy()

    def clear_changes(self):
        self._changes.clear()
