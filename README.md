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
附件目录：C:\Users\me\Downloads\QD06150618
报销单名称：QD06150618
Report Header Business Purpose：售前+东区+马士基工厂游学交流
6月17日晚餐需要扣减。
```

## Scope

- Concur+ flight invoice import.
- SAP Concur itinerary / Travel Allowance.
- Hotel, taxi, business meal expense item creation.
- Receipt merging.
- Draft preparation only; no final submission.

