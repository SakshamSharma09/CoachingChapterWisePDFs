# Step 1: tidy the folder. Nothing is deleted: old scattered folders go to _old_unorganized.
$root = "D:\Coaching Chapterwise PDFs"
Set-Location $root
New-Item -ItemType Directory -Force _old_unorganized | Out-Null
Get-ChildItem -Directory | Where-Object { $_.Name -notin @('_incoming','_old_unorganized','.git') } | ForEach-Object { Move-Item -LiteralPath $_.FullName -Destination _old_unorganized }
Get-ChildItem _incoming\chunk*.zip | Sort-Object Name | ForEach-Object { Write-Host "Extracting $($_.Name)"; Expand-Archive -LiteralPath $_.FullName -DestinationPath $root -Force }
Add-Content -Path .gitignore -Value "`n_incoming/`n_old_unorganized/"
Write-Host "Done. Check the Class_05 ... Class_10 folders, then run 2_push_to_github.ps1"
