from fastapi import APIRouter

from database.tagservice import get_tags, careste_tag,delete_category
tag_router = APIRouter(prefix='/tag', tags=['Работа с тегами'])
# Получить все теги
@tag_router.get('/all-tags')
async def all_tags():
    return get_tags()
# Для добавления тега
@tag_router.post('/add-tag')
async def add_tag(category:str):
    new_c = careste_tag(category)
    return f'Успешно добавлен {new_c}'
# Запрос на удаление тега
@tag_router.delete('/delete_tag')
async def delete_category(category:str):
    result = delete_category(category)
    if result:
        return {'message': result}
    else:
        return {'message': 'Ничего не найдено'}
# Получить все задания определенного тега
@tag_router.get('/all-tasks-tag')
async def get_exact_task(category:str):
    return get_exact_task(category)