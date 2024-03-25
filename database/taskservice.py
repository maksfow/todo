from database.models import Task
from database import get_db
import asyncio
# Добавление задания
def add_task(host_id, title, description, status, due_date, category):
    db = next(get_db())
    new_task = Task(host_id=host_id, title=title, description=description, status=status, due_date=due_date,
                    category=category)
    db.add(new_task)
    db.commit()
    return new_task.title_id
# Получить все задания
def get_tasks():
    db = next(get_db())
    tasks = db.query(Task).all()
    return tasks
# Получить определенное задание
def get_exact_task(category):
    db = next(get_db())
    checker = db.query(Task).filter_by(category=category).all()
    if checker:
        return f'{checker.title_name}'
    else:
        return 'Ничего не найдено'
#  Удаления задания
def delete_task(title_id):
    db = next(get_db())
    task = db.query(Task).filter_by(title_id=title_id).first()
    if task:
        db.delete(task)
        db.commit()
        return f' {title_id} удален'
    else:
        return 'Задание не найдено'
# Изменения задания
def edit_task(title_id,edit_info,new_info):
    db = next(get_db())
    exact_task = db.query(Task).filter_by(title_id=title_id).first()
    if exact_task:
        if edit_info == 'description':
            exact_task.description = new_info
        elif edit_info == 'title':
            exact_task.title = new_info
        elif edit_info == 'due_date':
            exact_task.due_date = new_info
        elif edit_info == 'category':
            exact_task.category = new_info
        db.commit()
        return 'Комментарий успешно изменен!'
    else:
        return 'Не найдено'

# Получить пользователей кто выполнил определенное задание
def get_exact_users(title_id):
    db = next(get_db())
    checker = db.query(Task).filter_by(title_id=title_id).all()
    if checker:
      return checker.userwhodid
    else:
        return 'Ничего не найдено'