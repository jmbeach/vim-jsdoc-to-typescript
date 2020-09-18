let g:jsdoc_to_typescript_path = expand('<sfile>:p:h') . '/jsdoc_to_typescript.py'
if !has('python') && !has('python3')
	echo "Error: JsdocToTypescript requires vim compiled with +python or +python3"
	finish
endif

function! JsdocToTypescript()
	execute (has('python3') ? 'py3file' : 'pyfile') g:jsdoc_to_typescript_path
endfunction
