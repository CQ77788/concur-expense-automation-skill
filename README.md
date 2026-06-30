# Concur Expense Automation Skill

This repository contains a GitHub Copilot Skill for preparing Siemens China SAP Concur expense reports.

## Install

Copy this folder into your Copilot skills directory, for example:

```powershell
Copy-Item -Recurse . "$env:USERPROFILE\.copilot\skills\concur-expense-automation"
```

Then start Copilot CLI from any directory and ask it to use the skill.

## Use

Example:

```text
使用 concur-expense-automation skill 帮我处理报销。
附件目录：C:\Users\me\Downloads\XXXXX
报销单名称：XXXXX
Report Header Business Purpose：XX+XX+XX

```

## Scope

- Concur+ flight invoice import.
- SAP Concur itinerary / Travel Allowance.
- Hotel, taxi, business meal expense item creation.
- Receipt merging.
- Draft preparation only; no final submission.

