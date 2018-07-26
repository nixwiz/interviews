# Cleanup script

Here was the original ask of the exercise:

Write a Bash script that can be used as a cron job to delete files recursively using the following parameters. You may assume that a server on which the cron job will run is properly configured to email any cron job output to the admin team.

  -  Your script should be delivered as a text file (non-executable)

Required script arguments:

- File location
  - The script must allow for one or more directories to be specified as top-level starting points for recursive file deletion
- Filename pattern
  - Only one pattern is needed but you are free to allow for more.
- Whether to delete files and/or directories
- If directories are included for deletion, provide a script argument that specifies whether they must be empty to be deleted
  - Empty directory deletion can happen after any files are deleted

Optional script arguments (the script must allow for these arguments, but does not require them to run):

- File age
  - You are free to determine the file age criteria (e.g. seconds, hours, days)
- File size
  - You are free to determine the file size criteria (e.g. bytes, kb, mb)
