/**
 * @file main.cpp
 * @author your name (you@domain.com)
 * @brief
 * @version 0.1
 * @date 2022-05-09
 *
 * @copyright Copyright (c) 2022
 *
 */
#define _USE_MATH_DEFINES
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <iostream>

using std::ofstream;
using std::ifstream;
using std::vector;
using std::string;


/**
 * A - матрица системы
 * X - ответ
 * D - правая часть
 */
vector<double> solveMatrix(vector<vector<double>> A, vector<double> X, vector<double> D)
{
    int n = X.size();

    vector<double> Xi(n + 1);
	vector<double> Eta(n + 1);

	Xi[1] = A[0][1] / (-A[0][0]);
	Eta[1] = -D[0] / (-A[0][0]);

	for (int i = 2; i < n; i++)
	{
		Xi[i] = A[i - 1][i] / ((-A[i - 1][i - 1]) - A[i - 1][i - 2] * Xi[i - 1]);
		Eta[i] = (A[i - 1][i - 2] * Eta[i - 1] - D[i - 1]) / ((-A[i - 1][i - 1]) - A[i - 1][i - 2] * Xi[i - 1]);
	}

	Xi[n] = 0;
	Eta[n] = (A[n - 1][n - 2] * Eta[n - 1] - D[n - 1]) / ((-A[n - 1][n - 1]) - A[n - 1][n - 2] * Xi[n - 1]);

	X[n - 1] = Eta[n];
	for (int i = n - 2; i >= 0; i--)
	{
		X[i] = Xi[i + 1] * X[i + 1] + Eta[i + 1];
	}

	return X;
}

int main()
{
    // Потоки считывания записи
    ifstream Read("Config.txt");
    ofstream Write("Data.txt");

    // Кол-во точек по x, y, t соотвественно
    double Nx, Ny, Nt;
    // Предель по времени и координатам
    double T;
    double lx = M_PI/3, ly = M_PI/2;
    // Погрешность
    double epsilon;
    // Коэфициент теплопроводности
    double a;

    string str;
    // Считывание параметров
{
    Read >> str >> str;

    Read >> Nx; // Считываем Nx

    Read >> str >> str;

    Read >> Ny; // Считываем Ny

    Read >> str >> str;

    Read >> Nt; // Считываем Nt

    Read >> str >> str;

    Read >> T; // Считываем T

    Read >> str >> str;

    Read >> epsilon; // Считываем e

    Read >> str >> str;

    Read >> a; //Считываем a
}

    // Steps
    double hy = ly/Ny;          // y[n] = n*hy
    double t = T/Nt;            // t[n] = n * t
    double hx = lx/(Nx - 1);    // x[n] = -hx/2 + n * hx

    // Lattis[x][y][t]
    vector<vector<vector<double>>> Lattis(Nx + 1, vector<vector<double>>(Ny + 1, vector<double>(Nt + 1)));
    // Промежуточный массив
    // TransLay[x][y]
    vector<vector<double>> TransLay(Nx + 1, vector<double>(Ny + 1));

    // Матрица системы при фиксированном m
    vector<vector<double>> Ax(Nx + 1, vector<double>(Nx + 1));
    // Матрица системы при фиксированном n
    vector<vector<double>> Ay(Ny + 1, vector<double>(Ny + 1));

    // Массив неизвестных x для нахождения
    vector<double> X(Nx + 1);
    // Массив неизвестных y для нахождения
    vector<double> Y(Ny + 1);

    // Правые части уравнения системы
    // Для x
    vector<double> Dx(Nx + 1);
    // Для y
    vector<double> Dy(Ny + 1);

    // Инициализация данных в момент времени t = 0
    for(int i = 0; i < Nx; i++){
        for(int j = 0; j < Ny; j++)
        {
            Lattis[i][j][0] = cos(3 * (-hx/2 + i*hx)) * sin(4 * hy * j);
        }
    }

    // Расчет
    for(int j = 0; j <= Nt; j++)
    {
        // Неявно по x
        for(int m = 1; m < Ny; m++)
        {
            // Задание матрицы системы
            for(int i = 1; i < Nx - 1; i++)
            {
                Ax[i][i - 1] = (a * a) / (hx * hx);
				Ax[i][i] = -(2 * a * a) / (hx * hx) - 2 / t;
				Ax[i][i + 1] = (a * a) / (hx * hx);
            }

            Ax[0][0] = 1;
            Ax[0][1] = -1;

            Ax[Nx][Nx] = 1;
            Ax[Nx][Nx - 1] = -1;
            
            // Задаём правую часть уравнения
            for(int i = 1; i < Nx - 1; i++) Dx[i] = -(2 / t) * Lattis[i][m][j] -
            - ((a * a) / (hy * hy)) * (Lattis[i][m + 1][j] -
            - 2 * Lattis[i][m][j] + Lattis[i][m - 1][j]);

            X = solveMatrix(Ax, X, Dx);

            // Заполняем промежуточную матрицу
			for (int i = 0; i <= Nx; i++)
			{
				TransLay[i][m] = X[i];
			}
        }

        // Граничные условия по y
        for (int i = 0; i <= Nx; i++)
		{
			TransLay[i][0] = 0;
			TransLay[i][Ny] = 0;
		}

        // Неявная по y
        for(int n = 1; n < Nx; n++)
        {
            // Задаем нач. и конечные значения матрицы
            Ay[0][0] = 1;
            Ay[0][1] = 0;

            Ay[Ny][Ny] = 1;
            Ay[Ny][Ny - 1] = 0;

            // Задаем внутрение значения матрицы
            for(int i = 1; i < Ny; i++)
            {
                Ay[i][i - 1] = (a * a) / (hy * hy);
				Ay[i][i] = -(2 * a * a) / (hy * hy) - 2 / t;
				Ay[i][i + 1] = (a * a) / (hy * hy);
            }

            // Задаём правую часть уравнения
            for(int i = 1; i < Ny - 1; i++) Dy[i] = -(2 / t) * TransLay[n][i] -
            - ((a * a) / (hx * hx)) * (TransLay[n + 1][i] - 2 * TransLay[n][i] +
            + TransLay[n - 1][i]);

            // Первое и последенее значение правой части
            Dy[0] = 0;
            Dy[Ny] = 0;

            Y = solveMatrix(Ay, Y, Dy);

            // Записываем значение в массив ответа
            for (int i = 0; i <= Ny; i++)
			{
				Lattis[n][i][j + 1] = Y[i];
			}
        }

        // Заполнение фиктивной прямой
        for (int i = 0; i <= Ny; i++)
		{
			Lattis[0][i][j + 1] = Lattis[1][i][j + 1];
			Lattis[Nx][i][j + 1] = Lattis[Nx - 1][i][j + 1];
		}
    }

    vector<double> times(1);
    times[0] = 3;

    
}