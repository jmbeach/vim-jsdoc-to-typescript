import vim
import re
# from vimmock.mocked import VimMock


class JsdocToTypeScript(object):
    def __init__(self, vim):
        """
        @type vim: VimMock
        """
        self._vim = vim
    
    def get_buffer_index(self, object):
        for i in range(0, len(self._vim.current.buffer)):
            if self._vim.current.buffer[i] == object:
                return i
        return -1

    def insert_buffer(self, index, object):
        self._vim.current.buffer.append("");
        for i in reversed(range(index, len(self._vim.current.buffer))):
            self._vim.current.buffer[i] = self._vim.current.buffer[i - 1]
        self._vim.current.buffer[index] = object

    def convert_line(self, buffer_index, current_line):
        regex = r"\*\s+(\@param|\@property)\s+\{(?P<type>[a-zA-Z0-{}9[\]=>(): |.]+)\}\s+(?P<is_optional>\[?)(?P<name>[a-zA-Z0-9_.]+)\]?(?P<description>.*)"
        match = re.search(regex, current_line)
        type_name = match.group('type')
        is_optional = match.group('is_optional').strip() == '['
        name = match.group('name')
        description = match.group('description').strip()
        new_line = '\t' + name
        if is_optional:
            new_line += '?'

        new_line += ': ' + type_name + ';'
        self._vim.current.buffer[buffer_index] = new_line
        if description is not None and description != '':
            self.insert_buffer(buffer_index, '/** @description ' + description + ' */')
            return buffer_index + 2
        return buffer_index + 1

    def convert(self):
        line = self._vim.current.line
        buffer_index = self.get_buffer_index(line)
        current_line = self._vim.current.buffer[buffer_index];
        while ('@property' in current_line or '@param' in current_line) and buffer_index < len(self._vim.current.buffer):
            buffer_index = self.convert_line(buffer_index, current_line)
            if buffer_index < len(self._vim.current.buffer):
                current_line = self._vim.current.buffer[buffer_index]


JsdocToTypeScript(vim).convert()
