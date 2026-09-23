#!/usr/bin/env python3
import os

login_path = 'routes/login.ts'
if os.path.exists(login_path):
    with open(login_path, 'r', encoding='utf-8') as f:
        code = f.read()
    old_login = "models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: UserModel, plain: true })"
    new_login = "models.sequelize.query('SELECT * FROM Users WHERE email = :email AND password = :password AND deletedAt IS NULL', { replacements: { email: req.body.email || '', password: security.hash(req.body.password || '') }, model: UserModel, plain: true })"
    if old_login in code:
        code = code.replace(old_login, new_login)
        with open(login_path, 'w', encoding='utf-8') as f:
            f.write(code)
        print("Patched routes/login.ts")

search_path = 'routes/search.ts'
if os.path.exists(search_path):
    with open(search_path, 'r', encoding='utf-8') as f:
        code = f.read()
    old_search = "models.sequelize.query(`SELECT * FROM Products WHERE ((name LIKE '%${criteria}%' OR description LIKE '%${criteria}%') AND deletedAt IS NULL) ORDER BY name`)"
    new_search = "models.sequelize.query('SELECT * FROM Products WHERE ((name LIKE :criteria OR description LIKE :criteria) AND deletedAt IS NULL) ORDER BY name', { replacements: { criteria: `%${criteria}%` } })"
    if old_search in code:
        code = code.replace(old_search, new_search)
        with open(search_path, 'w', encoding='utf-8') as f:
            f.write(code)
        print("Patched routes/search.ts")
