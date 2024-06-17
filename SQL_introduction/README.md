# SQL - Introduction

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer à n'importe qui, sans l'aide de Google :

**Général :**

- Qu'est-ce qu'une base de données
- Qu'est-ce qu'une base de données relationnelle
- Que signifie SQL
- Qu'est-ce que MySQL
- Comment créer une base de données dans MySQL
- Que signifient DDL et DML
- Comment créer ou modifier une table
- Comment sélectionner des données à partir d'une table
- Comment insérer, mettre à jour ou supprimer des données
- Qu'est-ce que les sous-requêtes
- Comment utiliser les fonctions MySQL

## Ressources à consulter

- [Qu'est-ce qu'une base de données et SQL ?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
- [Installer MySQL (Serveur MySQL)](https://www.youtube.com/watch?v=9h3ctGFTz9w)
- [Tutoriel de base sur MySQL](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
- [Instructions SQL de base : DDL et DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php) (pas besoin de lire le chapitre "Privileges")
- [Requêtes de base : SQL et RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
- [Technique SQL : fonctions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
- [Technique SQL : sous-requêtes](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [Quelle est la grande différence entre un backtick et une apostrophe ?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
- [Cheat Sheet MySQL](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
- [Syntaxe des instructions SQL MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

## Liens supplémentaires

- [Tutoriel MySQL en français](https://sql.sh/)

## Exigences

**Général :**

- Éditeurs autorisés : `vi`, `vim`, `emacs`
- Tous vos fichiers seront exécutés sur Ubuntu 20.04 LTS en utilisant MySQL 8.0 (version 8.0.25)
- Tous vos fichiers doivent se terminer par une nouvelle ligne
- Toutes vos requêtes SQL doivent avoir un commentaire juste avant (c'est-à-dire la syntaxe ci-dessus)
- Tous vos fichiers doivent commencer par un commentaire décrivant la tâche
- Tous les mots-clés SQL doivent être en majuscules (`SELECT`, `WHERE`, etc.)
- Un fichier `README.md`, à la racine du dossier du projet, est obligatoire
- La longueur de vos fichiers sera testée en utilisant `wc`

## Informations supplémentaires

**Commentaires pour votre fichier SQL :**

```sql
$ cat my_script.sql
-- 3 premiers étudiants dans le Batch ID=3
-- parce que le Batch 3 est le meilleur !
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

**Installer MySQL 8.0 sur Ubuntu 20.04 LTS :**

```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

**Se connecter à votre serveur MySQL :**

```bash
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

**Utiliser la sandbox pour exécuter MySQL :**

- Dans le conteneur, les identifiants sont `root/root`
- Demander un conteneur `Ubuntu 20.04`
- Se connecter via SSH
- OU se connecter via le terminal Web
- Dans le conteneur, vous devez démarrer MySQL avant de jouer avec :

```bash
$ service mysql start
 * Starting MySQL database server mysqld
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$
```
