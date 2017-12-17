# Pat/ to your oh-my-zsh installation.
export HOME=/home/lars
export ZSH=${HOME}/utils/oh-my-zsh

plugins=(git jump nmap docker ssh-agent  mvn archlinux)

ZSH_THEME="pygmalion"
xrdb ~/.Xresources
source $ZSH/oh-my-zsh.sh
source ${HOME}/utils/fzf/shell/completion.zsh
source ${HOME}/.config/zplug/init.zsh

export PATH="/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:${HOME}/apps/starter:${HOME}/develop/openthinclient/otc-eclipse/eclipse/:${HOME}/develop/python_scripts"
export CLASSPATH=${HOME}/utils/helperjars/*

if [[ -n $SSH_CONNECTION ]]; then
	export EDITOR='vim'
	export TERM=xterm-color
else
	export EDITOR='vim'
	export TERM=xterm-color
fi

alias ftl="find ${HOME} | fzf"
alias sue="sudo -E"
alias whobinds="ss -l -p -n | grep"
alias j="jump"
alias m="mark"

function wech {
	mv $1 $1"_wech"
}

function dall {
	docker rm $(docker ps -a -q)
	docker rmi $(docker images -q -f dangling=true)
}

function nuke {
	docker rmi $(docker images -q)
}

function dkillall {
	docker rm -f $(docker ps -q )
}

function dkill {
	docker stop $1
	docker rm $1
}

function con {
	ssh -o ServerAliveInterval=5 -o ServerAliveCountMax=1 $1
}

function dec {
	echo "$1" | gpg --decrypt
}

function vimm {
	vim ${HOME}/.vim_runtime_lars/$(cd ${HOME}/.vim_runtime_lars && fzf -m)
}


