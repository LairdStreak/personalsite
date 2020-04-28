XCOPY "E:\private_dev\personalsite\output" "E:\private_dev\LairdStreak.github.io" /Y /S

CD "E:\private_dev\LairdStreak.github.io"
git add .
git commit --amend --no-edit
git push -f