
classname = lambda obj: obj.__class__.__name__


class BufferMock(object):
    def __init__(self, text=None):
        self.setup_text(text)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self._lines[key.start : key.stop : key.step]
        if not isinstance(key, int):
            raise TypeError("Index should be integer, not %s" % classname(key))
        return self._lines[key]

    def __len__(self):
        return len(self._lines)

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            self._lines[key.start : key.stop : key.step] = value
        elif not isinstance(key, int):
            raise TypeError("Indes should be integer, not %s" % classname(key))
        self._lines[key] = value

    def index(self, object, start=None, stop=None):
        if start is not None:
            return self._lines.index(object, start)
        if stop is not None:
            return self._lines.index(object, start, stop)
        return self._lines.index(object)

    def insert(self, index, object):
        return self._lines.insert(index, object)

    def setup_text(self, text=None):
        self._text = text or ''
        self._lines = self._text.splitlines()


class WindowMock(object):
    def __init__(self, cursor=None):
        self.cursor = cursor or (0, 0)


class RangeMock(object):
    pass


class CurrentMock(object):
    def __init__(self, text=None):
        self.line = ""
        self.buffer = BufferMock(text)
        self.window = WindowMock()
        self.range = RangeMock()

    def set_line(self, line):
        self.line = line


class VimMock(object):

    def __init__(self):
        self.current = CurrentMock()

    def setup_text(self, text):
        self.current.buffer.setup_text(text)

