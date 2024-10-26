#include <iostream>
#include <fstream>
#include <string>

#include <conio.h>
#include <map>
#include <list>
#include <cstring>
 

using namespace std;

list<string> inventory;
map<string, int> countInventory;


// retrives input from text file in project folder and adds each item to a list
// Displays astericks corresponding to the amount sold
string Multiply(int count)
{
    return string(count, '*');
}
void PopulateInventory()
{
    int total = 0;
    for (string item : inventory)
    {
        total = count(inventory.begin(), inventory.end(), item);

        countInventory.insert({ item, total });
    }
}
// Reads from the text file and adds entries to a list
//Then takeas all entries and counts them, adding to a dictionary
void ReadFile()
{
    
    ifstream newfile;
    string text;
    newfile.open("textInput.txt");
    if (newfile.is_open())
    {
        while (getline(newfile, text))
        {
            inventory.push_front(text);
        }
        newfile.close();
        PopulateInventory();
    }
}

// Menu item one takes user input to search
// presents error if item is not listed or could not be found
void MenuItemOne()
{
    system("cls");
    string userInput;


    cout << "Enter an item to search" << endl;
    cin >> userInput;

    if (countInventory.find(userInput) == countInventory.end())
    {
        cout << "Not a valid item" << endl << endl << endl;
    }
    else {
        cout << countInventory.find(userInput)->second << " " << userInput << " are found." << endl << endl << endl;
    }  
}
// iterates the entire inventory and displays to the user ordered by item name
void MenuItemTwo()
{
    system("cls");
    for (auto i = countInventory.begin(); i != countInventory.end(); i++)
        cout << i->first << " " << i->second
        << endl;
    cout << endl << endl << endl;
    cout << endl << endl << endl;
}

// functionally same as item two except the multiply function is used to display as a histogram
void MenuItemThree()
{
    for (auto i = countInventory.begin(); i != countInventory.end(); i++)
        cout << i->first << " " << Multiply(i->second)
        << endl;
    cout << endl << endl << endl;
    cout << endl << endl << endl;
}

// prints menu options to user in accordance with specifications
void MenuText()
{
    cout << "Corner Grocer Book keeper" << endl << "*************************" << endl << endl;
    cout << "Type the number for the menu option you wish to use" << endl;
    cout << "1: Item Quantity lookup." << endl;
    cout << "2: Display entire inventory." << endl;
    cout << "3: Display entire inventory as histogram." << endl;
    cout << "4: Enter quit to exit" << endl;
}

// gets user input for display option
// clears screen after each iteration to increase readability
void DisplayMenu()
{
    int userInput = -1;
    while (userInput != 4)
    {
        MenuText();
        cin >> userInput;
        if (userInput == 1)
        {
            system("cls");
            MenuItemOne();
        }
        if (userInput == 2)
        {
            system("cls");
            MenuItemTwo();
            cout << endl << endl;
        }
        if (userInput == 3)
        {
            system("cls");
            MenuItemThree();
        }
        if (userInput == 4)
        {
            system("cls");
            cout << "Thank you" << endl << endl << endl;
        }
        
    }
}

// Main entry function
int main()
{
    ofstream outPut;
    outPut.open("Frequency.dat");
    ReadFile();
    for (auto i = countInventory.begin(); i != countInventory.end(); i++)
    {
        outPut << i->first << " " << i->second << endl;
    }
    outPut.close();
    DisplayMenu();
    system("cls");
    
    return 0;
}



