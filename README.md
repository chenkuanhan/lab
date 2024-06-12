```
Windows PowerShell
著作權（C） Microsoft Corporation。保留擁有權利。

安裝最新的 PowerShell 以取得新功能和改進功能！https://aka.ms/PSWindows

PS C:\Users\Asus> cd C:\Users\Asus\Documents\lab
PS C:\Users\Asus\Documents\lab> & 'C:/Program Files/Git/bin/sh.exe' --login

Asus@DESKTOP-C00MOE5 MINGW64 ~/Documents/lab
$ git init
Initialized empty Git repository in C:/Users/Asus/Documents/lab/.git/

Asus@DESKTOP-C00MOE5 MINGW64 ~/Documents/lab (master)
$ git pull https://github.com/chenkuanhan/Cheat-sheet-cached.git
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 875 bytes | 46.00 KiB/s, done.
From https://github.com/chenkuanhan/Cheat-sheet-cached
 * branch            HEAD       -> FETCH_HEAD

Asus@DESKTOP-C00MOE5 MINGW64 ~/Documents/lab (master)
$ start .

Asus@DESKTOP-C00MOE5 MINGW64 ~/Documents/lab (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Cheat-sheet-cached.txt

nothing added to commit but untracked files present (use "git add" to track)

Asus@DESKTOP-C00MOE5 MINGW64 ~/Documents/lab (master)
$ git add .

Asus@DESKTOP-C00MOE5 MINGW64 ~/Documents/lab (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   Cheat-sheet-cached.txt


Asus@DESKTOP-C00MOE5 MINGW64 ~/Documents/lab (master)
$ git log
commit b2fb719b23521a88044c8cb9541c5660d932868a (HEAD -> master)
Author: chenkuanhan <104495841+chenkuanhan@users.noreply.github.com>
Date:   Wed Jun 12 08:50:44 2024 +0800

    Initial commit

Asus@DESKTOP-C00MOE5 MINGW64 ~/Documents/lab (master)
$ git commit
[master ab00d11] 1st commit after Initial commit
 1 file changed, 9 insertions(+)
 create mode 100644 Cheat-sheet-cached.txt

Asus@DESKTOP-C00MOE5 MINGW64 ~/Documents/lab (master)
$ git log
commit ab00d11dbf8a3d05b25a1df0b80082318046aff4 (HEAD -> master)
Author: Hank <kuanc1784@gmail.com>
Date:   Wed Jun 12 09:00:16 2024 +0800

    1st commit after Initial commit

commit b2fb719b23521a88044c8cb9541c5660d932868a
Author: chenkuanhan <104495841+chenkuanhan@users.noreply.github.com>
Date:   Wed Jun 12 08:50:44 2024 +0800

    Initial commit

Asus@DESKTOP-C00MOE5 MINGW64 ~/Documents/lab (master)
$ git remote -v

Asus@DESKTOP-C00MOE5 MINGW64 ~/Documents/lab (master)
$ git remote add origin https://github.com/chenkuanhan/Cheat-sheet-cached.git

Asus@DESKTOP-C00MOE5 MINGW64 ~/Documents/lab (master)
$ git push origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 20 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 461 bytes | 461.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/chenkuanhan/Cheat-sheet-cached.git
   b2fb719..ab00d11  master -> master

Asus@DESKTOP-C00MOE5 MINGW64 ~/Documents/lab (master)
$ git log
commit ab00d11dbf8a3d05b25a1df0b80082318046aff4 (HEAD -> master, origin/master)
Author: Hank <kuanc1784@gmail.com>
Date:   Wed Jun 12 09:00:16 2024 +0800

    1st commit after Initial commit

commit b2fb719b23521a88044c8cb9541c5660d932868a
Author: chenkuanhan <104495841+chenkuanhan@users.noreply.github.com>
Date:   Wed Jun 12 08:50:44 2024 +0800

    Initial commit











```
