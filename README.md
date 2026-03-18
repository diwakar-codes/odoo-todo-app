# Odoo 17 - Todo App

A custom Odoo 17 module for managing To-Do tasks.

## Features
- Create tasks with name, description, deadline
- Set priority (Low, Medium, High)
- Mark tasks as Done
- List and Form views

## Tech Stack
- Python 3.10
- Odoo 17 Framework
- PostgreSQL
- XML Views

## Setup
1. Clone this repo into your Odoo custom_addons folder
2. Add path to addons_path in odoo.conf
3. Restart Odoo server
4. Install todo_app from Apps menu

## Module Structure
custom_addons/
└── todo_app/
    ├── __manifest__.py
    ├── models/
    │   └── models.py
    ├── views/
    │   ├── todo_views.xml
    │   └── todo_menu.xml
    └── security/
        └── ir.model.access.csv
