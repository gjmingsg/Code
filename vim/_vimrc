set nocompatible
"source $VIMRUNTIME/vimrc_example.vim
source $VIMRUNTIME/mswin.vim
"source $VIMRUNTIME/ruby-macros.vim
behave mswin

" 设置编码自动识别, 中文引号显示
set fileencodings=utf-8,gbk
set ambiwidth=double

" 允许退格键删除和tab操作
set smartindent  
set smarttab  
set expandtab  
set tabstop=4  
set softtabstop=4  
set shiftwidth=4  
set backspace=2
set textwidth=79
" 启用鼠标  
set mouse=a  
  
" 启用行号  
set nu 

"自动补全  
filetype plugin indent on
set completeopt=longest,menu
"自动补全命令时候使用菜单式匹配列表  
set wildmenu
autocmd FileType ruby,eruby set omnifunc=rubycomplete#Complete
autocmd FileType python set omnifunc=pythoncomplete#Complete
autocmd FileType javascript set omnifunc=javascriptcomplete#CompleteJS
autocmd FileType html set omnifunc=htmlcomplete#CompleteTags
autocmd FileType css set omnifunc=csscomplete#CompleteCSS
autocmd FileType xml set omnifunc=xmlcomplete#CompleteTags
autocmd FileType java set omnifunc=javacomplete#Complet
"Pydiction
let g:pydiction_location = 'D:\Program Files\Vim\vim72\ftplugin\complete-dict'

"TagList
let Tlist_Show_One_File=1
let Tlist_Exit_OnlyWindow=1
"tags
set tags=F:\workspace\Coder\ctags

"WinManager
let g:winManagerWindowLayout='FileExplorer|TagList'
nmap wm :WMToggle<cr>

"Grep
nnoremap <silent> <F3> :Grep<CR>

"MiniBufExplorer
let g:miniBufExplMapWindowNavVim = 1 
let g:miniBufExplMapWindowNavArrows = 1 
let g:miniBufExplMapCTabSwitchBufs = 1 
let g:miniBufExplModSelTarget = 1


" 设置backup file后缀
set backupext=.bak
" 设置backup dir
set backupdir=F:\workspace\Coder\vim_backup


set diffexpr=MyDiff()
function MyDiff()
  let opt = '-a --binary '
  if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif
  if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif
  let arg1 = v:fname_in
  if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif
  let arg2 = v:fname_new
  if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif
  let arg3 = v:fname_out
  if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif
  let eq = ''
  if $VIMRUNTIME =~ ' '
    if &sh =~ '\<cmd'
      let cmd = '""' . $VIMRUNTIME . '\diff"'
      let eq = '"'
    else
      let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'
    endif
  else
    let cmd = $VIMRUNTIME . '\diff'
  endif
  silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3 . eq
endfunction




syntax enable
syntax on
colorscheme desert
