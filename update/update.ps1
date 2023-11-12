Get-ChildItem -Directory ../.. | ForEach-Object {
    Write-Host $_.FullName -ForegroundColor Green
    Set-Location $_.FullName
    git pull
    Set-Location ..
}