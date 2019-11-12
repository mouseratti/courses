# https://www.tutorialspoint.com/python/os_chmod.htm
import os
import stat
import time

NEW_FILE_PATH = f"/tmp/new_file_{time.time_ns()}"
NEW_DIRECTORY_PATH = os.path.join("/tmp/", "new_directory/")

print(f"created path is {NEW_DIRECTORY_PATH}")
if not os.path.exists(NEW_DIRECTORY_PATH):
    print(f"creating dir {NEW_DIRECTORY_PATH}")
    os.mkdir(NEW_DIRECTORY_PATH,)

os.chmod(NEW_DIRECTORY_PATH, stat.S_IREAD| stat.S_IWRITE | stat.S_IEXEC |stat.S_IRGRP | stat.S_IXGRP)


os.rmdir(NEW_DIRECTORY_PATH)

collection = os.walk("/tmp", topdown=False)

print(type(collection))
for path in collection: print(path)


os.system(f"touch {NEW_FILE_PATH}")
if os.path.exists(NEW_FILE_PATH):
    print(f"file {NEW_FILE_PATH} exists, removing!")
    os.remove(NEW_FILE_PATH)

# for env in os.environ:
#     print(f"{env} : {os.environ.get(env)}")
#
# my_env_var = os.environ.get("MY_ENV_VAR")
# print(f"my_env_var value is {my_env_var}")
