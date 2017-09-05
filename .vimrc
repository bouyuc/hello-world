execute pathogen#infect()
syntax on
filetype plugin indent on
colorscheme jellybeans
autocmd vimenter * NERDTree
nmap <F5> :shell<CR>
nmap <F8> :TagbarToggle<CR>
nmap <F7> :NERDTreeToggle<CR>

set ruler
set number
set showcmd
set incsearch
set hlsearch

no <down> <Nop>
no <left> <Nop>
no <right> <Nop>
no <up> <Nop>


ino <down> <Nop>
ino <left> <Nop>
ino <right> <Nop>
ino <up> <Nop>

imap <leader>' ''<ESC>i
imap <leader>" ""<ESC>i
imap <leader>( ()<ESC>i
imap <leader>[ []<ESC>i
imap <leader>{ {}<ESC>i

let g:ycm_global_ycm_extra_conf = '/usr/share/vim/vimfiles/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'
