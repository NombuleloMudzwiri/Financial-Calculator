# Financial-Calculator

This is a Financial calcuator program calculates either the amount of interest you'll earn on your investment or the amount you'll have to pay on a home loan (bond).

## Usage

1. Clone or download the code from this GitHub repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the code.

3. Run the program by executing the following command:

    ```bash
    python repayment_calculator.py
    ```

4. You will be prompted to choose between "investment" and "bond" repayment options. Enter your choice to proceed.

### Bond Repayment

If you choose "bond," you will need to provide the following information:

- The value of the house (e.g., 100000)
- The interest rate (e.g., 7)
- The number of months you plan to repay the bond (e.g., 120)

The program will calculate and display your monthly repayment amount.

### Investment Interest

If you choose "investment," you will need to provide the following information:

- The amount of money you are depositing
- The interest rate (numbers only, e.g., 7)
- The number of years you plan on investing
- Choose an interest type: "simple" or "compound"

The program will calculate and display your investment amount based on the chosen interest type.

## Example

Here's an example of running the program and choosing the "investment" option:

```bash
Enter either 'investment' or 'bond' from the menu above to proceed: investment
You have chosen investment as your repayment choice.
Enter the amount of money you are depositing: 10000
Enter the interest rate (NB. numbers only!): 5
Enter the number of years you plan on investing: 2
Choose interest type: 'simple' or 'compound': simple
Your investment amount will be R10500 on simple interest.
