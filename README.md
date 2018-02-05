Information Systems Design

This is your private repository for working and submitting homework
assignments.

Each homework assignment is stored in a separate folder within this
repository.

Development Environment
=======================

You are welcome to use whatever development environment you prefer. If
you don’t have a preference, I recommend that you use PyCharm. The full
"professional" version is installed on the lab machines, and is
available for free for students to download and use. Follow these steps:

1.  Download PyCharm at <https://www.jetbrains.com/pycharm/>.

2.  Install it on your machine.

3.  Apply for a free student license at
    <https://www.jetbrains.com/student/>.

4.  Follow the instructions in the e-mail you will receive that contains
    your license.

Getting Started
===============

To get started, you will clone your Github repository to your *sandbox*
on your CSE share.

Follow these steps:

1.  Run PyCharm

2.  From the **Welcome to PyCharm** window, click **Check out from
    Version Control**

3.  Click **Github**

4.  Fill out the following details:

    1.  For **Git Repository URL**, enter
        `https://github.com/tu-isd/individual-labs-<your-github-id>.git`
        except substitute your actual Github ID for `<your-github-id>`

    2.  For **Parent Directory** and **Directory Name**, choose a
        sensible location on your CSE share.

5.  Click the **Clone** button.

These steps should create a new PyCharm project that contains starter
files for the ISD homework assignments.

Installing Python Modules (Automated Process)
=============================================

For both individual homework assignments and the project, you will have
to install Python modules in addition to those installed by default.

For example, say you want to use Flask. Your Python code would include
in `import` statement like this:

    from flask import Flask

If Flask is not yet installed, PyCharm will show a squiggly underline
below `flask` to indicate that it doesn’t know about this module.

PyCharm is incredibly helpful when you need a new module.

1.  Click to place your cursor on `flask` in the `import` statement, and
    hit **Alt+Enter**. This will open up a suggestions menu for
    resolving the error. The first suggestion should be
    `Install package <package-name>`.

2.  Select the `Install package` option. PyCharm will install the
    package. You’ll see a progress bar at the bottom of the PyCharm
    window as the installation completes.

Installing Python Modules (Manual Process)
==========================================

If the automatic process for module installation doesn’t work, here are
detailed manual instructions for installing a module.

1.  Run PyCharm

2.  Open PyCharm’s setttings, which are found under different menus
    depending on your computer.

    -   On a Mac, from the **PyCharm** menu, choose **Preferences…**

    -   On Windows, from the **File** menu, choose **Settings…**

3.  In the list on the left, find the **Project** section.

    -   If **Project Interpreter** *is* shown beneath **Project**, click
        on **Project Interpreter**

    -   If **Project Interpreter** is *not* show beneath **Project**,
        either:

        -   Click the triangle to the left of **Project**, then click on
            **Project Interpreter**

        -   Click on **Project**, the click on **Project Interpreter**
            in the main section of the window.

4.  The **Project Interpreter** window shows a list of packages
    currently installed. Check that the package you need isn’t already
    installed. If it is, you’re done—click **Cancel**.

5.  Click the **+** button at the bottom of the package list. A window
    containing available packages appears.

6.  In the search box at the top of the **Available Packages** window,
    type (a portion of) the name of the package you want to install. For
    example, to install Flask, type `Flask`.

7.  Many packages have related names. For example, there are a lot of
    packages that extend Flask that are named `Flask-<something>`. Make
    sure the correct package name is selected in the list on the left.

8.  Click **Install Package** at the bottom of the window.

9.  While the package installs, you’ll see `(Installing)` next to the
    package name. When installation is complete, a message highlighted
    in green tells you that the package was installed correctly.

10. Close the **Available Packages** window. (Unless you want to install
    more packages; in that case, search for the next package and
    repeat.)

11. Check that the list of installed packages includes the package you
    just installed.

12. Click **OK** to dismiss the settings window.

Working on an Assignment
========================

Following are general instructions for all assignments.

Update your Sandbox (Optional)
------------------------------

Before working on an assignment, you may wish to update your sandbox
from Github to make sure you have the latest-and-greatest version of the
files for the assignment. Do this as follows within PyCharm:

1.  From the **VCS** menu, choose **Update Project…**

2.  From the **Update Project** window, leave the default options
    selected and click **OK**.

Instructions
------------

Instructions for the assignment are found in a file called `README.adoc`
at the top level of each folder. The `README.adoc` file (an `asciidoc`
file) should be legible as is, but if you would like to read a nicely
formatted version, refer to the file on Github, which formats `.adoc`
files automatically as HTML.

You are welcome to use any starter files in the homework directory to
get going on the assignment.

Submitting an Assignment
========================

When you’ve completed an assignment, you’ll need to push your updated
repository back to Github, where your work will be available for
grading.

Add New Files
-------------

If you created any new files while working on the assignment, you’ll
need to add them to revision control *before* you push your completed
assignment to Github. To use PyCharm to check whether you have files not
yet under revision control

1.  From the **View** menu, choose **Tool Windows** &gt; **Version
    Control**.

2.  The **Version Control** window appears

3.  Choose the **Local Changes** tab.

4.  Check whether there are files listed as **Unversioned Files**.

5.  If so, and if the file(s) listed are ones that are part of the
    project (and not just temporary files that you don’t want to turn
    in), right click on the file and choose **Add to VCS**. This will
    register the file with Git and it will be submitted when you push
    your changes to Github.

Commit and Push
---------------

Although commit and push are two separate Git operations, PyCharm makes
it easy to do both when you are ready to submit your assignment.

1.  From the **VCS** menu, click **Commit Changes**. `PyCharm` opens the
    **Commit Changes** dialog box.

2.  In the top-left window, `PyCharm` shows you the files that are going
    to be committed. Make sure there aren’t any files that you *don’t*
    want to commit, or files that are not listed there that you *do*
    want to commit (see above for information on how to add new files to
    Git).

3.  Write a brief commit message in the window in the lower-left corner
    of the dialog box. Commit messages are extremely valuable when
    working on a team project so that you can communicate (and
    remember!) what you’ve done. **When your homework submission is
    ready for grading, please start your commit message with
    `READY FOR GRADING`.**

4.  Hover over the highlighted **Commit** button in the lower-right
    corner.

5.  A pop-up menu appears. Choose **Commit and Push…**

6.  After the commit is complete, the **Push Commits** dialog appears.
    Click **Push** to push your changes to Github.

Verify your Submission
----------------------

Just to make sure everything you intended to submit is available on
Github, you should log on to your Github account, navigate to the
appropriate homework folder in your repository, and verify that all the
files you intended to submit are present.
