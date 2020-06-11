# Created by sarathkaul on 13/11/19

import os
import random

for year in range(2016, 2018):
    os.system("mkdir " + str(year))
    os.chdir(str(year))
    for month in range(1, 13):
        os.system("mkdir " + str(month))
        os.chdir(str(month))
        total_days = random.randint(1, 31)
        for day in range(1, total_days):
            os.system("mkdir " + str(day))
            os.chdir(str(day))
            total_commits = random.randint(1, 12)
            for a_commit in range(total_commits):
                os.system(
                    "echo '"
                    + str(a_commit)
                    + " on "
                    + str(month)
                    + "/"
                    + str(day)
                    + "/"
                    + str(year)
                    + "' > commit.md"
                )
                # os.system(
                #     "export GIT_COMMITTER_DATE='"
                #     + str(year)
                #     + "-"
                #     + str(month)
                #     + "-"
                #     + str(day)
                #     + " "
                #     + "12:"
                #     + str(a_commit)
                #     + ":00'"
                # )
                # os.system(
                #     "export GIT_AUTHOR_DATE='"
                #     + str(year)
                #     + "-"
                #     + str(month)
                #     + "-"
                #     + str(day)
                #     + " "
                #     + "12:"
                #     + str(a_commit)
                #     + ":00'"
                # )
                os.system("git add commit.md -f")
                os.system(
                    "git commit --date='"
                    + str(year)
                    + "-"
                    + str(month)
                    + "-"
                    + str(day)
                    + " 12:0"
                    + str(a_commit)
                    + ":00'"
                    + " "
                    + "-m"
                    + "'"
                    + str(a_commit)
                    + " on "
                    + str(month)
                    + " "
                    + str(day)
                    + " "
                    + str(year)
                    + "'"
                )

            os.chdir("../")
        os.chdir("../")
    os.chdir("../")
os.chdir("../")

# git push origin branch-name
# git rm -rf 20**
# git rm -rf 19**
# git commit -am "cleanup"
# git push origin branch-name
