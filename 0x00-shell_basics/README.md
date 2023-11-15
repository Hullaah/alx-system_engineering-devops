# 0x00-shell_basics

This is the directory for project 0x00-shell_basics. It was part of the project done during the ALX software enginerring programme to learn about devops.
Some of the tasks included in the project are:

## 0-current_working_directory
File: [0-current_working_directory](0-current_working_directory)

- This task involves writing a script that prints the absolute pathname of the current working directory.
- I used the ```pwd``` command for the task.

It works this way:
```bash
[hullaah@fedora 0x00-shell_basics]$ ./0-current_working_directory 
/home/hullaah/Documents/ALX/alx-system_engineering-devops/0x00-shell_basics
[hullaah@fedora 0x00-shell_basics]$
```
## 1-listit
File: [1-listit](1-listit)

- This task involves writing a script that displays the contents list of your current directory
- I used the ```ls``` command for the task.

It works this way:
```bash
[hullaah@fedora 0x00-shell_basics]$ ./1-listit 
0-current_working_directory  102-tree    11-lists          14-copy_html     3-listfiles           6-firstdirectory  9-firstdirdeletion
100-lets_move                103-commas  12-file_type      1-listit         4-listmorefiles       7-movethatfile    README.md
101-clean_emacs              10-back     13-symbolic_link  2-bring_me_home  5-listfilesdigitonly  8-firstdelete     school.mgc
[hullaah@fedora 0x00-shell_basics]$ 
```
## 2-bring_me_home
File: [2-bring_me_home](2-bring_me_home)
- This task involves writing a script that changes the working directory to the current user's home directory.
- The requirements was not to use any shell variables
- I used the command ```cd ~```
- ```~``` expands to the current user's home directory. You can confirm by using this command in your shell:
```bash
[hullaah@fedora 0x00-shell_basics]$ echo ~
/home/hullaah
[hullaah@fedora 0x00-shell_basics]$ 
```
You can test it with:
```bash
[hullaah@fedora 0x00-shell_basics]$ source ./2-bring_me_home 
[hullaah@fedora ~]$
```
## 3-listfiles
File: [3-listfiles](3-listfiles)
- This task involves writing a script that displays current directory content in a long format
- I used the command ```ls``` with the flag ``` -l```
- The ```-l``` flag in the ls command specifies that ls should use a long listing format

It works this way:
```bash
[hullaah@fedora 0x00-shell_basics]$ ./3-listfiles 
total 84
-rwxr-xr-x. 1 hullaah hullaah   16 Sep 27 21:45 0-current_working_directory
-rwxr-xr-x. 1 hullaah hullaah   35 Sep 27 21:45 100-lets_move
-rwxr-xr-x. 1 hullaah hullaah   18 Sep 27 21:45 101-clean_emacs
-rwxr-xr-x. 1 hullaah hullaah   39 Sep 27 21:45 102-tree
-rwxr-xr-x. 1 hullaah hullaah   34 Sep 27 21:45 103-commas
-rwxr-xr-x. 1 hullaah hullaah   17 Sep 27 21:45 10-back
-rwxr-xr-x. 1 hullaah hullaah   30 Sep 27 21:45 11-lists
-rwxr-xr-x. 1 hullaah hullaah   31 Sep 27 21:45 12-file_type
-rwxr-xr-x. 1 hullaah hullaah   33 Sep 27 21:45 13-symbolic_link
-rwxr-xr-x. 1 hullaah hullaah   28 Sep 27 21:45 14-copy_html
-rwxr-xr-x. 1 hullaah hullaah   15 Sep 27 21:45 1-listit
-rwxr-xr-x. 1 hullaah hullaah   17 Sep 27 21:45 2-bring_me_home
-rwxr-xr-x. 1 hullaah hullaah   18 Sep 27 21:45 3-listfiles
-rwxr-xr-x. 1 hullaah hullaah   19 Sep 27 21:45 4-listmorefiles
-rwxr-xr-x. 1 hullaah hullaah   20 Sep 27 21:45 5-listfilesdigitonly
-rwxr-xr-x. 1 hullaah hullaah   42 Sep 27 21:45 6-firstdirectory
-rwxr-xr-x. 1 hullaah hullaah   50 Sep 27 21:45 7-movethatfile
-rwxr-xr-x. 1 hullaah hullaah   45 Sep 27 21:45 8-firstdelete
-rwxr-xr-x. 1 hullaah hullaah   42 Sep 27 21:45 9-firstdirdeletion
-rwxr-xr-x. 1 hullaah hullaah 2198 Nov 13 12:24 README.md
-rwxr-xr-x. 1 hullaah hullaah  752 Sep 27 21:45 school.mgc
[hullaah@fedora 0x00-shell_basics]$
```
## 4-listmorefiles
File: [4-listmorefiles](4-listmorefiles)
- This task involves writing a script that displays current directory content, including hidden files (starting with `.`), in a long format
- I used the command ```ls``` with the flag ``` -la```
- The ```-l``` flag in the ls command specifies that ls should use a long listing format
- The `-a` flag specifies that ls should also list hidden files

It works this way:
```bash
[hullaah@fedora 0x00-shell_basics]$ ./4-listmorefiles 
total 84
drwxr-xr-x. 1 hullaah hullaah  554 Sep 27 21:45 .
drwxr-xr-x. 1 hullaah hullaah 1006 Oct 25 11:17 ..
-rwxr-xr-x. 1 hullaah hullaah   16 Sep 27 21:45 0-current_working_directory
-rwxr-xr-x. 1 hullaah hullaah   35 Sep 27 21:45 100-lets_move
-rwxr-xr-x. 1 hullaah hullaah   18 Sep 27 21:45 101-clean_emacs
-rwxr-xr-x. 1 hullaah hullaah   39 Sep 27 21:45 102-tree
-rwxr-xr-x. 1 hullaah hullaah   34 Sep 27 21:45 103-commas
-rwxr-xr-x. 1 hullaah hullaah   17 Sep 27 21:45 10-back
-rwxr-xr-x. 1 hullaah hullaah   30 Sep 27 21:45 11-lists
-rwxr-xr-x. 1 hullaah hullaah   31 Sep 27 21:45 12-file_type
-rwxr-xr-x. 1 hullaah hullaah   33 Sep 27 21:45 13-symbolic_link
-rwxr-xr-x. 1 hullaah hullaah   28 Sep 27 21:45 14-copy_html
-rwxr-xr-x. 1 hullaah hullaah   15 Sep 27 21:45 1-listit
-rwxr-xr-x. 1 hullaah hullaah   17 Sep 27 21:45 2-bring_me_home
-rwxr-xr-x. 1 hullaah hullaah   18 Sep 27 21:45 3-listfiles
-rwxr-xr-x. 1 hullaah hullaah   19 Sep 27 21:45 4-listmorefiles
-rwxr-xr-x. 1 hullaah hullaah   20 Sep 27 21:45 5-listfilesdigitonly
-rwxr-xr-x. 1 hullaah hullaah   42 Sep 27 21:45 6-firstdirectory
-rwxr-xr-x. 1 hullaah hullaah   50 Sep 27 21:45 7-movethatfile
-rwxr-xr-x. 1 hullaah hullaah   45 Sep 27 21:45 8-firstdelete
-rwxr-xr-x. 1 hullaah hullaah   42 Sep 27 21:45 9-firstdirdeletion
-rwxr-xr-x. 1 hullaah hullaah 4065 Nov 13 12:33 README.md
-rwxr-xr-x. 1 hullaah hullaah  752 Sep 27 21:45 school.mgc
[hullaah@fedora 0x00-shell_basics]
```
## 5-listfilesdigitonly
File: [5-listfilesdigitonly](5-listfilesdigitonly)
- This task involves writing a script that displays current directory contents in long format with user and group IDs displayed numerically And hidden files (starting with .)
- I used the command `ls` with the flags `-na`
- The `-a` flag specifies that ls should also list hidden files
- The `-n` flag works like `-l` flag, but lists numeric user and group IDs

It works this way:
```bash
[hullaah@fedora 0x00-shell_basics]$ ./5-listfilesdigitonly 
total 88
drwxr-xr-x. 1 1000 1000  554 Sep 27 21:45 .
drwxr-xr-x. 1 1000 1000 1006 Oct 25 11:17 ..
-rwxr-xr-x. 1 1000 1000   16 Sep 27 21:45 0-current_working_directory
-rwxr-xr-x. 1 1000 1000   35 Sep 27 21:45 100-lets_move
-rwxr-xr-x. 1 1000 1000   18 Sep 27 21:45 101-clean_emacs
-rwxr-xr-x. 1 1000 1000   39 Sep 27 21:45 102-tree
-rwxr-xr-x. 1 1000 1000   34 Sep 27 21:45 103-commas
-rwxr-xr-x. 1 1000 1000   17 Sep 27 21:45 10-back
-rwxr-xr-x. 1 1000 1000   30 Sep 27 21:45 11-lists
-rwxr-xr-x. 1 1000 1000   31 Sep 27 21:45 12-file_type
-rwxr-xr-x. 1 1000 1000   33 Sep 27 21:45 13-symbolic_link
-rwxr-xr-x. 1 1000 1000   28 Sep 27 21:45 14-copy_html
-rwxr-xr-x. 1 1000 1000   15 Sep 27 21:45 1-listit
-rwxr-xr-x. 1 1000 1000   17 Sep 27 21:45 2-bring_me_home
-rwxr-xr-x. 1 1000 1000   18 Sep 27 21:45 3-listfiles
-rwxr-xr-x. 1 1000 1000   19 Sep 27 21:45 4-listmorefiles
-rwxr-xr-x. 1 1000 1000   19 Nov 13 12:41 5-listfilesdigitonly
-rwxr-xr-x. 1 1000 1000   42 Sep 27 21:45 6-firstdirectory
-rwxr-xr-x. 1 1000 1000   50 Sep 27 21:45 7-movethatfile
-rwxr-xr-x. 1 1000 1000   45 Sep 27 21:45 8-firstdelete
-rwxr-xr-x. 1 1000 1000   42 Sep 27 21:45 9-firstdirdeletion
-rwxr-xr-x. 1 1000 1000 6038 Nov 13 12:43 README.md
-rwxr-xr-x. 1 1000 1000  752 Sep 27 21:45 school.mgc
[hullaah@fedora 0x00-shell_basics]$
```
## 6-firstdirectory
File: [6-firstdirectory](6-firstdirectory)
- This task involves writing a script that creates a directory named my_first_directory in the /tmp/ directory
- I used the `mkdir` command for the task
## 7-movethatfile
File: [7-movethatfile](7-movethatfile)
- This task involves writing a script that moves the file betty from /tmp/ to /tmp/my_first_directory.
- I used the `mv` command

## 8-firstdelete
File: [8-firstdelete](8-firstdelete)
- This task involves writing a script that deletes the file betty from /tmp/my_first_directory
- I used the `rm` command
## 9-firstdirdeletion
File: [9-firstdirdeletion](9-firstdirdeletion)
- This task involves writing a script that deletes the directory my_first_directory that is in the /tmp directory.
- I used the `rmdir` command
## 10-back
File: [10-back](10-back)
- This task involves writing a script that changes the working directory to the previous one.
- I used the `cd` command

It works this way:
```bash
[hullaah@fedora alx-system_engineering-devops]$ pwd
/home/hullaah/Documents/ALX/alx-system_engineering-devops
[hullaah@fedora alx-system_engineering-devops]$ cd 0x00-shell_basics/
[hullaah@fedora 0x00-shell_basics]$ pwd
/home/hullaah/Documents/ALX/alx-system_engineering-devops/0x00-shell_basics
[hullaah@fedora 0x00-shell_basics]$ source ./10-back 
/home/hullaah/Documents/ALX/alx-system_engineering-devops
[hullaah@fedora alx-system_engineering-devops]$ pwd
/home/hullaah/Documents/ALX/alx-system_engineering-devops
[hullaah@fedora alx-system_engineering-devops]$
```
