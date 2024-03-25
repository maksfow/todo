from database.models import Tag
from database import get_db
# Создание тегов
def careste_tag(category):
    db = next(get_db())
    new_tag = Tag( category=category)
    db.add(new_tag)
    db.commit()
    return f'Успешно создан {new_tag.category_id}'
# Получить все теги
def get_tags():
    db = next(get_db())
    tags = db.query(Tag).all()
    return tags
# Получить все задания определенного тега
def get_exact_task(category_id):
    db = next(get_db())
    checker = db.query(Tag).filter_by(category_id=category_id).all()
    if checker:
        return f'{checker.name}'
    else:
        return 'Ничего не найдено'
#Удаление тега
def delete_category(category_id):
    db = next(get_db())
    task = db.query(Tag).filter_by(category_id=category_id).first()
    if task:
        db.delete(task)
        db.commit()
        return f' {category_id} удален'
    else:
        return 'Тег не найден'


