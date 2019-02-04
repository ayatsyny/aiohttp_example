import time
from aiohttp import web
from con_db import save_db, get_all_rows


async def get_users(request):
    data = get_all_rows(query='SELECT * FROM Users')
    return web.json_response(data)


async def create_user(request):
    if 'json' not in request.content_type:
        return web.json_response({'not valid transmission format'}, status=400)

    response_json = await request.json()
    if not all(k in ('name', 'age', 'city') for k in response_json.keys()):
        return web.json_response({'not valid args'}, status=400)

    args = (response_json['name'], response_json['age'], response_json['city'])
    query = "INSERT INTO Users (name, age, city) VALUES(%s, %s, %s)"
    try:
        save_db(query, *args)
    except Exception as e:
        return web.json_response({'status': 'failed', 'message': str(e)}, status=500)
    time.sleep(10)
    return web.json_response({'status': 'success', 'message': 'user successfully created'})


if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/show_users', get_users)
    app.router.add_post('/users', create_user)
    web.run_app(app)
