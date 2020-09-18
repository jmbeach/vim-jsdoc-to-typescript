from jsdoc_to_typescript import JsdocToTypeScript

import vimmock
vimmock.patch_vim()
import vim

vim.setup_text("/**\n" +
" * @typedef NetSuiteSearchCreateOptions\n" +
" * @property {string} type The search type that you want to base the search on. Use the search.Type enum for this argument\n" +
" * @property {NetSuiteSearchFilter[] | string[][] | any[]} [filters]\n" +
" * @property {any[]} [filterExpression]\n" +
" * @property {string[]} [columns]\n" +
" * @property {string} [packageId]\n" +
" * @property {any[]} [settings]\n" +
" * @property {string} [title]\n" +
" * @property {string} [id]\n" +
" * @property {boolean} [isPublic]\n" +
" * ")
vim.current.set_line(" * @property {string} type The search type that you want to base the search on. Use the search.Type enum for this argument")
JsdocToTypeScript(vim).convert()
for line in vim.current.buffer:
    print(line)
print('done')
