ZSH='/usr/share/oh-my-zsh'
ZSH_THEME="agnoster"
ZSH_CACHE_DIR="$HOME/.cache/zsh"
DISABLE_AUTO_UPDATE='true'
DISABLE_LS_COLORS='false'
source "$ZSH/oh-my-zsh.sh"

plugins=(git archlinux zsh-autosuggestions)
alias aurs='aur search'

# Start feh in a 1920x1080 window centered on the screen where the terminal which call this funtion is.
feg(){
  feh -g 960x540+480+270 --scale-down -B "black" --info 'echo "%wx%h %n %S:%s (%u/%l)"' "$1"
}

auri(){
    aur sync --noview "$1"
    sudo pacman -S "$1"
}

auru(){
  aur sync --noview -u
  sudo pacman -Syu
}

aurr(){
  aur repo --list-path | while read -r repo_path; do
     repo-remove "$repo_path" "$@"
     paccache -c "${repo_path%/*}" -rvk0 "$@"
  done
}

() {
  local i
  for i in sudo sudox su sux
  do  eval '_my_'$i'() path=($path /sbin /usr/sbin) _'$i' "$@"
  compdef _my_'"$i $i"
  done
}

powerline-daemon -q
. /usr/share/powerline/bindings/zsh/powerline.zsh
