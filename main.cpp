#include <iostream>
#include <ctime>



int main()
{
	//Universal variables
	std::string gradeA = "A";
	std::string gradeB = "B";
	std::string gradeC = "C";
	std::string gradeD = "D";
	std::string gradeF = "F";

	std::string grade = gradeC;
	
	
	//Prints out the rules of the game and how to play
	std::cout << "\nTo play this game, you choose which room you want go to by guessing if a teacher will be there too.";
	std::cout << "\nYour grade starts at a C and if you end up going to a room that a teacher is in then your grade goes up by one letter, if there is not a teacher than it goes down by a letter.";
	std::cout << "\nIf you get an A then you win, but if you get an F then you lose.";

	while (grade != gradeF || grade != gradeA)
	{
		int randomNumberForClassroom;
		bool isClassroomOccupied = false;
		int occupiedClassrooms[10];

		// srand used put at the top because it will effect ever rand usage
		srand(time(0));
		// String array creates list to define each professor to a room
		std::string professors[10] = { "Hinton", "Prater", "Clark","Bolman", "Glover","Beam","Coddington","Bowling","Beamer","Hromas" };

		// int array is used here because its is numbers rather than the names of professors
		int classroom[20] = { 106,107,108,135,201,202,203,204,205,206,207,208,231,232,234,235,244,245,252,253 };

		std::cout << "The UAT classrooms are: ";
		//This for loop lists the classrooms
		for (int i = 0; i <= 19; i++)
		{
			std::cout << "\n" << classroom[i];
		}
		// Define user choice here
		std::cout << "\nChose what classroom you want to go: ";
		int userGuess = 0;
		std::cin >> userGuess;
		std::cout << "\nYou chose to go the room corresponding with " << userGuess << ". " << std::endl;
		// Array created "usedNumbers" is going to store the random numbers that have already been generated into this array
		int usedNumbers[20];
		//This is the bell that signals the start of class
		std::cout << '\a';
		//This loop is used to link the professor to a room
		for (int i = 0; i < 10; i++)
		{
			int min = 0;
			int max = 20;
			randomNumberForClassroom = rand() % max + min;
			
			// Bool is used to logic the if statement
			bool isNumberUsed = false;
			// Second for loop is working with a different number that has to equal i for the loop to function so we used "j"
			for (int j = 0; j <= i; j++)
			{
				
					//Already used do nothing
				while (randomNumberForClassroom == usedNumbers[j])
				{
					if (randomNumberForClassroom == usedNumbers[j])
					{
						isNumberUsed = true;
						usedNumbers[i] = rand() % max + min;
						//randomNumberForClassroom = usedNumbers[i];

					}
					else
					{
						usedNumbers[i] = randomNumberForClassroom;
					}
				}
			}
			//if (isNumberUsed == false)
			//{
				//usedNumbers[i] = randomNumberForClassroom;
			//}
			//std::cout << "This is a used number " << usedNumbers[i] << ". \n";
			std::cout << "Professor " << professors[i] << " is in room " << classroom[randomNumberForClassroom] << "\n";
			occupiedClassrooms[i] = classroom[randomNumberForClassroom];
		}

		// This checks to see if the room has a teacher in it
		for (int i = 0; i <= 9; i++) {
			if (userGuess == occupiedClassrooms[i])
			{
				isClassroomOccupied = true;
			}
		}


		//This makes your grade go up a letter
		if (isClassroomOccupied == true){
			if (grade == gradeD)
			{
				grade = gradeC;
			}
			 else if (grade == gradeC)
			{
				grade = gradeB;
			}
			 else if (grade == gradeB)
			{
				grade = gradeA;
				std::cout << "\n\t\t ****Your grade is an A! Congratulations you attained the highest grade and win!****";
				std::cout << "\n\t\t Would you like to play again?";
				std::string playAgain;
				std::cin >> playAgain;
				if (playAgain == "yes") {
					main();
				}
				else {
					break;
				}
			}
			std::cout << "\nYour grade is " << grade << ".\n";
		}
		else
		{
			std::cout << "Your grade is going down a letter";
		}

		//This makes your grade go down a letter
		if (isClassroomOccupied != true)
		{
			if (grade == gradeB)
			{
				grade = gradeC;
			}
			else if (grade == gradeC)
			{
				grade = gradeD;
			}
			else if (grade == gradeD)
			{
				grade = gradeF;
				std::cout << "\n\t\t ****Your grade is an F! You failed your class!****";
				std::cout << "\n\t\t Would you like to play again?";
				std::string playAgain;
				std::cin >> playAgain;
				if (playAgain == "yes") {
					main();
				}
				else {
					break;
				}
			}
			std::cout << "\nYour grade is " << grade << ".\n";
		}
		else
		{
			std::cout << "\nYour grade is going up a letter";
		}
	}
	return 0;
}
