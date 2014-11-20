Abstract
===============
This command is used to execute commands with locking. It also provides a way to try `N` times before failure.

###Explanation
This script accepts as input a command to be executed and the corresponding lock file. The lock file is used to ensure
that the command can only be used by the process which creates the lock file. The lock file is deleted after the command has been
run. This ensures mutual exclusion.

Also accepted as optional input is a threshold value and a file to record the number of times the command has been attempted.
If the lock cannot be acquired then the number of attempts is retrieved from the attempts count file and compared
with the threshhold. If the attempts reaches or exceeds the threshold then the scripts indicates that the execution failed.
Otherwise the attempts count is incremented and the script exits normally.

The process of creating the lock file is as follows:

1. A temporary file with the desired path is created with the `.tmp` extension.
2. If this file already exists then a false is returned.
3. The newly created temp file is then symlinked to the required file.
4. If this command completes successfully then `True` is returned, else `False`