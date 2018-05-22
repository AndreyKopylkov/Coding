//
// Created by Андрей on 21.05.2018.
//

Subject: #include <iostream>
#include <iostream>
#include <stdlib.h>
#include <conio.h>
char str[20];
double series[1000];
double sum = 0;
for (int i = 0; i < 1000; i++)
{
series[i] = 1 / i;
sum += series[i];
}
int Field[4][4];
int EmptyX, EmptyY;
void CreateField()
{
    bool NumIsFree[15];
    int Nums[15];
    for (int i = 0; i < 15; i++)
                NumIsFree[i] = true;
    randomize();
    bool Ok;
    int RandNum;
    for (int i = 0; i < 15; i++)
            {
                    Ok = false;
            while (!Ok)
            {
                RandNum = random(15) + 1;
                от 0 до n - 1, а нам нужно от 1 до 15
                if (NumIsFree[RandNum - 1])
                Ok = true;
            }
            Nums[i] = RandNum;
            NumIsFree[RandNum - 1] = false;
            }
}
int Chaos = 0;
int CurrNum;
for (int i = 0; i < 14; i++)
{
CurrNum = Nums[i];
for (int j = i + 1; j < 15; j++)
if (CurrNum > Nums[j])
Chaos++;
}
if (Chaos % 2 == 1)
{
int temp = Nums[13];
Nums[13] = Nums[14];
Nums[14] = temp;
}
for (int i = 0; i < 15; i++)
Field[i % 4][i / 4] = Nums[i];
Field[3][3] = 0;
EmptyX = 3; EmptyY = 3;
void DrawField() //С помощью gotoxy
{
    clrscr();
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (Field[i][j])
            {
                gotoxy(i * 4 + 1, j * 3 + 1);
                std::cout « "++++";
                gotoxy(i * 4 + 1, j * 3 + 2);
                std::cout « "+";
                std::cout.width(2);
                std::cout « Field[i][j] « "+";
                gotoxy(i * 4 + 1, j * 3 + 3);
                std::cout « "++++";
            }
}
void DrawField()
{
    clrscr();
    for (int j = 0; j < 4; j++)
    {
        for (int i = 0; i < 4; i++)
        {
            if (Field[i][j])
                std::cout « "++++";
            else
            std::cout « " ";
        }
        std::cout « '\n';
        for (int i = 0; i < 4; i++)
        {
            if (Field[i][j])
            {
                std::cout « "+";
                std::cout.width(2);
                std::cout « Field[i][j] « "+";
            }
            else
                std::cout « " ";
        }
        std::cout « '\n';
        for (int i = 0; i < 4; i++)
        {
            if (Field[i][j])
                std::cout « "++++";
            else
            std::cout « " " ;
        }
        std::cout « '\n';
    }
}
enum Direction {LEFT, UP, RIGHT, DOWN};
void Move(Direction dir)
{
    switch (dir)
    {
        case LEFT:
        {
            if (EmptyX < 3)
            {
                Field[EmptyX][EmptyY] = Field[EmptyX + 1][EmptyY];
                Field[EmptyX + 1][EmptyY] = 0;
                EmptyX++;
            }
        } break;
        case UP:
        {
            if (EmptyY < 3)
            {
                Field[EmptyX][EmptyY] = Field[EmptyX][EmptyY + 1];
                Field[EmptyX][EmptyY + 1] = 0;
                EmptyY++;
            }
        } break;
        case RIGHT:
        {
            if (EmptyX > 0)
            {
                Field[EmptyX][EmptyY] = Field[EmptyX - 1][EmptyY];
                Field[EmptyX - 1][EmptyY] = 0;
                EmptyX--;
            }
        } break;
        case DOWN:
        {
            if (EmptyY > 0)
            {
                Field[EmptyX][EmptyY] = Field[EmptyX][EmptyY - 1];
                Field[EmptyX][EmptyY - 1] = 0;
                EmptyY--;
            }
        } break;
    }
}
bool FieldIsCorrect()
{
    for (int i = 0; i < 15; i++)
        if (Field[i % 4][i / 4] != i + 1)
            return false;
    return true;
}
int main()
{
    CreateField();
    DrawField();
    char c;
    while (!FieldIsCorrect()) //Игровой цикл, управление
    {
        c = getch();
        switch(c)
        {
            case 75: Move(LEFT); break;
            case 72: Move(UP); break;
            case 77: Move(RIGHT); break;
            case 80: Move(DOWN); break;
            case 27: return 0;
        }
        DrawField();
    }
    std::cout « "\n\nYou won! Press Enter to exit!";
    std::cin.get();
}
