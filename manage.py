import os
import sys
import subprocess

home_folder = os.path.expanduser('~')
vim_folder = home_folder + '/.vim'
bundle_folder = vim_folder + '/bundle'
plugin_list = vim_folder + '/plugins.txt'

#setup pathogen if necessary
if not os.path.exists(vim_folder):
    print('.VIM Not Present, setting up Pathogen\n')
    #Download Pathogen
    #Setup Temporary .vimrc

os.chdir(bundle_folder)
with open(plugin_list, 'r') as plugins:
    for block in iter(lambda: plugins.readline(), ""):
        gitstr = block.split(',')
        clonestr = 'git clone ' + gitstr[1]
        os.system(clonestr)
