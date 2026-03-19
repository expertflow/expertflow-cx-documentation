esx# Git Cheat Sheet (Commands You Used)

## 1) Create a new file (Windows PowerShell)
```powershell
New-Item -Path "newfile.md" -ItemType File
```

## 2) Add the new file to Git (stage it)
```bash
git add newfile.md
```

## 3) Commit your change
```bash
git commit -m "Add newfile.md"
```

## 4) Push the commit to GitHub
```bash
git push
```

> If pushing a new branch for the first time:
```bash
git push -u origin <branch-name>
```

## 5) Revert local working changes (undo edits)
```bash
git restore .
```

## 6) Remove the file from the repo (delete + commit + push)
```bash
git rm newfile.md
git commit -m "Remove newfile.md"
git push
```

---

## Helpful status / troubleshooting commands

- Show current status:
```bash
git status
```

- Check Git version:
```bash
git --version
```

- Make sure PowerShell can find Git (if `git` is not recognized):
```powershell
Get-Command git
where.exe git
```
