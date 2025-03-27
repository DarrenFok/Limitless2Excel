# Limitless2Excel
A script that converts a Limitless TCG link (specifically for Pokemon) to an .xlsx checklist file. 

## Script Usage
To use the script, run the following command in a command terminal:

`python limitless2excel.py "<limitlesstcg.com link>" "<desired excel sheet name>"`

This will create a `.xlsx` file that contains a checklist of the deck you are interested in from [limitlesstcg.com](https://limitlesstcg.com/).

## Excel Sheet Usage
To use the Excel sheet, please edit the "amount have" column. Editing the "remaining" column's cells will remove the existing formula used to
calculate the amount of cards remaining. 

![image](https://github.com/user-attachments/assets/017ca642-0de4-48c0-aee9-b2318da56eaf)

Once the amount of cards needed is input into the "amount have" cell, the same row's "remaining" cell will turn green, indicating that the amount has been collected.

