# Testing

## Manual Testing

| Type of Test | Steps | Expected Results | Results
|--------------|-------|------------------|---------
| Name Input Test | Open deployed site https://choose-your-adventure-pp3.herokuapp.com/    |   Directs to Terminal in webpage               | Working as intended     
|              | Enter Name with numbers | Input error name cant contain numbers please try again | Working as intended |
|              | Enter Name with symbols | Input error name cant contain symbols please try again | Working as intedned |
|        | Enter name longer than 20 letters | Input error username is too long try again | Working as intended |
|        | Dont enter any name and press enter | Input error username too short try again | Working as inteded |
|        | Enter normal name with no symbols or numbers 4 letters long | Ask do you want to play a game? | Working as intended |
| Name gets called correctly throughout story | Play through story with username Paul | Named called correctly at different stages of the story | Working as intended |

| Type of Test | Steps | Expected Results | Results |
| -------------|-------|------------------|---------|
|Do you want to play User Input | Open deploted site | Directs to Terminal in webpage | Working as intended
| | Enter name correctly | Accepts name and welcomes user by name | Working as intended |
| | User is asked do they want to play? Yes/No | |
| | User types numbers | Input error please try again | Working as intended |
| | User types symbols | Input error please try again | Working as intedned |
| | User dosent type, only pressed Enter | Input error please try again | Working as intended |
| | User types Yes or Y | Game starts | Working as intended |
| | User types No or N | User is asked do they want to go back to the start | Working as intended |
| 1st choice Left or right | Type l3ft | Invalid input please try again | Working as intended |
| | Type up | Invalid input please try again | Working as intended |
| | Blank input | Invalid input please try again | Working as intended |
| | Type left | Progress to next part of story | Working as intedned |
| | Type Right | Progress to next part of story | Working as intended |
| 2nd choice(going left direction) Forward or Back | Type f0ward | Invalid input please try forward or back | Working as intended |
| | Type foorward | Invalid input please try forward or back | Working as intended |
| | Type forward | Progress to next part of story | Working as intedned |
| | Type back | Progress to next part of story | Working as intedned | 

| Game over screen | | Correctly called after going forward | Working as intended |
| Back to start in game over screen | Type y3s | Invalid input please try yes or no | Working as intended |
| | Type n0 | Invalid input please try yes or no | Working as intended |
| | type yes | Game starts over again | Working as intended | 
| | Type no | application closed | Working as intended |


## Validator Testing 

Code Institue recomended using the PEP8 Python Validator to to validate the code written for this project.

This site is no longer active so the below steps were taken to validate the code for this project.

A PEP8 validator was added to my Gitpod Workspace by following these steps.

1. Run the command pip3 install pycodestyle  Note that this extension may already be installed, in which case this command will do nothing.
2. In your workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
3. Type the word linter into the search bar that appears, and click on Python: Select Linter from the filtered results.
4. Select pycodestyle from the list.
5. PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.

See below images of problems found after installing the above PEP8 workaround.

#### Problems for run.py

- Problem on Ln 269 - line is too long. This is because of .strip().lower()
    Will to accept this problem
- Problem on Ln 70 line is too long. This is because of .strip().lower()
    Will to accept this problem
- Problem on Ln138. Line is too long. To fix this i re worded the print statement.
    See below images to support.

![run.py](assets/images/PEP8-Validator-gitpod.png)

![Ln 138 Problem](assets/images/Ln-138-problem.png)

![Ln 138 Problem Fixed](assets/images/Ln-138-problem-fixed.png)


#### Problems for stories.py

Will to accept all warnings because they are shown because of th ASCII art used.

![stories.py](assets/images/PEP8-Validator-gitpod-stories.py.png)


## Bugs

- First bug I encountered was when I started using while loops for validation.
    I didnt have any breaks in the loops so they kept running when they shouldnt of been.
    To fix this I used break to break the while loops after receiving a valid input from the user.