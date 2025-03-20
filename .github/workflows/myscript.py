import os

badhash = "HEAD"
goodhash = "HEAD~10"

os.system(f"git bisect start {badhash} {goodhash}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")
