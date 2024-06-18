# SQL - More queries

## Description

Ce projet couvre des requêtes SQL plus avancées, y compris la création d'utilisateurs, la gestion des privilèges, les clés primaires et étrangères, les contraintes, les sous-requêtes, les jointures et les unions.

### Ressources

**Lire ou regarder :**

- [Comment créer un nouvel utilisateur et lui accorder des permissions dans MySQL - FR](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql-fr)
- [Comment utiliser l'instruction MySQL GRANT pour accorder des privilèges à un utilisateur ?- EN](https://www.mysqltutorial.org/mysql-administration/mysql-grant/)
- [Contraintes MySQL-EN](https://zetcode.com/mysql/constraints/)
- [Technique SQL : sous-requêtes-EN](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [Opération d'interrogation de base : la jointure-EN](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
- [Technique SQL : jointures multiples et mot-clé distinct-EN](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)
- [Technique SQL : types de jointures-EN](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
- [Technique SQL : l'union et la soustraction-EN](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)
- [Fiche d'information sur MySQL-EN](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
- [Les sept types de jointures SQL-EN](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
- [Tutoriel MySQLl-EN](https://www.youtube.com/watch?v=yPu6qV5byu4)
- [Guide de style SQL - FR](https://www.sqlstyle.guide/fr/)
- [Syntaxe des instructions SQL de MySQL 8.0-EN](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

**Ressources supplémentaires sur la conception de modèles de bases de données relationnelles :**

- [Design-EN](https://intranet.hbtn.io/rltoken/A81_Vk2TV-f_f5wG0HK6Zw)
- [Normalisation-EN](https://intranet.hbtn.io/rltoken/cwgE_DVy7l3ap6lCVJsPZQ)
- [Modélisation de l'ER-EN](https://intranet.hbtn.io/rltoken/1JFNpSloiEAI7aLW2rnyKw)

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer à n'importe qui, sans l'aide de Google :

**Général :**

- Comment créer un nouvel utilisateur MySQL
- Comment gérer les privilèges pour un utilisateur sur une base de données ou une table
- Qu'est-ce qu'une `PRIMARY KEY`
- Qu'est-ce qu'une `FOREIGN KEY`
- Comment utiliser les contraintes `NOT NULL` et `UNIQUE`
- Comment récupérer des données de plusieurs tables en une seule requête
- Qu'est-ce qu'une sous-requête
- Qu'est-ce que les `JOIN` et `UNION`

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

**Utiliser le sandbox pour exécuter MySQL :**

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

**Comment importer un dump SQL :**

```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
