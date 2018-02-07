# Using Atom with Github

Recent versions of Atom have integrated support for Git and GitHub.

1. Install Atom from https://atom.io/
1. Copy the URL of the repository you want to clone by navigating to
   the repository on GitHub and clicking the *Clone or Download* button.
1. In Atom, open the *Command Palette*. You'll find in the *Packages*
   menu under *Command Palette > Toggle*. (You may wish to note the
   shortcut key from the menu for later use.)
1. In the command palette, enter `github:clone`.
   As you type, the list of commands will filter down to just this one.
   Hit *ENTER* to execute the command.
1. Under *Clone from*, enter the URL you copied from GitHub.
1. Set *To directory* to the directory into which you want to clone the
   repository.
   - If you're on your own machine, use whatever directory you'd like.
   - If you're on a CS&E machine, don't clone into a folder
     on your *C:* drive; it is local to only that computer. Instead, use
     a folder on your *X:* drive, which is a file share that you can access
     from any computer in the CS&E network.
1. In the *Git* tab,
   you will see a list of files you've changed
   under *Unstaged Changes*.
   These changes are local to your develoment sandbox and have not been staged for command to GitHub (i.e., no `github add` command has been executed for them yet).
   - To stage a single file, click on it.
   - To stage all unstaged files, click *Stage All*
1. When you have the desired files staged for commit, enter a commit message
   in the text box and click the *Commit* button. This will commit your
   staged changes to your local repository.
1. To push changes to GitHub, click on the "up and down arrow" icon
   at the bottom of the *Git* tab. Click the *Push* button.
1. Your file should be pushed to GitHub.
   You may wish to go to GitHub in your web browser and check that the files you intended to push are actually present.
