#include "main.h"
/**
*_isdigit - fonction qui vérifie la présence d'un chiffre (0 à 9)
*@nombre: caractère testé
*Return: Renvoie 1 si c est un chiffre, sinon 0
*/

int _isdigit(int nombre)
{
	if ((nombre >= '0') && (nombre <= '9'))
	return (1);
	else
	return (0);
}
