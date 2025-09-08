# Limitless2Excel
A program that converts a Limitless TCG link (specifically for Pokemon) to an .xlsx checklist file. 

## Program Usage
To use the program, find the newest version under releases, run the .exe file, and follow the folllowing steps:
1. Enter limitlesstcg.com link into the text field and click "Confirm"
2. Click "Browse" to choose where to save your .xlsx file, or "Cancel" if you would like to go back and change the link
3. Review confirmation details, and either:
    - Click "Close Program" to close the program
    - Click "Create another .xlsx deck checklist" to repeat the process

This will create a `.xlsx` file that contains a checklist of the deck you are interested in from [limitlesstcg.com](https://limitlesstcg.com/).

**Please ensure the link you enter is in the following format: `limitlesstcg.com/decks/list/(number)`. Example link: `https://limitlesstcg.com/decks/list/18851`**

## Excel Sheet Usage
To use the Excel sheet, please edit the "amount have" column. Editing the "remaining" column's cells will remove the existing formula used to
calculate the amount of cards remaining. 

<img width="687" height="657" alt="image" src="https://github.com/user-attachments/assets/4274a8a3-8d78-4a42-b630-5f24aecd9424" />


Once the amount of cards needed is input into the "amount have" cell, the same row's "remaining" cell will turn green, indicating that the amount has been collected.

