# Step 2: commit and push to GitHub (uses your own git login on this computer).
Set-Location "D:\Coaching Chapterwise PDFs"
if (-not (Test-Path .git)) { git init -b master }
git remote remove origin 2>$null
git remote add origin https://github.com/SakshamSharma09/CoachingChapterWisePDFs.git
git config http.postBuffer 524288000
git add -A
git commit -m "Add organised Class 5-10 practice papers, notes, answer keys and generator source"
git push -u origin master
