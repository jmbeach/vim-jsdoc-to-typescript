import vim
import re
from vimmock.mocked import VimMock


class JsdocToTypeScript(object):
    def __init__(self, vim):
        """
        @type vim: VimMock
        """
        self._vim = vim

    def convert_line(self, buffer_index, current_line):
        regex = r"\* \@property \{([a-zA-Z0-9[\] |]+)\} (\[?)([a-zA-Z0-9]+)\]?(.*)"
        match = re.search(regex, current_line)
        type_name = match.groups()[0]
        is_optional = match.groups()[1].strip() == '['
        name = match.groups()[2]
        description = match.groups()[3].strip()
        new_line = name
        if is_optional:
            new_line += '?'

        new_line += ': ' + type_name + ';'
        self._vim.current.buffer[buffer_index] = new_line
        if description is not None and description != '':
            self._vim.current.buffer.insert(buffer_index, '/** @description ' + description + ' */')
            return buffer_index + 2
        return buffer_index + 1

    def convert(self):
        line = self._vim.current.line
        buffer_index = self._vim.current.buffer.index(line)
        current_line = self._vim.current.buffer[buffer_index];
        while '@property' in current_line and buffer_index < len(self._vim.current.buffer):
            buffer_index = self.convert_line(buffer_index, current_line)
            if buffer_index < len(self._vim.current.buffer):
                current_line = self._vim.current.buffer[buffer_index]


JsdocToTypeScript(vim).convert()
