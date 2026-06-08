# git st → git status
git config --global alias.st "status"

# git co → git checkout
git config --global alias.co "checkout"

# git br → git branch
git config --global alias.br "branch"

# git ci → git commit
git config --global alias.ci "commit"

# git lg → красивый вывод лога
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# git amend → исправить последний коммит
git config --global alias.amend "commit --amend -C HEAD"

# git undo → отменить последний коммит (осторожно — см. "Опасные скрипты")
git config --global alias.undo "reset HEAD~1"

# git unstage → убрать файл из индекса
git config --global alias.unstage "reset HEAD --"
