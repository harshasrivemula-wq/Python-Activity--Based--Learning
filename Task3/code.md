## 1. Problem Statement

Develop a **Student Email and Identifier Validation System** to validate a student's email address and registration ID. The program should identify missing components, spaces, incorrect formats, and invalid character groups.

## 2. Algorithm

1. Start.
2. Enter the student email and registration ID.
3. Split the email using `@`.
4. Check whether the email has exactly one `@`.
5. Check username, domain, spaces, and domain extension.
6. Display the email validation result.
7. Check whether the registration ID is empty.
8. Check spaces and minimum length.
9. Check whether the first three characters are letters.
10. Check whether the remaining characters are digits.
11. Display the registration ID validation result.
12. Stop.

## 3. Flowchart
```mermaid
flowchart TD
    A[Start] --> B[Enter email and registration ID]
    B --> C[Split email using @]
    C --> D{Exactly two parts?}
    D -->|No| E[Display malformed separator]
    D -->|Yes| F[Check username and domain]
    F --> G{Username or domain empty?}
    G -->|Yes| H[Display missing component]
    G -->|No| I{Space found?}
    I -->|Yes| J[Display invalid space]
    I -->|No| K{Dot in domain?}
    K -->|No| L[Display missing domain]
    K -->|Yes| M{Username starts with digit?}
    M -->|Yes| N[Display invalid username]
    M -->|No| O[Display email is valid]
    E --> P[Validate registration ID]
    H --> P
    J --> P
    L --> P
    N --> P
    O --> P
    P --> Q{Registration ID empty?}
    Q -->|Yes| R[Display missing ID]
    Q -->|No| S{Space found?}
    S -->|Yes| T[Display malformed ID]
    S -->|No| U{Length less than 6?}
    U -->|Yes| V[Display ID too short]
    U -->|No| W{First 3 are letters?}
    W -->|No| X[Display invalid beginning]
    W -->|Yes| Y{Remaining are digits?}
    Y -->|No| Z[Display invalid characters]
    Y -->|Yes| AA[Display registration ID is valid]
    R --> AB[End]
    T --> AB
    V --> AB
    X --> AB
    Z --> AB
    AA --> AB
```
## 4. Sample Input

```text
Enter student email: student@gmail.com
Enter registration ID: ABC123
```

## 5. Sample Output

```text
--- Email Validation ---
Email is valid.

--- Registration ID Validation ---
Registration ID is valid.
```
