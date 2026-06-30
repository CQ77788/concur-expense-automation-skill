# Example Flow: QD06150618

## Inputs

- Folder: `C:\Users\z003ybyb\Downloads\QD06150618`
- Report name: `QD06150618`
- Report Header Business Purpose: `售前+东区+马士基工厂游学交流`
- Meal deduction: 2026-06-17 dinner

## Expected Flow

1. Detect flight documents for 2026-06-15 and 2026-06-18.
2. Use Concur+ invoice folder.
3. Select six flight-related records:
   - `43610347_1`
   - `43610347`
   - `3244877249446`
   - `44560760_1`
   - `44560760`
   - `3244877567445`
4. In Concur+ reimbursement form:
   - report name: `QD06150618`
   - business usage: select dropdown `Domestic-Travel-External`
   - verify visible text before syncing.
5. Sync to Concur and wait.
6. In SAP Concur, open the synced report.
7. Set Report Header Business Purpose to `售前+东区+马士基工厂游学交流`.
8. Create itinerary rows:
   - Shanghai -> Qingdao on 2026-06-15 12:15-13:50
   - Qingdao -> Shanghai on 2026-06-18 11:30-13:10
9. In Expenses & Adjustments:
   - mark 2026-06-17 dinner provided.
   - Create Expenses.
10. Add:
   - Hotel Costs CNY 1200.
   - Taxi A CNY 351.
   - Taxi B CNY 473.60.
   - Business Meals CNY 566, Business Purpose `meal with customer`.
11. Stop before Submit Report.

