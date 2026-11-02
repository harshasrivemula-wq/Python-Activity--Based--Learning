## 1. Problem Statement

**Campus Event Financial Planning:**  
Write a Python program to calculate the total event cost using venue, equipment, catering, transport, and certificate costs. Calculate participant contributions, sponsorship shortfall, and the minimum number of registrations required to break even.

## 2. Algorithm

1. Start.
2. Enter venue, equipment, catering, transport, and certificate costs.
3. Enter number of particiflowchart TD
4. Calculate total event cost.
5. Calculate participant contribution.
6. Calculate total income.
7. Calculate sponsorship shortfall.
8. Calculate minimum registration count needed to break even.
9. Display the financial report.
10. Check whether total income is greater than or equal to total cost.
11. Display the result.
12. Stop.

## 3. Flowchart — Mermaid Code
``` mermaid

flowchart TD
    A([Start]) --> B[/Enter venue, equipment, catering, transport and certificate costs/]
    B --> C[/Enter participants, registration fee and sponsorship/]
    C --> D[Calculate total cost]
    D --> E[Calculate participant contribution]
    E --> F[Calculate total income]
    F --> G[Calculate sponsorship shortfall]
    G --> H[Calculate minimum registration count]
    H --> I[/Display financial report/]
    I --> J{Total income >= Total cost?}
    J -->|Yes| K[Event is financially successful]
    J -->|No| L[More registrations are needed]
    K --> M([End])
    L --> M
```


## 5. Sample Input

```text
Enter venue cost: 10000
Enter equipment cost: 5000
Enter catering cost: 15000
Enter transport cost: 5000
Enter certificate cost: 2000
Enter expected participants: 100
Enter registration fee: 300
Enter sponsorship amount: 10000
```

## 6. Sample Output

```text
No sponsorship shortfall.

--- Event Financial Report ---
Total Event Cost: 37000.0
Participant Contribution: 30000.0
Sponsorship: 10000.0
Total Income: 40000.0
Minimum Registration Count: 91
Event is financially successful.
```
